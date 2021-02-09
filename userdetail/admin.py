from django.contrib import admin

# Register your models here.
from userdetail.models import patient


       
admin.site.register(patient)

from userdetail.models import Input
admin.site.register(Input)