from django.contrib import admin
from .models import Adventure, DiaryEntry

# Register your models here.

admin.site.register(Adventure)
admin.site.register(DiaryEntry)