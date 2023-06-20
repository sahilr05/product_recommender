from django.contrib import admin
from django.urls import path
import api.views as api_views

app_name = "api"

urlpatterns = [
    path("recommender/", api_views.RecommenderAPI.as_view()),
    path("<uuid:product_id>/recommendations/", api_views.GetProductRecommendationsAPI.as_view())
]
