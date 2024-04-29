from django.contrib import admin
from .models import *

class AboutAdmin(admin.ModelAdmin):
        list_display = ('content', 'image')
        list_display_links = ('content', 'image')





admin.site.register(About, AboutAdmin)
admin.site.register(Gallery)
admin.site.register(Video)
admin.site.register(Trening)
admin.site.register(Author)

