from django.contrib import admin
from . models import *
# Register your models here.


admin.site.register(Customer)
admin.site.register(Customerprofile)
admin.site.register(Driver)
admin.site.register(Driverprofile)

admin.site.register(Bookings)
admin.site.register(Payment)
