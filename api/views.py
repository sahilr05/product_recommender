from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api import recommender
from api import services
from api.models import Product
from api.types import CurrencyCode
from api.types import PaymentMode
from api.types import states_as_list

# Create your views here.


class RecommenderAPI(APIView):
    def get(self, request):
        """Check celery task and update product recommendations."""
        print("check celery task")
        recommender.update_product_recommendations.apply_async()
        return Response(status=status.HTTP_200_OK)


class GetProductRecommendationsAPI(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = "__all__"

    def get(self, request, product_id: str) -> Response:
        """Get recommendations for a product with the given ID."""
        recommendations = services.recommend_products(product_id)
        serialized_recommendations = self.OutputSerializer(
            recommendations, many=True
        ).data
        return Response(data=serialized_recommendations, status=status.HTTP_200_OK)


class CreateOrderAPI(APIView):
    class InputSerializer(serializers.Serializer):
        product_id = child = serializers.UUIDField()
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        currency_code = serializers.ChoiceField(choices=states_as_list(CurrencyCode))
        quantity = serializers.IntegerField()
        address = serializers.CharField()
        payment_mode = serializers.ChoiceField(choices=states_as_list(PaymentMode))

    def post(self, request) -> Response:
        """Create an order with the given data."""
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_data = services.create_order(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class RemoveProductFromOrderAPI(APIView):
    def post(self, request, order_id: str, product_id: str) -> Response:
        """Remove a product with the given ID from an order with the given ID."""
        services.remove_product_from_order(order_id, product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddProductToOrderAPI(APIView):
    class InputSerializer(serializers.Serializer):
        product_id = child = serializers.UUIDField()
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        currency_code = serializers.ChoiceField(choices=states_as_list(CurrencyCode))
        quantity = serializers.IntegerField()

    def post(self, request, order_id: str) -> Response:
        """Add a product to an order with the given ID."""
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.add_product_to_order(order_id, **serializer.validated_data)
        return Response(status=status.HTTP_204_NO_CONTENT)
