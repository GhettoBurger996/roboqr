from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Company(models.Model):
	# Info
	company_name = models.CharField(max_length=50)
	company_logo = models.FileField()
	company_email = models.EmailField(max_length=50)
	company_password = models.CharField(max_length=50)
	company_number = PhoneNumberField()

	# Addres
	company_address = models.CharField(max_length=200)
	company_post_code = models.CharField(max_length=200)
	company_country = models.CharField(max_length=200)
	company_state = models.CharField(max_length=200)


class ScanPersonnel(models.Model):
	purpose_visitation_choices = [
	('WK', 'Work'),
	('VT', 'Visit'),
	]

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	company_number = PhoneNumberField()
	temperature = models.FloatField()
	purpose_of_visitation = models.CharField(
		max_length=2,
		choices=purpose_visitation_choices,
		default=False)
	

