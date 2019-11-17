from django.contrib import admin
from .models import Contact, Entry

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ("post_id", "heading", "author", "published_date", "status", "category", "tags")
	list_filter = ("published_date", "author")
	search_fields = ("heading",)

admin.site.register(Contact)
admin.site.register(Entry, BlogAdmin)
