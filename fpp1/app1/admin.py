from django.contrib import admin
from .models import Stage

@admin.register(Stage)
class TextAdmin(admin.ModelAdmin):
    list_display = ['other_model','title','question','answer']
