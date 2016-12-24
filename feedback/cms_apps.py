from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class FeedbackApphook(CMSApp):
	"""
	Apphook for the feedback app.
	"""
	app_name = "feedback" 							#how sys refers to apphook
	name = _("Feedback Application")				#name for admin user

	#overriding get_urls does not work
	urls = ["feedback.urls"]						#hooking urls to page

#register the apphook
apphook_pool.register(FeedbackApphook)
