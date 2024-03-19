from django.contrib import admin

# Register your models here.

from .models import Restaurant, DishRestaurant, Employee, BusinessHours, Dish

admin.site.register(Restaurant)
admin.site.register(DishRestaurant)
admin.site.register(Employee)
admin.site.register(BusinessHours)
admin.site.register(Dish)
