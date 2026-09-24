from django.contrib import admin
from Person.models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    search_fields=["username"]
admin.site.register(Person,PersonAdmin)