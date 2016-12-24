from django.contrib import admin

from .models import Featured

class FeaturedAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date')

admin.site.register(Featured, FeaturedAdmin)