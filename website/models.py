from django.db import models
from datetime import datetime, date
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
#from phonenumber_field.modelfields import PhoneNumberField
#from phonenumber_field.formfields import PhoneNumberField

# Create your models here.
class Company(models.Model):
	# Info
	company_name = models.CharField(max_length=50)
	company_logo = models.FileField()
	company_email = models.EmailField(max_length=50)
	company_password = models.CharField(max_length=50)
	company_number = models.CharField(max_length=50)

	# Addres
	company_address = models.CharField(max_length=200)
	company_post_code = models.CharField(max_length=200)
	company_country = models.CharField(max_length=200)
	company_state = models.CharField(max_length=200)

	def __str__(self):
		return self.company_name

class QRScanMember(models.Model):

	phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$', message="Phone number must not consist of space and requires country code. eg : +6591258565")

	full_name = models.CharField(max_length=50)
	contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
	temperature = models.FloatField(validators=[MinValueValidator(35), MaxValueValidator(40)])
	time_stamp = models.TimeField(auto_now=False, auto_now_add=True, blank=True)
	date_stamp = models.DateField(auto_now=False, auto_now_add=True, blank=True)

	def __str__(self):
		return self.full_name 
