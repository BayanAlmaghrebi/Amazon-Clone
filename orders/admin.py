from django.contrib import admin

# Register your models here.
from .models import Order , OrderDetail , Cart , CartDetail , Coupon


admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(Coupon)
admin.site.register(CartDetail)
