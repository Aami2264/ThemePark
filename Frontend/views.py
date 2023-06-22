from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.html import format_html

from Backend.models import Ticketdb, Gallerydb, Activitydb, Feedbackdb, FamilyTicketdb, BirthdayTicketdb, SchoolTicketdb


def homepage(request):
    data = Ticketdb.objects.all()
    return render(request,'index.html',{'data':data})

def aboutus(request):
    return render(request,'About.html')

def gallerydisp(request):
    data = Gallerydb.objects.all()
    return render(request,'Gallerydisp.html',{'data':data})

def activitydisp(request):
    data = Activitydb.objects.all()
    return render(request,'Activitydisp.html',{'data':data})

def activityeach(request,dataid):
    data = Activitydb.objects.get(id=dataid)
    return render(request,'Activityeach.html',{'data':data})

def contactus(request):
    return render(request,'Contact.html')

def feedback(request):
    if request.method=="POST":
        n = request.POST.get('name')
        p = request.POST.get('phone')
        e = request.POST.get('email')
        msg = request.POST.get('message')
        obj = Feedbackdb(Name=n, Phone=p,Email=e, Message=msg)
        obj.save()
        return redirect('contactus')

def map(request):
    return render(request,'Map.html')

def ticketdetail(request):
    data = Ticketdb.objects.all()
    return render(request,'TicketDetail.html',{'data':data})


def selectpack(request):
    return render(request,'SelectPack.html')

def familyform(request):
    data = Ticketdb.objects.all()
    return render(request,'FamilyForm.html',{'data':data})

def savebooking(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('phone')
        e = request.POST.get('email')
        d = request.POST.get('date')
        a = request.POST.get('span')
        obj = FamilyTicketdb(Name=n,Phone=p,Email=e,Date=d,Amount=a)
        obj.save()
        messages.success(request, "Ticket Reserved")
        return redirect('homepage')

def birthdayform(request):
    return render(request,'BirthdayForm.html')

def savebdaybooking(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('phone')
        e = request.POST.get('email')
        d = request.POST.get('date')
        g = request.POST.get('guests')
        a = request.POST.get('age')
        obj = BirthdayTicketdb(Name=n,Phone=p,Email=e,Date=d,Guests=g, Age=a)
        obj.save()
        messages.success(request, "Thank You!!!We will contact you SOON!")
        return redirect('homepage')

def schoolform(request):
    return render(request,'SchoolForm.html')

def saveschoolbooking(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('phone')
        e = request.POST.get('email')
        d = request.POST.get('date')
        obj = SchoolTicketdb(Name=n,Phone=p,Email=e,Date=d)
        obj.save()
        messages.success(request, "Thank You!!!We will contact you SOON!")
        return redirect('homepage')

# Create your views here.
