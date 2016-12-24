from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class FeaturedApphook(CMSApp):
	"""
	Apphook for the tutorials app.
	"""
	app_name = "featured" 							#how sys refers to apphook
	name = _("Featured Application")				#name for admin user

	#overriding get_urls does not work
	urls = ["featured.urls"]						#hooking urls to page

#register the apphook
apphook_pool.register(FeaturedApphook)