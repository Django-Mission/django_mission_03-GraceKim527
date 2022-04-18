from django.contrib import admin
from .models import Faq
# Register your models here.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'category', 'answer', 'writer', 'date', 
    'final_modify', 'final_date')