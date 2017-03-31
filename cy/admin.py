from django.contrib import admin
from models import CY, Category, Article, WellCome

# Register your models here.


class CYAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'spell', 'content')
    search_fields = ('name',)
    list_display_links = ('id', 'name', )
    ordering = ('id', )
    list_per_page = 30


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name', 'description')
    list_display_links = ('id', 'name',)
    ordering = ('id',)
    list_per_page = 30


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'auth', 'date_time')
    list_display_links = ('id', 'title',)
    ordering = ('id',)
    list_per_page = 30


admin.site.register(CY, CYAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(WellCome)



