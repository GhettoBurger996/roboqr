from django.forms import ModelForm
from .models import QRScanMember

class MemberQRForm(ModelForm):
	class Meta:
		model = QRScanMember
		fields = ['full_name', 'contact_number', 'temperature']