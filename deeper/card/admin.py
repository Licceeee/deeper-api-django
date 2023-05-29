from django.contrib import admin  # NOQA
from .models import Category, Question
from django import forms
from django.db import models


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'icon_web', 'icon_mobile',
                    'is_online', 'icon_package_name_mobile',
                    'get_nr_questions')
    readonly_fields = ('created', 'updated')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['categories']
    search_fields = ['content']
    list_display = ('content', 'get_categories', 'created')
    readonly_fields = ('created', 'updated')
    list_filter = ('categories__name',)
    exclude = ('members',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }
