from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Person, PersonAdmin)