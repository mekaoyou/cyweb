from django.contrib import admin
from .models import CY

# Register your models here.


class CYAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'spell', 'content')
    search_fields = ('name',)
    list_display_links = ('id', 'name', )
    ordering = ('id', )
    list_per_page = 30


admin.site.register(CY, CYAdmin)



