from django.contrib import admin
from .models import Stage, Answer

@admin.register(Stage)
class TextAdmin(admin.ModelAdmin):
    list_display = ['other_model','title','question']


@admin.register(Answer)
class TextAdmin(admin.ModelAdmin):
    list_display = ['stage','answer_text']