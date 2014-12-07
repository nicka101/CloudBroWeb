from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    list_display = ('title', 'author', 'created')
    list_filter = ['created']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'author'):
            instance.author = request.user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Post, PostAdmin)
