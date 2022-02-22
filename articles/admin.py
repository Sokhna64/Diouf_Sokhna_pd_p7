from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Description


admin.site.register(Description)
# admin.site.register(Article)

# Apply summernote to all TextField in model.


class ArticleAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('contenu')


admin.site.register(Article, ArticleAdmin)
