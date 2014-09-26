# coding: UTF-8
# Копипаста

from django.contrib import admin
from django import forms
from bicycle.admin import MetaSeoModel

from models import News


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)


def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)


class myNewsAdminForm(forms.ModelForm):

    class Meta(MetaSeoModel):
        model = News
        exclude = ()


class NewsAdmin(admin.ModelAdmin):
    form = myNewsAdminForm
    list_display = ('title', 'slug', 'published', 'custom_created',)
    actions = [make_published, make_unpublished, ]
    search_fields = ('title',)
    fieldsets = (
        (u'Основное', {'fields': ('title', 'slug', 'published', 'custom_created',
                                  'preview', 'text')}),
        (u'SEO', {'fields': ('html_title', 'html_keywords', 'html_description', 'priority')}),
    )


admin.site.register(News, NewsAdmin)
