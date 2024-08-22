from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.webpage),
    path('logout',views.logoutall,name='logout'),
    
    #Customer urls
    path('Customer/login',views.userlogin,name='customer-login'),
    path('Customer/register',views.userregister,name='customer-register'),
    path('Customer/Completeprofile',views.completeuserprofile,name="customer-completeprofile"),
    
    path('Home',views.userhome,name="customer-home"),
    path('Search',views.search,name="customer-search"),
    path('Schedules',views.schedules,name="customer-schedule"),
    path('Transaction',views.allpayments,name="customer-transaction"),
    path('Myprofile',views.customerprofile,name="customer-myprofile"),
    path('Booking/<int:id>',views.bookdriver,name="customer-booking"),
    path('Payment/<int:id>',views.payment,name="customer-payment"),
    path('Customer/Editprofile',views.edituserprofile,name="customer-editprofile"),
    path('Driverprofile/<int:id>',views.viewdriverprofile,name="customer-driverprofile"),
    
    #Driver urls
    path('Driver/login',views.driverlogin,name='driverlogin'),
    path('Driver/register',views.driverregister,name="driverregister"),
    path('Driver/CompleteProfile',views.completedriverprofile,name="driver-completeprofile"),
    
    path('Appointments',views.appointment,name="driver-appointment"),
    path('Transactions',views.transactions,name="driver-transactions"),
    path('Profile',views.driverprofile,name="driver-profile"),
    path('Customerprofile/<int:id>',views.viewcustomerprofile,name="driver-customerprofile"), 
    path('Driver/Editprofile',views.editdriverprofile,name="driver-editprofile"),
]



urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)