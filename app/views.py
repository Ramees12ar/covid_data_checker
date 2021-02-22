from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from covid import Covid

# Create your views here.

def index(request):
	return render(request,"covid.html",{})

def home(request):
	return render(request,"covid.html",{})

def check(request):
	try:
		covid = Covid()
		n=request.POST.get("country")
		case= covid.get_status_by_country_name(n)
		print(case)
		active = case["active"]
		confirmed = case["confirmed"]
		recovered = case["recovered"]
		deaths = case["deaths"]
		return render(request,"covid.html",{"active":active,"confirmed":confirmed,"recovered":recovered,"deaths":deaths})
	except:
		return HttpResponse("<script>alert('No Data Available');window.location.href='/home/';</script>")
