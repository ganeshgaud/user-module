from django.shortcuts import render
from .models import Student,User
from .forms import StudentForm,SignupForm

# Create your views here.
def registration(request):
    form1=SignupForm()
    form2=StudentForm()
    if request.method=="POST":
        form1=SignupForm(request.POST)
        if form1.is_valid():
            user=form1.save()
            studentform = StudentForm(request.POST)
            studentform.instance.user = user
            if studentform.is_valid():
                studentform.save()
    return render(request,'reg.html',{'form1':form1,'form2':form2})

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "myapp/upload_csv.html", data)
