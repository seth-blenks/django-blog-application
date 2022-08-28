from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.

class BlogPostImageAdminInline(admin.TabularInline):
    model = models.BlogPostImage
    readonly_fields = ("thumbnail",)

    

class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)

    list_display = ('title','description','slug','active', 'named_category', 'date_updated','image')
    list_filter = ('active','date_updated')
    search_fields = ('title',)
    inlines = (BlogPostImageAdminInline,)

    @admin.display(description='Category')
    def named_category(self, obj):
        return obj.category.name.lower()

    def image(self,obj):
        if obj.blogpostimage.thumbnail:
            return format_html('<img style="width: 50px; height: 50px;" src="%s"/>' % obj.blogpostimage.thumbnail.url )
        else:
            return '-'



class TagCategoryInline(admin.StackedInline):
    model = models.BlogPostTag

class BlogPostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogPostTagAdmin(admin.ModelAdmin):
    list_display = ('name',)








admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.User)
admin.site.register(models.BlogPostCategory, BlogPostCategoryAdmin)
admin.site.register(models.BlogPostTag, BlogPostTagAdmin)
