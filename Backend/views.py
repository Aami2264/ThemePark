from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

from Backend.models import  Ticketdb, Activitydb, Gallerydb, Feedbackdb, FamilyTicketdb, BirthdayTicketdb, \
    SchoolTicketdb, Staffdb


def indexpage(request):
    ndata = Feedbackdb.objects.all()
    return render(request,'Home.html',{'ndata':ndata})

def loginpage(request):
    return render(request,'login.html')

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                messages.success(request, "Login Successful")

                return redirect(indexpage)
            else:
                messages.error(request, "Invalid User")
                return redirect(loginpage)
        else:
            messages.error(request, "Invalid User")
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def addstaff(request):
    ndata = Feedbackdb.objects.all()
    return render(request,'Addadmin.html',{'ndata':ndata})

def saveadmin(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('mobile')
        d = request.POST.get('date')
        im = request.FILES['image']
        obj = Staffdb(Name=n, Email=e, Mobile=m, Date=d, Image=im)
        obj.save()
        messages.success(request, "Staff Added")
        return redirect(addstaff)


def displayadmin(request):
    ndata = Feedbackdb.objects.all()
    data = Staffdb.objects.all()
    return render(request,'Displayadmin.html',{'data':data,'ndata':ndata})

def delete(request,dataid):
    data = Staffdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(displayadmin)

def edit(request,dataid):
    ndata = Feedbackdb.objects.all()
    data = Staffdb.objects.get(id=dataid)
    return render(request, 'Edit.html', {'data':data,'ndata':ndata})

def update(request,dataid):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('mobile')
        d = request.POST.get('date')

        try:
            im = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = Staffdb.objects.get(id=dataid).Image
        Staffdb.objects.filter(id=dataid).update(Name=n,Email=e,Mobile=m,Date=d,Image=file)
        messages.success(request, "Updated")
        return redirect(displayadmin)


def addtickets(request):
    ndata = Feedbackdb.objects.all()
    return render(request,'Addtickets.html',{'ndata':ndata})

def saveticket(request):
        if request.method == "POST":
            n = request.POST.get('name')
            d = request.POST.get('description')
            r = request.POST.get('rate')
            obj = Ticketdb(Name=n, Description=d, Rate=r)
            obj.save()
            messages.success(request, "Successfully Added")
            return redirect(addtickets)

def displaytickets(request):
        ndata = Feedbackdb.objects.all()
        data = Ticketdb.objects.all()
        return render(request, 'Displaytickets.html', {'data': data,'ndata':ndata})

def editticket(request,dataid):
    ndata = Feedbackdb.objects.all()
    data = Ticketdb.objects.get(id=dataid)
    return render(request, 'Editicket.html', {'data': data,'ndata':ndata})

def deleteticket(request,dataid):
    data = Ticketdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(displaytickets)

def updateticket(request,dataid):
    if request.method=="POST":
        n = request.POST.get('name')
        d = request.POST.get('description')
        r = request.POST.get('rate')
        Ticketdb.objects.filter(id=dataid).update(Name=n, Description=d, Rate=r)
        messages.success(request, "Updated")
        return redirect(displaytickets)

def addactivities(request):
    ndata = Feedbackdb.objects.all()
    return render(request,'Addactivities.html',{'ndata':ndata})

def saveactivities(request):
    if request.method=="POST":
        n = request.POST.get('name')
        r = request.POST.get('role')
        d = request.POST.get('description')
        du = request.POST.get('duration')
        c = request.POST.get('content')
        im = request.FILES['image']
        obj = Activitydb(Name=n, Role=r, Description=d, Duration=du,Content=c, Image=im)
        obj.save()
        messages.success(request, "Activity Successfully Added")
        return redirect(addactivities)

def displayactivities(request):
    ndata = Feedbackdb.objects.all()
    data = Activitydb.objects.all()
    return render(request,'DisplayActivities.html',{'data':data,'ndata':ndata})

def editactivity(request,dataid):
    ndata = Feedbackdb.objects.all()
    data = Activitydb.objects.get(id=dataid)
    return render(request,'EditActivity.html',{'data':data,'ndata':ndata})

def updateactivity(request,dataid):
    if request.method=="POST":
        n = request.POST.get('name')
        r = request.POST.get('role')
        d = request.POST.get('description')
        du = request.POST.get('duration')
        c = request.POST.get('content')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Activitydb.objects.get(id=dataid).Image
        Activitydb.objects.filter(id=dataid).update(Name=n, Description=d, Image=file)
        messages.success(request, "Updated")
        return redirect(displayactivities)

def deleteactivity(request,dataid):
    data = Activitydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(displayactivities)

def gallery(request):
    ndata = Feedbackdb.objects.all()
    return render(request,'Gallery.html',{'ndata':ndata})

def saveimages(request):
    im = request.FILES['image']
    obj = Gallerydb(Image=im)
    obj.save()
    messages.success(request, "Image Added")
    return redirect('gallery')

def displaygallery(request):
    ndata = Feedbackdb.objects.all()
    data = Gallerydb.objects.all()
    return render(request,'DisplayGallery.html',{'data':data,'ndata':ndata})

def deleteimage(request,dataid):
    data = Gallerydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect('displaygallery')

def feedbackdisp(request):
    ndata = Feedbackdb.objects.all()
    data = Feedbackdb.objects.all()
    return render(request,'Feedbackdisp.html',{'data':data,'ndata':ndata})

def deletemsg(request,dataid):
    data = Feedbackdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect('feedbackdisp')

def familyreserved(request):
    data = Feedbackdb.objects.all()
    dat = FamilyTicketdb.objects.all()
    return render(request,'FamilyTickets.html',{'data': data, 'dat': dat})

def deleteticket(request,dataid):
    data = FamilyTicketdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect('familyreserved')

def birthdayreserved(request):
    data = Feedbackdb.objects.all()
    dat = BirthdayTicketdb.objects.all()
    return render(request,'BirthdayTickets.html',{'data': data, 'dat': dat})

def deletebdayticket(request,dataid):
    data = BirthdayTicketdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect('birthdayreserved')

def schoolreserved(request):
    data = Feedbackdb.objects.all()
    dat = SchoolTicketdb.objects.all()
    return render(request,'SchoolTickets.html',{'data': data, 'dat': dat})

def deleteschoolticket(request,dataid):
    data = SchoolTicketdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect('schoolreserved')
