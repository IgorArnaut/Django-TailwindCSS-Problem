from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Building, Item, Apartment, Terms, Listing])
