from django.contrib import admin

from api.models import Order
from api.models import OrderProduct
from api.models import Product

admin.site.register([Order, Product, OrderProduct])
