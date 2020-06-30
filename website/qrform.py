from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MemberQRForm(ModelForm):
	class Meta:
		model = QRScanMember
		fields = ['full_name', 'contact_number', 'temperature']

class CreateComapnyForm(ModelForm):
	class Meta:
		model = Company
		fields = ['company_name', 'company_email', 'company_password', 
				  'company_number', 'company_address', 'company_post_code',
				  'company_country', 'company_state']
