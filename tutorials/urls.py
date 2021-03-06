from django.conf.urls import url

from . import views

#this app should be hooked onto /tutorials
urlpatterns = [
	
	#home page that displays category overviews
	url(r'^$', views.index, name='index'),

	#category page that displays a list of tutorials within a category
	url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),

	#tutorial page that includes the full list of steps
	url(r'^category/tutorial/(?P<tutorial_id>[0-9]+)/$',	views.tutorial, name='tutorial'),
]