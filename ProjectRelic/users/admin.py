from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Accounts)
admin.site.register(Address)
admin.site.register(Carts)