from django.forms import ModelForm
from .models import QRScanMember

class MemberQRForm(ModelForm):
	class Meta:
		model = QRScanMember
		fields = ['first_name', 'last_name', 'contact_number', 'temperature', 'purpose_of_visitation']