from django.conf.urls import url

from . import views

#this app should be hooked onto /tutorials
urlpatterns = [
	
	#home page that displays an overview of the featured pages
	url(r'^$', views.index, name='index'),

	#detailed view of individual stories
	url(r'^story/(?P<story_id>[0-9]+)/$', views.story, name='story'),

]