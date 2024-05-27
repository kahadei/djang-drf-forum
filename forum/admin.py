from django.contrib import admin

# Register your models here.

from forum.models import Forum


@admin.register(Forum)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

