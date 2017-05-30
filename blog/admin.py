from django.contrib import admin
from .models import Post, Category, Image, Featured

class PostAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Featured)