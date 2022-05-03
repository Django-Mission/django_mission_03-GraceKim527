# [Django Mission 03] Mission Complete✨

.gitignore을 통해 DB파일과 가상환경이 없으니 git clone을 통해 확인하실 분은 가상환경을 설치해주시고, 마이그레이션을 진행해주세요.

## Result
### Basic Mission
![Hnet-image](https://user-images.githubusercontent.com/80322308/166418861-52cdb457-1316-48ce-a8fc-5ebc1cbebb93.gif)

### Challenge Mission
![Hnet com-image](https://user-images.githubusercontent.com/80322308/166418697-fdf0775c-9295-4a73-b0c4-5f0766c0ab79.gif)

---

## Of Development
### models.py (2week include)

```python
from copyreg import constructor
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #


# BASIC MISSION 
class Faq(models.Model):
    question = models.TextField(verbose_name="질문")
    GENERAL = '일반'
    ACCOUNT = '계정'
    OTHER = '기타'
    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (OTHER, '기타'),
    ]
    category = models.CharField(max_length = 10, choices=CATEGORY_CHOICES, default = GENERAL, verbose_name="카테고리")
    answer = models.TextField(verbose_name="답변")
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="생성자", related_name='writer')
    date = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    final_modify = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name="최종 수정자", related_name='final_modify')
    final_date = models.DateTimeField(verbose_name = "최종 수정일시", auto_now = True)

# ADVANCED MISSION
class Inquiry(models.Model): #1대 1 모델
    CATEGORY_CHOICES = [
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]
    STATUS_CHOICES = [
        ('1', '문의 등록'),
        ('2', '접수 완료'),
        ('3', '답변 완료')
    ]
    category = models.CharField(max_length = 2, choices=CATEGORY_CHOICES, default = '1', verbose_name="카테고리")
    status = models.CharField(max_length = 2, choices=STATUS_CHOICES, default = '1', verbose_name="상태")
    title = models.TextField(max_length = 50, verbose_name = "제목")
    email_btn = models.BooleanField(verbose_name="이메일답변수신", default=False)
    email = models.CharField(max_length = 50, verbose_name = "이메일", null = True, blank = True)
    SMS_btn = models.BooleanField(verbose_name="문자메세지수신", default=False)
    SMS = models.CharField(max_length = 50, verbose_name = "문자메시지", null = True, blank = True)
    content = models.TextField(verbose_name = "내용")
    image = models.ImageField(verbose_name = "이미지", null = True, blank = True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="생성자", related_name='inq_writer')
    date = models.DateTimeField(verbose_name="생성일시", auto_now_add=True, null=True)
    final_modify = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name="최종 수정자", related_name='inq_modify')
    final_date = models.DateTimeField(verbose_name = "최종 수정일시", auto_now = True)
    
class Answer(models.Model): #답변 모델
    answer = models.TextField(verbose_name = "답변 내용")
    content = models.ForeignKey(to = 'Inquiry', on_delete = models.CASCADE, verbose_name = "참조 문의글")
    ans_writer = models.ForeignKey(to=User, on_delete = models.CASCADE, default = User, verbose_name = "생성자", related_name = 'ans_writer')
    ans_date = models.DateTimeField(verbose_name = "생성 일시", auto_now_add = True)
    ans_final_mod = models.ForeignKey(to=User, on_delete = models.CASCADE, null = True, blank = True, default = None, verbose_name = "최종 수정자", related_name = 'ans_final_mod')
    ans_final_date = models.DateTimeField(verbose_name = "최종 수정일시", auto_now = True)
```

### admin.py
```python
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
```
