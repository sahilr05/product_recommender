from django.contrib import admin

from recommender_app.models import Order
from recommender_app.models import OrderProduct
from recommender_app.models import Product

admin.site.register([Order, Product, OrderProduct])
