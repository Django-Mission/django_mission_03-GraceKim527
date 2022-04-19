from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'category', 'answer', 'writer', 'date', 
    'final_modify', 'final_date')

@admin.register(Inquiry)
class InquiyModelAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'email', 'SMS', 'content', 'image')

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'content', 'ans_writer', 'ans_date',
    'ans_final_mod', 'ans_final_date')