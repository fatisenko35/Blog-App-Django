from django.contrib import admin

from blog.models import BlogModel, CommentModel

# Register your models here.
admin.site.register(BlogModel)

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'blog', 'created_on', 'activate')
    list_filter = ('activate', 'created_on')
    search_fields = ( 'author',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)