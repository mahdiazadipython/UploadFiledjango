from django.contrib import admin

from.models import Base,TutorailDjango


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    list_display = ["title",'slug']

    prepopulated_fields = {"slug":("title",)}




@admin.register(TutorailDjango)
class TutorailDjangoAdmin(admin.ModelAdmin):
    list_display = ["title","slug"]
    prepopulated_fields = {"slug":("title",)}

