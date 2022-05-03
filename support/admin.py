from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    min_num = 1
    verbose_name = '답변'
    verbose_name_plural = '답변'

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'final_date')
    list_filter = ['category']
    search_fields = ('question',)
    search_help_text = '제목 검색 가능합니다.'

@admin.register(Inquiry)
class InquiyModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'writer')
    #writer은 FK로 가져온거기 때문에 유저모델에 있는 username을 가져와야함
    search_fields = ('title', 'writer__username', 'SMS', 'email') 
    list_filter = ['category', 'status']
    inlines = [AnswerInline]

    actions = ['make_published']
    
    @admin.action(description='답변 완료 문의 안내 발송')
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            if item.email_btn == True: #이메일 수신 버튼이 true일때만
                print(item.email)
            if item.SMS_btn == True: #문자 수신 버튼이 true일때만
                print(item.SMS)
        

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'content', 'ans_writer', 'ans_date',
    'ans_final_mod', 'ans_final_date')