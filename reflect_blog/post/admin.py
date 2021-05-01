from django.contrib import admin
from .models import Post, Category, Author
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Author)

admin.site.site_header = "Reflect Blog"
admin.site.site_title = "Reflect Blog"
admin.site.index_title = "Dashboard"
