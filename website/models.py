from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

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
		return self.company_name + ' ' + self.company_email

class QRScanMember(models.Model):

	full_name = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=50)
	temperature = models.CharField(max_length=50)

	def __str__(self):
		return self.full_name + ' ' + self.contact_number + ' ' + self.temperature
