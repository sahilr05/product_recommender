from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from api.models import Product
from rest_framework.views import APIView
from rest_framework import serializers
from api import recommender
from api.types import states_as_list, CurrencyCode, PaymentMode
from api import services
# Create your views here.


# class RecommenderAPI(APIView):
#     def get(self, request):
#         recommender.calculate_recommendations()

class GetProductRecommendationsAPI(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = "__all__"

    def get(self, request, product_id):
        recommendations = recommender.recommend_products(product_id)
        return Response(data=recommendations, status=status.HTTP_200_OK)
    
class CreateOrderAPI(APIView):
    class InputSerializer(serializers.Serializer):
        product_id = child=serializers.UUIDField()
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        currency_code = serializers.CharField(choices=states_as_list(CurrencyCode), max_length=100)
        quantity = serializers.IntegerField()
        address = serializers.CharField()
        payment_mode = serializers.CharField(choices=states_as_list(PaymentMode), max_length=100)
    
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_data = services.create_order(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    
class RemoveProductFromOrderAPI(APIView):
    def post(self, request, order_id, product_id):
        services.remove_product_from_order(order_id, product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AddProductToOrderAPI(APIView):
    class InputSerializer(serializers.Serializer):
        product_id = child=serializers.UUIDField()
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        currency_code = serializers.CharField(choices=states_as_list(CurrencyCode), max_length=100)
        quantity = serializers.IntegerField()
    
    def post(self, request, order_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.add_product_to_order(order_id, **serializer.validated_data)
        return Response(status=status.HTTP_204_NO_CONTENT)