from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    list_display = ("title")
    list_editable = ("is_active")
    search_fields = ("title")

admin.site.register(Lessons)
admin.site.register(LessonBg)
admin.site.register(HomeSlayt)
admin.site.register(HomeSmallPhoto)
admin.site.register(AboutBg)
admin.site.register(AboutText)
admin.site.register(ContactBg)
admin.site.register(ContactText)
admin.site.register(Trainers)
admin.site.register(HomeTexts)
admin.site.register(Gallery)
