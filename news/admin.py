from django.contrib import admin
from .models import NewsArticle, User
# Register your models here.

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'source')

class UserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'browser', 'os', 'device', 'date', 'token')

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(User, UserAdmin)