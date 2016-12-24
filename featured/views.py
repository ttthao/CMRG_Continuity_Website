from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Featured 

def index(request):
	"""
	Homepage containing an overview of all the featured stories.
	"""
	featured = Featured.objects.all()
	paginator = Paginator(featured, 2)
	page_range = paginator.page_range

	page = request.GET.get('page')

	try:
		stories = paginator.page(page)
	except PageNotAnInteger:
		stories = paginator.page(1)
	except EmptyPage:
		stories = paginator.page(paginator.num_pages)

	context = {
		'stories': stories,
		'page_range': page_range
	}

	return render(request, 'featured/home.html', context)

def story(request, story_id):
	"""
	Detailed view of a specific story.
	"""
	story = get_object_or_404(Featured, pk=story_id)

	context = {
		'story': story
	}

	return render(request, 'featured/detail.html', context)