from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'final_date')
    list_filter = ['category']
    search_fields = ('question',)
    search_help_text = '제목 검색 가능합니다.'

@admin.register(Inquiry)
class InquiyModelAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'email', 'SMS', 'content', 'image')

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'content', 'ans_writer', 'ans_date',
    'ans_final_mod', 'ans_final_date')