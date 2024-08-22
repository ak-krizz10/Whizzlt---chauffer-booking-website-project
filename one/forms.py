from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm


class Userform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'name':"username",'type':"text",'class':"input"}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'name':"password",'type':"password",'class':"input",'data-type':"password"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'name':"password",'type':"password",'class':"input",'data-type':"password"}))
    class Meta:
        model=User
        fields=['username']


class CustomerProfileForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"text"}))
    address=forms.CharField(widget=forms.Textarea(attrs={'class':"textarea--style-6",'type':"text",'placeholder':"Your address..."}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"email",'placeholder':"example@email.com"}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"text",'placeholder':"+91 "}))
    picture=forms.ImageField(required=False)
    class Meta:
        model=Customerprofile
        fields=['name','address','email','phone','picture']


class DriverProfileForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"text"}))
    dob=forms.DateField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"date"}))
    place=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"text"}))
    license=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"text",'placeholder':"eg: KL8767.."}))
    exp=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"input--style-6",'type':"number",'placeholder':"years",'min':"1"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"email",'placeholder':"example@email.com"}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-6",'type':"text",'placeholder':"+91 "}))
    availability=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':"input--style-6",'type':"checkbox"}))
    about=forms.CharField(widget=forms.Textarea(attrs={'class':"textarea--style-6",'type':"text",'placeholder':"About yourself..."}))
    picture=forms.ImageField(required=False)
    class Meta:
        model=Driverprofile
        fields=['name','dob','place','license','exp','email','phone','availability','about','picture',]
         
class BookingForm(forms.ModelForm):
    schedule=forms.DateField(widget=forms.TextInput(attrs={'type':"date"}))
    source=forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    destination=forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    class Meta:
        model=Bookings
        fields=['source','destination','schedule']
        
        
class PaymentForm(forms.ModelForm):
    amount=forms.IntegerField(widget=forms.TextInput(attrs={'type':"number",'min':"250"}))
    class Meta:
        model=Payment
        fields=['amount']