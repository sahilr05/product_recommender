from django.contrib import admin

from api.models import Order, Product, OrderProduct

admin.site.register([Order, Product, OrderProduct])