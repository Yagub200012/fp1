from django.contrib import admin
from .models import Stage, Question, Answer

@admin.register(Stage)
class TextAdmin(admin.ModelAdmin):
    list_display = ['other_model','title']


@admin.register(Answer)
class TextAdmin(admin.ModelAdmin):
    list_display = ['question','answer_text']

@admin.register(Question)
class TextAdmin(admin.ModelAdmin):
    list_display = ['stage','question_text']