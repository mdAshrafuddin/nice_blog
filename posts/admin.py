from django.contrib import admin
from .models import Post, Category, Author, Comment, PostView

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'author')
    # fields = ('title', 'content', 'author', 'image')
    #  date_hierarchy = 'content'
    search_fields = ('title', 'content')
    list_filter = ('title', )
    list_per_page = 1
    ordering = ['-title']
    # autocomplete_fields = ['title']
    # fieldsets = (
    #     ('Section 1', {
    #         'fields': ('title',),
    #         'classes': ('wide', 'extrapretty'),
    #     }),
    #     ('Section 2', {
    #         'fields': ('content', ),
    #         'classes': ('wide', 'extrapretty'),
    #     }),
    # )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')
    search_fields = ('user', 'content')
    list_per_page = 5
    list_filter = ('content', )
    # fields = ('user', )

# admin.site.register(Category)
# admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # fields = ('name', )
    list_display = ('id', 'name', 'create_on')
    search_fields = ('name', )
    list_per_page = 5
    # date_hierarchy = 'create_on'
    empty_value_display = '-empty-'
    exclude = ('name',)
# admin.site.register(Category, CategoryAdmin)

@admin.register(Comment)
class CommentyAdmin(admin.ModelAdmin):
    # fields = ('name', )
    # list_display = ('content', 'timestamp', 'user')
    search_fields = ('name', )
    list_per_page = 5
    # date_hierarchy = 'create_on'

admin.site.register(PostView)