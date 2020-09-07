from django.contrib import admin

# Register your models here.
from .models import Message

admin.site.site_header = "Greeting Admin"
admin.site.site_title = "Greeting Admin Area"
admin.site.index_title = "Welcome to Message Admin Area"

admin.site.register(Message)
