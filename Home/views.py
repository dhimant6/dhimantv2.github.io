from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("My love Tera Patrick")
    conext = {
        "variable": "It will start in next 6 months"
    }
    return render (request,'index.html',conext)
def want(request):
    return HttpResponse("I want gf like Faye and want to fuck her for 3 days NONSTOP every week for atleast 2 months")

def about(request):
    return render (request, 'about.html')

def resume(request):
    return render (request, 'resume.html')

def projects(request):
    return render (request, 'projects.html')

def contact(request):
    return render (request, 'contact.html')