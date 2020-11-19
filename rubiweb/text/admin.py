from django.contrib import admin

# Register your models here.

from .models import *



from django.forms import TextInput, Textarea
from django.db import models
from django import forms



admin.site.register(Language)
admin.site.register(AppParameters)
admin.site.register(Domain)
admin.site.register(Word)
admin.site.register(Document)
admin.site.register(GenericSearch)
admin.site.register(GoogleResult)
admin.site.register(SearchResult)
admin.site.register(TmpGoogleResult)
admin.site.register(DomainList)
admin.site.register(FocusList)
admin.site.register(Status)
admin.site.register(ProjectSearch)


#class TrackInline(admin.StackedInline):
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

#class TrackInline(admin.StackedInline):
class ProjectSearchInLine(admin.TabularInline):
    model = ProjectSearch
    verbose_name_plural = "Your web sarches"
    extra = 1
    fk_name = "project"
    fields =(
        ('generic_search', 'priority'),
    )
   

#@admin.register(Track)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        ('Parameters', {'fields': ['priority', 'status', 'language']}),
    ]
    inlines = [ProjectSearchInLine]

admin.site.register(Project, ProjectAdmin)
