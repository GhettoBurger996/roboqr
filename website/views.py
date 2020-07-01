from django.shortcuts import render

# Create views here
from .models import *
from .qrform import MemberQRForm
from .qrform import CreateComapnyForm

# Regsiter
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'login.html', {})

def confirmation(request):
	return render(request, 'confirmation.html', {})

def register(request):
	form = CreateComapnyForm()

	if request.method == 'POST':
		form = CreateComapnyForm(request.POST)
		if form.is_valid():
			form.save()
	
	context = {'form':form}
	return render(request, 'register.html', context)

def qrform(request):
	form = MemberQRForm()
	
	if request.method == "POST":
		form = MemberQRForm(request.POST or None)
		if form.is_valid():
			form.save()
		return render(request, 'qrform.html', {})

	else:
		return render(request, 'qrform.html', {})

def dashboard(request):
	members = QRScanMember.objects.all()

	total_members = members.count()

	return render(request, 'dashboard.html', {'total_members' : total_members})

def dashboard_table(request):
	members = QRScanMember.objects.all()
	return render(request, 'dashboard_table.html', {'members': members})
