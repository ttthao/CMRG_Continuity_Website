from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField

class Category(models.Model):
	"""
	Table for a tutorial Category. Each category must include a name
	and description to be displayed in the Tutorial home page. 
	
	name: the name of the category
	desc: the description of the category
	icon: an image that represents the category.
	
	TODO: the icon field is currently set at #, but we should have a
	default image.
	"""
	name = models.CharField(							#category name
		'Category Name',								#name of Category
		blank=False,									#required
		max_length=100,									#max length
		help_text='Please provide a name for your category.'
	)

	desc = HTMLField(									#rich textfield
		help_text='Please describe the category.'
	)

	icon = models.ImageField(
		upload_to='tutorials', 							#uploaded to media
		blank=True,										#icon not required
		#default='#',									#TODO default icon
		help_text='Please provide an icon representing the category.',
	)

	def __str__(self):
		"""
		Represent a category by its name.
		"""
		return self.name  								#return name



class Tutorial(models.Model):
	"""
	Table for each tutorial. Each tutorial must include a name, description,
	and must also be related to one Category.

	name: name of tutorial
	desc: tutorial description, to be displayed in the Tutorial category page.
	level: the difficulty of each tutorial, expressed as a positive integer.
	category: the category that this tutorial belongs to.
	"""
	name = models.CharField(							#tutorial name
		'Tutorial Name',								#name of field
		blank=False,									#required
		max_length=100,									#max length
		help_text='Please provide a name for your tutorial.'
	)

	header = models.CharField(
		'Tutorial Header',								#name of field
		blank=True,										#optional
		max_length=200,									#max length
		help_text='Please provide a SHORT description for your tutorial.'
	)

	desc = HTMLField(									#tutorial description
		help_text='Please describe your tutorial.'
	)

	level = models.PositiveSmallIntegerField(			#difficulty of tutorial
		default=1										#1 for easiest
	)
	
	category = models.ForeignKey(				#many tutorials in one category
		Category,										#related to Category
		on_delete=models.CASCADE, 						#delete all tutorials
		blank=False,									#required field
		help_text='Please categorize your tutorial.'
	)

	author = models.CharField(
		'Author Name',
		blank=False,
		default='Anonymous',
		max_length=100,
		help_text='Please provide your name.'
	)

	def __str__(self):
		"""
		Represent a tutorial by its title.
		"""
		return self.name  								#return name



class Step(models.Model):
	"""
	Table for a step within a tutorial. Each step has a placeholderfield
	that holds the content of the step. Each step must specify its name
	and the tutorial it belongs to.

	name: the name of the step
	step: the placeholderfield
	tutorial: the tutorial it belongs to.
	"""
	name = models.CharField(
		'name',
		blank=False, 									#name is required
		help_text='Please name your step.',
		max_length=250,
	)

	step = PlaceholderField(
		'step',
	)

	tutorial = models.ForeignKey( 					#many steps in one tutorial
		Tutorial, 										#related to Tutorial
		on_delete=models.CASCADE, 						#delete all steps
		blank=False,									#required
		help_text='Please place your step in a tutorial.'
	)

	youtube = models.URLField(
		max_length=200,
		blank=True,										#optional
		help_text='OPTIONAL: Please provide the URL to EMBEDDED YouTube video (not the regular URL).'
	)

	start = models.IntegerField(
		blank=True,
		default=1,
		help_text='OPTIONAL: Please provide a start time for the video, in seconds.'
	)

	end = models.PositiveIntegerField(
		blank=True,
		default=1,
		help_text='OPTIONAL: Please provide an end time for the video, in seconds.'
	)

	def __str__(self):
		return self.name


class Feedback(models.Model):
	rating = models.PositiveSmallIntegerField(
		'Rating',
		help_text='User rating.',
		blank=False,
	)
	subject = models.CharField(
		help_text='Subject of your comment.',
		blank=False,
		max_length=100,
		default='Subject'
	)

	comment = models.TextField(
		help_text='User comments.',
		blank=False
	)

	tutorial = models.ForeignKey(
		Tutorial,
		on_delete=models.CASCADE,
		blank=False,
		help_text='Please associate your feedback with a tutorial.'
	)

	def __str__(self):
		if len(self.subject) > 75:
			return self.subject[:75] + '...'
		else:
			return self.subject
