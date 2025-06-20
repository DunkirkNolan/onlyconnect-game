from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'group', 'solution_name')
    list_filter = ('group',)
    search_fields = ('text', 'solution_name')