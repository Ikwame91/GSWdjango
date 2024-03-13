from django.contrib import admin
from .models import Memeber
# Register your models here.

class MemeberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'joined_date')

admin.site.register(Memeber, MemeberAdmin)
