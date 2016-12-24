from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField

class Category(models.Model):
	"""
	Table for a theory category. Each category must include a name
	and description to be displayed in the Theory home page.

	name: the name of the category
	desc: the description of the category
	icon: an image that represents the category.
	"""

	name = models.CharField(							#category name
		'Category Name',								#name of category
		blank=False,									#required
		max_length=100,									#max length
		help_text='Please provide a name for your category.'
	)

	desc = HTMLField(									#rich textfield
		help_text='Please describe the category.',
		blank=True,
	)

	icon = models.ImageField(
		upload_to='theory/', 							#uploaded to media
		blank=True,										#icon not required
		help_text='Please provide an icon representing the category.',
	)

	def __str__(self):
		"""
		Represent a category by its name.
		"""
		if (len(self.name) > 75):
			return self.name[:75] + '...'
		else:
			return self.name



class Lecture(models.Model):
	"""
	Table for each lecture. Each lecture must include a name, description,
	and must also be related to one category.

	name: name of lecture
	desc: lecture description, to be displayed in the Lecture category page.
	category: the category that this lecture belongs to.
	"""

	name = models.CharField(							#lecture name
		'Lecture Name',									#name of lecture
		blank=False,									#required
		max_length=100,									#max length
		help_text='Please provide a name for your tutorial.'
	)

	desc = HTMLField(									#lecture description
		help_text='Please describe your tutorial.',
		blank=True
	)

	category = models.ForeignKey(						#many lectures in one category
		Category,										#related to category
		on_delete=models.CASCADE, 						#delete all lectures
		blank=False,									#required field
        help_text='Please categorize your lecture.'
	)

	def __str__(self):
		"""
		Represent a lecture by its title.
		"""
		if (len(self.name) > 75):
			return self.name[:75] + '...'
		else:
			return self.name


class Reading(models.Model):
	"""
	Table for each suggested reading. Each suggested reading must include a name,
	related to one category and must also be related to one attachment.

	name: name and description of the reading
	category: the category that this reading belongs to.
	attachment: the attachment associated with this reading
	"""
	name = models.CharField(							#attachment name
		'Reading Name',									#name of reading
		blank=False,									#required
		max_length=300,									#max length
		help_text='Please provide a name for your reading.'
	)

	category = models.ForeignKey(						#many readings in one category
		Category,										#related to category
		on_delete=models.CASCADE, 						#delete all readings
		blank=False,									#required field
        help_text='Please categorize your reading to a category.'
	)

	attachment = models.FileField(
		upload_to='reading/',							#in media folder
		blank=True,										#optional field
		help_text='Please provide an attachment.'
	)

	def __str__(self):
		"""
		Represent a reading by its name.
		"""
		if (len(self.name) > 75):
			return self.name[:75] + '...'
		else:
			return self.name



class Attachment(models.Model):
	"""
	Table for each attachment. Each attachment must include a name, file,
	and must also be related to one lecture.

	name: name of attachment, or filetype, depending on context
	desc: description of attachment
	attachment: actual attachment
	lecture: lecture that this attachment is associated with
	"""

	name = models.CharField(							#attachment name
		'Attachment Name',								#name of attachment
		blank=False,									#required
		max_length=100,									#max length
		help_text='Please provide a name for your attachment.'
	)

	desc = HTMLField(									#tutorial description
		help_text='Please describe your attachment.',
		blank=True
	)

	attachment = models.FileField(
		upload_to='lectures/',							#in media folder
		blank=True,										#optional field
		help_text='Please provide an attachment.'
	)

	lecture = models.ForeignKey(
		Lecture,
		blank=False,
		on_delete=models.CASCADE,
		help_text='Please indicate which lecture this attachment is for.'
	)

	def __str__(self):
		"""
		Represent an attachment by its title.
		"""
		if (len(self.name) > 75):
			return self.name[:75] + '...'
		else:
			return self.name