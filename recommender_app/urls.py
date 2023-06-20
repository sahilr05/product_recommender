from django.contrib import admin
from django.urls import path

import recommender_app.views as api_views

app_name = "recommender_app"

urlpatterns = [
    path("precompute-recommendations/", api_views.RecommenderAPI.as_view()),
    path(
        "products/<uuid:product_id>/recommendations/",
        api_views.GetProductRecommendationsAPI.as_view(),
        name="recommendations",
    ),
    path("orders/create/", api_views.CreateOrderAPI.as_view(), name="create_order"),
    path(
        "orders/<uuid:order_id>/",
        api_views.DetailOrderAPI.as_view(),
        name="detail_order",
    ),
    path(
        "orders/<uuid:order_id>/products/add/",
        api_views.AddProductToOrderAPI.as_view(),
        name="add_product_to_order",
    ),
    path(
        "orders/<uuid:order_id>/products/<uuid:product_id>/remove/",
        api_views.RemoveProductFromOrderAPI.as_view(),
        name="remove_product_from_order",
    ),
]
