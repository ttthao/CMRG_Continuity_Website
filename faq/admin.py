from django.contrib import admin
from .models import Question, Category 				#our FAQ classes

class QuestionInline(admin.StackedInline):
	"""
	Displays three question forms at a time.
	"""
	model = Question 								#associated model
	extra = 3										#how many at a time

class CategoryAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]		#write questions when creating categories


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', '__str__')

admin.site.register(Category, CategoryAdmin)		#edit Categories
admin.site.register(Question, QuestionAdmin)		#edit Question

