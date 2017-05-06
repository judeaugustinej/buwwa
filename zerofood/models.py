from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class UserType(models.Model):
    user_type = models.CharField(max_length=10)

    def __str__(self):
    	return self.user_type


class FoodType(models.Model):
    food_type = models.CharField(max_length=10)

    def __str__(self):
    	return self.food_type


class FoodState(models.Model):
	food_state = models.CharField(max_length=30)

	def __str__(self):
		return self.food_state

"""
class FoodRequest(models.Model):
	# one food state allowed
    food_state = models.OneToOneField(FoodState, on_delete=models.CASCADE)
    # many type of food can be sponsered
    food_type  = 
    food_quantity = 
    date_of_request =
    # user can change the already registered given number.
    contact_number = 
    # location =
    # recevie the data for location from form
    # for doner has to recevied from user and stored.
    # for ngo can be taken from profile db or updated and stored here.
    # has to stored in db for donner
    # user_id find way to find it
"""


class Profile(models.Model):
    # blank = True ie empty field is allowed.
    role = models.OneToOneField(UserType, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = PhoneNumberField()
    location = models.CharField(max_length=70)
    # how to set ngo_id to 7-digits.
    ngo_id = models.IntegerField()
    #photo = models.
    description = models.TextField(max_length=500, blank=True)
