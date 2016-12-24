from django.conf.urls import url

from . import views

#this app should be hooked onto /tutorials
urlpatterns = [

	#home page that displays category overviews
	url(r'^$', views.index, name='index'),

]
