from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import FeedbackForm
from .models import Feedback

def index(request):
	"""
	The Feedback Home page that displays a summary of categories.
	"""
	form = FeedbackForm()
	context = {
        'form': form,
    }

	return render(request, 'feedback/index.html', context)
