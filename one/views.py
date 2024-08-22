from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q 
import random,string
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def webpage(request):
    return render(request,"webpage.html")


def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            c=Customer.objects.filter(user=request.user)
            if c:
                return redirect(userhome)
            
    return render(request,"Customer/customer-login.html")


def driverlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            d=Driver.objects.filter(user=request.user)
            if d:
                return redirect(appointment)        
    return render(request,"Driver/driver-login.html")


def userregister(request):
    if request.method=="POST":
        form=Userform(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password1')
        if form.is_valid():
            form.save()
            user=authenticate(request,username=username,password=password)
            login(request,user)
            Customer.objects.get_or_create(user=request.user)
            return redirect(completeuserprofile) 
    form=Userform() 
    context={
        'form':form,
    }
    return render(request,"Customer/customer-register.html",context)


@login_required(login_url=webpage)
def completeuserprofile(request):
    if request.method=="POST":
        form=CustomerProfileForm(request.POST,request.FILES)
        customer=Customer.objects.get(user=request.user)
        print(customer)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=customer
            obj.save()
            return redirect(userhome)
    form=CustomerProfileForm()
    context={
        'form':form,
    }
    return render(request,"Customer/customer-profileform.html",context)

  
def driverregister(request):
    if request.method=="POST":
        form=Userform(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password1')
        if form.is_valid():
            form.save()
            user=authenticate(request,username=username,password=password)
            login(request,user)
            Driver.objects.get_or_create(user=request.user)
            return redirect(completedriverprofile)      
    form=Userform()  
    context={
        'form':form,
    }
    return render(request,"Driver/driver-register.html",context)


@login_required(login_url=webpage)
def completedriverprofile(request):
    if request.method=="POST":
        form=DriverProfileForm(request.POST,request.FILES)
        driver=Driver.objects.get(user=request.user)
        if form.is_valid():
            print("hello")
            obj=form.save(commit=False)
            obj.user=driver
            obj.save()
            return redirect(appointment)
    form=DriverProfileForm()
    context={
        'form':form,
    }
    return render(request,"Driver/driver-profileform.html",context)


@login_required(login_url=webpage)
def logoutall(request):
    if request.method=="POST":
        logout(request)
        return redirect(webpage)
    return render(request,"logout.html")


@login_required(login_url=webpage)
def userhome(request):
    d=Driverprofile.objects.all().order_by('?')
    context={
        'drivers':d,
    }
    return render(request,"Customer/customer-home.html",context)


@login_required(login_url=webpage)
def bookdriver(request,id):
    d=Driverprofile.objects.get(id=id)
    c=Customer.objects.get(user=request.user)
    u=Customerprofile.objects.get(user=c)
    if request.method=="POST":
        form=BookingForm(request.POST)
        print(form)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.client=u
            obj.driver=d
            obj.save()
            return redirect(schedules)
    
    form=BookingForm()
    context={
        'driver':d,
        'form':form,
    }
    
    return render(request,"Customer/customer-booking.html",context)


@login_required(login_url=webpage)
def schedules(request):
    c=Customer.objects.get(user=request.user)
    p=Customerprofile.objects.get(user=c)
    b=Bookings.objects.filter(client=p).order_by('schedule')
    paid=Payment.objects.values_list('booking', flat=True)
    context={
        'p':p,
        'bookings':b,
        'payments':paid,
    }
    return render(request,"Customer/customer-schedules.html",context)
    
    
@login_required(login_url=webpage) 
def payment(request,id):
    b=Bookings.objects.get(id=id)
    if request.method=="POST":
        form=PaymentForm(request.POST)
        amount=request.POST.get('amount')
        transc_id="WHID"+''.join([random.choice(string.digits) for n in range(8)])
        print(transc_id)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.booking=b
            obj.trans_id=transc_id
            obj.save()
            info={
                'booking':b,
                'transactionid':transc_id,
                'amount':amount,
            }
            return render(request,"Customer/confirm-payment.html",info)

    form=PaymentForm()  
    context={
        'booking':b,
        'form':form,
    }
    return render(request,"Customer/customer-payment.html",context)


@login_required(login_url=webpage)
def allpayments(request):
    c=Customer.objects.get(user=request.user)
    p=Customerprofile.objects.get(user=c)
    t=Payment.objects.filter(booking__client=p)
    print(t)
    context={
        'transactions':t,
    }
    return render(request,"Customer/customer-transactions.html",context)
    
    
@login_required(login_url=webpage)    
def search(request):
    search=request.GET.get('search')
    print(search)
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    
    items=Driverprofile.objects.filter( Q(place__icontains=q) |
                                    Q(name__icontains=q) |
                                    Q(exp__icontains=q)).order_by('-id')
    context={
        'drivers':items,
        'search':search,
    }
    return render(request,"Customer/customer-search.html",context)


@login_required(login_url=webpage)
def viewdriverprofile(request,id):
    pro=Driverprofile.objects.get(id=id)
    context={
        'profile':pro,
    }
    return render(request,"Customer/driver-profile.html",context)


@login_required(login_url=webpage)
def customerprofile(request):
    c=Customer.objects.get(user=request.user)
    pro=Customerprofile.objects.get(user=c)
    context={
        'profile':pro,
    }
    return render(request,"Customer/customer-profile.html",context)


@login_required(login_url=webpage)
def edituserprofile(request):
    c=Customer.objects.get(user=request.user)
    pro=Customerprofile.objects.get(user=c)
    if request.method=="POST":
        form=CustomerProfileForm(request.POST,request.FILES,instance=pro)
        customer=Customer.objects.get(user=request.user)
        print(customer)
        if form.is_valid():
            form.save()
            return redirect(customerprofile)
    form=CustomerProfileForm(instance=pro)
    context={
        'form':form,
    }
    return render(request,"Customer/customer-profileform.html",context)


#Driver Views

@login_required(login_url=webpage)
def driverprofile(request):
    current_user=Driver.objects.get(user=request.user)
    pro=Driverprofile.objects.get(user=current_user)
    context={
        'profile':pro,
    }
    return render(request,"Driver/driver-profile.html",context)


@login_required(login_url=webpage)
def appointment(request):
    d=Driver.objects.get(user=request.user)
    p=Driverprofile.objects.get(user=d)
    b=Bookings.objects.filter(driver=p).order_by('-id')
    context={
        'bookings':b,
    }
    return render(request,"Driver/driver-appointments.html",context)


@login_required(login_url=webpage)
def transactions(request):
    d=Driver.objects.get(user=request.user)
    p=Driverprofile.objects.get(user=d)
    pa=Payment.objects.filter(booking__driver=p.id)
    context={
        'transactions':pa,
    }
    return render(request,"Driver/driver-transactions.html",context)


@login_required(login_url=webpage)
def viewcustomerprofile(request,id):
    pro=Customerprofile.objects.get(id=id)
    context={
        'profile':pro,
    }
    return render(request,"Driver/driver-customerprofile.html",context)


@login_required(login_url=webpage)
def editdriverprofile(request):
    d=Driver.objects.get(user=request.user)
    pro=Driverprofile.objects.get(user=d)
    if request.method=="POST":
        form=DriverProfileForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(driverprofile)
    form=DriverProfileForm(instance=pro)
    context={
        'form':form,
    }
    return render(request,"Driver/driver-profileform.html",context)


