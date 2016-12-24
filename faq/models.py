from django.db import models
from djangocms_text_ckeditor.fields import HTMLField

class Category(models.Model):
	"""
	Model for the categories of questions in Continuity's FAQ.
	"""
	category = models.CharField(				#name of category
		'Category Name',
		blank=False,							#name is required
		max_length=100,
		help_text='Please provide a category to group questions together.'
	)


	def __str__(self):
		"""
		Represent the category by the category name.
		"""
		return self.category 					#return name of category



class Question(models.Model):
	"""
	Model for the questions in Continuity's FAQ. The FAQ is organized by
	categories, each containing questions related to that category.
	"""
	question_text = models.CharField(			#question
		'Frequently Asked Question',
		blank=False,							#question is required
		max_length=350,
		help_text='Please provide a frequently asked question.'
	)

	answer_text = HTMLField(					#the answer to the question
		help_text='Please provide an answer to this question.'
	)	

	category = models.ForeignKey( 				#category the question is in
		Category,								#related to Category class
		on_delete=models.CASCADE, 				#deletes all questions in category
		help_text='Please categorize this question.',
		blank=False
	)


	def __str__(self):
		"""
		Represent the question by the question text
		"""
		if (len(self.question_text) > 75):
			return self.question_text[:75] + '...'
		else:
			return self.question_text
