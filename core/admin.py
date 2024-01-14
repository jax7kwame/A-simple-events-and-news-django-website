from django.contrib import admin
from .models import NewsPost, Event, EventComment #Category, NewsPostComment

class EventAdmin(admin.ModelAdmin):
	search_fields = ['event_title', 'description', 'hosting_church_or_group']
	list_display = ['event_title', 'hosting_church_or_group', 'created_at', 'event_date', 'event_type']
	list_filter = ['created_at', 'event_type']
	prepopulated_fields = {'slug': ('event_title',)}

'''
class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['category_title']
	list_display = ['category_title']
	list_filter = ['category_title']
	prepopulated_fields = {'category_slug': ('category_title',)}
'''

class NewsPostAdmin(admin.ModelAdmin):
	search_fields = ['title', 'author', 'intro', 'body']
	list_display = ['title', 'created_at', 'status']
	list_filter = ['author', 'created_at', 'status']
	prepopulated_fields = {'slug': ('title',)}


class EventCommentAdmin(admin.ModelAdmin):
	search_fields = ['name', 'email', 'body']
	list_display = ['name', 'email', 'created_at']
	list_filter = ['created_at']

admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventComment, EventCommentAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(NewsPostComment)