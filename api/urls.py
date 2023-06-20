from django.contrib import admin
from django.urls import path

import api.views as api_views

app_name = "api"

urlpatterns = [
    path("recommender/", api_views.RecommenderAPI.as_view()),
    path(
        "<uuid:product_id>/recommendations/",
        api_views.GetProductRecommendationsAPI.as_view(),
    ),
    path("orders/create/", api_views.CreateOrderAPI.as_view()),
    path(
        "orders/<uuid:order_id>/products/add/", api_views.AddProductToOrderAPI.as_view()
    ),
    path(
        "orders/<uuid:order_id>/products/<uuid:product_id>/remove/",
        api_views.RemoveProductFromOrderAPI.as_view(),
    ),
]
