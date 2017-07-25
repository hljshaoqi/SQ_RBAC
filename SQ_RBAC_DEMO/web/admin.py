from django.contrib import admin

from .models import UserInfo, Order

admin.site.register(UserInfo)
admin.site.register(Order)
