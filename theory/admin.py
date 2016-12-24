from django.contrib import admin

from .models import Category, Lecture, Reading, Attachment

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('lecture', '__str__')

class ReadingAdmin(admin.ModelAdmin):
	list_display = ('category', '__str__')

class LectureAdmin(admin.ModelAdmin):
	list_display = ('category', '__str__')

admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Category)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Reading, ReadingAdmin)
