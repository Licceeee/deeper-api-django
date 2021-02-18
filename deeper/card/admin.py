from django.contrib import admin
from .models import Category, Question


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'get_nr_questions', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ('content', 'get_categories', 'created')
    readonly_fields = ('created', 'updated')
    list_filter = ('categories__name',)