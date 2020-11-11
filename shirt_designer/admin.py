from django.contrib import admin
from .models import Collar, CollarType
# Register your models here.
admin.site.register(CollarType)

admin.site.register(Collar)