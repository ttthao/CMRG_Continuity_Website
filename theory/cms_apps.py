from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class TheoryApphook(CMSApp):
	"""
	Apphook for the theory app.
	"""
	app_name = "theory" 							#how sys refers to apphook
	name = _("Theory Application")				#name for admin user

	#overriding get_urls does not work
	urls = ["theory.urls"]						#hooking urls to page

#register the apphook
apphook_pool.register(TheoryApphook)
