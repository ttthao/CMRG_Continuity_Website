from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Featured                      #Featured classes

class FeaturedPlugin(CMSPluginBase):
    model = CMSPlugin                       #holds plugin instance info
    render_template = "featured/index.html"          #template
    cache = False
    name = 'Featured'                            #name of our plugin

    def render(self, context, instance, placeholder):
        """
    	Returns the context to be used to render the template
    	specified in render_template.

    	Param:	context: the context with which the page is rendered
    			instance: the instance of your plugin that is rendered
    			placeholder: the name of the placeholder that is rendered
    	"""

        #query all the categories
        featured = Featured.objects.all().order_by('-date')[:5]

        #pass the categories into the context
        context.update({'featured': featured})

        #return the context to update
        return context

plugin_pool.register_plugin(FeaturedPlugin)  #register our FAQ plugin
