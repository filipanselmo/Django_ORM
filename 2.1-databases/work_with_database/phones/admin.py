from django.contrib import admin
from phones.models import Phone


#@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, PhoneAdmin)
# Register your models here.
