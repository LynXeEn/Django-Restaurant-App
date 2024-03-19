from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    POSITION_CHOICES = {
        "W": "Waiter",
        "MG": "Manager",
        "B": "Bar",
        "DW": "DishWasher"
    }

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Dish(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=150)
    calories = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + str(self.calories)


class DishRestaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.dish.name + ' - ' + self.restaurant.name


class BusinessHours(models.Model):
    day_of_week = {
        "Mon": "Monday",
        'Tue': 'Tuesday',
        'Wed': 'Wednesday',
        'Thu': 'Thursday',
        'Fri': 'Friday',
        'Sat': 'Saturday',
        'Sun': 'Sunday'
    }

    day = models.CharField(max_length=4, choices=day_of_week)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    time_from = models.TimeField()
    time_to = models.TimeField()
