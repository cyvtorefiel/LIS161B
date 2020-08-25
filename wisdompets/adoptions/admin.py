from django.contrib import admin
from .models import *

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'submission_date')
    list_filter = ('sex', 'submission_date')
    
admin.site.register(Pet, PetAdmin)
admin.site.register(Vaccine)
