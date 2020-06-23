from django.shortcuts import render
from .models import *
from .qrform import MemberQRForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'login.html', {})

def register(request):
	all_members = QRScanMember.objects.all
	return render(request, 'register.html', {'all': all_members})

def qrform(request):
	if request.method == "POST":
		form = MemberQRForm(request.POST or None)
		if form.is_valid():
			form.save()
		return render(request, 'qrform.html', {})

	else:
		return render(request, 'qrform.html', {})

def dashboard(request):
	return render(request, 'dashboard.html', {})

def dashboard_table(request):
	members = QRScanMember.objects.all()
	return render(request, 'dashboard_table.html', {'members': members})
