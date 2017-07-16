from django.contrib import admin

from .models import *

admin.site.register(Hero)
admin.site.register(Group)
admin.site.register(Diary)
admin.site.register(DiaryEntry)
