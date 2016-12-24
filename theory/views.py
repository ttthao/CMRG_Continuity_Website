from django.shortcuts import render

from .models import Category


def index(request):
	"""
	The Theory Home page that displays a list of lectures.
	"""

	#query the existing categories
	categories = Category.objects.all()

	#context dictionary
	context = {
		'categories': categories,
	}

	return render(request, 'theory/index.html', context)
