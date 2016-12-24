from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Tutorial, Step, Feedback
from .forms import FeedbackForm

def index(request):
	"""
	The Tutorial Home page that displays a summary of categories.
	"""

	#query the existing categories
	categories = Category.objects.order_by('pk')

	#context dictionary
	context = {
		'categories': categories
	}

	return render(request, 'tutorials/index.html', context)



def category(request, category_id):
	"""
	View to display a list of tutorials within the specified category.
	"""

	#query the category and associated tutorials
	category = get_object_or_404(Category, pk=category_id)

	#query tutorials if the category exists
	tutorials = category.tutorial_set.order_by('pk')

	#context dictionary
	context = {
		'category': category,
		'tutorials': tutorials
	}

	return render(request, 'tutorials/category.html', context)



def tutorial(request, tutorial_id):
	"""
	View to display the specified tutorial, including the steps within
	the tutorial.
	"""

	#query the tutorial and related steps
	tutorial = get_object_or_404(Tutorial, pk=tutorial_id)

	#query steps if the tutorial exists
	steps = tutorial.step_set.order_by('pk')

	if request.method == 'POST':
		form = FeedbackForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = FeedbackForm(initial={'tutorial': tutorial})


	#context dictionary
	context = {
		'tutorial': tutorial,
		'steps': steps,
		'form': form
	}

	return render(request, 'tutorials/tutorial.html', context)
