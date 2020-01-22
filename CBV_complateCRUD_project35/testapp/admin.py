from django.contrib import admin
from testapp.models import Beer

class BeerAdmin(admin.ModelAdmin):
    list_display = ['name','taste','color','price','date']

admin.site.register(Beer,BeerAdmin)

