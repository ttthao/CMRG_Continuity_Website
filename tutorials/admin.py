from django.contrib import admin

from .models import Category, Tutorial, Step, Feedback

class StepInline(admin.TabularInline):
	"""
	Create and display three steps at a time.
	"""
	model = Step
	extra = 1

class TutorialAdmin(admin.ModelAdmin):
	"""
	Displays steps on the same page as tutorials.
	"""
	fieldsets = [
		(None, {'fields': ['name']}),
		('Tutorial Information', {'fields': ['header',
											'desc', 'level',
											'category', 'author'],
									'classes': ['collapse', 'wide']}),
	]

	inlines = [StepInline]

class StepAdmin(admin.ModelAdmin):
	list_display = ('tutorial', 'name')

class FeedbackAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields': []})
	]

#register all three models
admin.site.register(Category)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Feedback)
