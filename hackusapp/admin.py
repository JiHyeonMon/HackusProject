from django.contrib import admin

from .models import Challenge, Writeup, Success
# Register your models here.
admin.site.register(Challenge)
admin.site.register(Writeup)
admin.site.register(Success)