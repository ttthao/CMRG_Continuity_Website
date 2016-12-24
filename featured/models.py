from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField
from datetime import date

class Featured(models.Model):
	"""
	Model for the featured app to be outputted as a jumbotron in the
	desktop-only home page and as its own separate "Featured" page.
	"""
	header = models.CharField(
		'Featured Story Header',
		blank=False,
		max_length=200,
		help_text='Please provide a header for your story.'
	)

	date = models.DateField(
		default=date.today,
		blank=False,
		help_text='Please specify when this story was written.'
	)

	image = models.ImageField(
		upload_to='featured',
		blank=False,
		help_text='Please provide an image to go with your story.'

	)

	snippet = HTMLField(
		help_text='Please provide a SHORT snippet of the story.'
	)

	details = PlaceholderField(
		'details'
	)

	def __str__(self):
		"""
		Represent the featured by the featured name.
		"""
		if (len(self.header) > 75):
			return self.header[:75] + '...'
		else:
			return self.header
