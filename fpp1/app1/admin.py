from django.contrib import admin
from .models import Stage, Question, Answer, Subtage

@admin.register(Stage)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Subtage)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'mainstage']


@admin.register(Answer)
class TextAdmin(admin.ModelAdmin):
    list_display = ['question','answer_text']


@admin.register(Question)
class TextAdmin(admin.ModelAdmin):
    list_display = ['stage','question_text']