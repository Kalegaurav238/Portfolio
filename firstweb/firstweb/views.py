from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .froms import usersdata
from service.models import Service
from news.models import News
from contactenquriy.models import contactenquriy


def homePage(request):
    newsData=News.objects.all();
    servicesData = Service.objects.all()
    data={
        'newsData':newsData,
       'servicesData':servicesData
    }
    return render(request,"index.html",data)
def contactenquriy(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        project = request.POST.get('project')
        message = request.POST.get('message')
        en = contactenquriy(name=name,email=email,project=project,message=message)
        en.save()
    return render(request, "contact.html")

def aboutus(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output })
def newsDetail(request,slug):
    newsDetail=News.objects.get(news_slug=slug)
    data={
        'newsDetail': newsDetail
    }
    return render(request, "newsdetails.html",data)
def education(request):
    return render(request,"education.html")
def submitform(request):
    try:
        if request.method == "POST":
            # n1 = int(request.GET['num1'])
            # n2 = int(request.GET['num2'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
        finalans = n1 + n2
        data = {
            'n1': n1,
            'n2': n2,
            'output': finalans
        }
        url = "/about-us/?output={}".format(finalans)
        return redirect(url)
    except:
        pass
def portfolio(request):
    return render(request,"portfolios.html")
def contact(request):
    return render(request,"contact.html")
def course(request):
    return HttpResponse("Hello1")
def courseDetails(request,courseid):
    return HttpResponse(courseid)

def userForm(request):
    finalans = 0
    fn=usersdata()
    data={'form':fn}
    try:
        if request.method=="POST":
            # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
        finalans = n1+n2
        data={
            'form': fn,
            'n1': n1,
            'n2': n2,
            'output': finalans
        }
        url="/about-us/?output={}".format(finalans)
        return redirect(url)

    except:
        pass
    return render(request,"userform.html",data)
def evenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request, "evenodd.html", {'error':True})
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Number is Even"
        else:
            c="Number is Odd"
    return render(request, "evenodd.html", {'c':c})