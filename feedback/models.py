from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField
from django.forms import ModelForm

CATEGORY_CHOICES = (
    ('Suggestion/Comments', 'Suggestion/Comments'),
    ('Bug Report', 'Bug Report'),
)

SUBJECT_CHOICES = (
    ('Continuity', 'Continuity'),
    ('Blender', 'Blender'),
    ('Site', 'Site'),
)

class Feedback(models.Model):
	"""
	Table for Feedback objects.

    category: Type of feedback (Suggestion/comment or bug report)
    subject: Regarding which product (Continuity, Blender, Website)
    desc: input
	"""
	category = models.CharField(							#category name
		'Category Name',								#name of Category
		blank=False,									#required
		max_length=100,									#max length
        choices=CATEGORY_CHOICES,
		#help_text='Please select a category.'
	)

	subject = models.CharField(							#category name
		'Subject Name',								#name of Category
		blank=False,									#required
		max_length=100,									#max length
        choices=SUBJECT_CHOICES,
		#help_text='Please select a subject.'
	)

	desc = HTMLField(									#feedback
		#help_text='Please enter your feedback.'
	)

	def __str__(self):
		"""
		Represent a category by its name.
		"""
		return self.name  								#return name
