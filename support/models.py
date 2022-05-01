from copyreg import constructor
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #

# Create your models here.

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
    title = models.TextField(max_length = 50, verbose_name = "제목")
    email_btn = models.BooleanField(verbose_name="이메일답변수신", default=False)
    email = models.CharField(max_length = 50, verbose_name = "이메일", null = True, blank = True)
    SMS_btn = models.BooleanField(verbose_name="문자메세지수신", default=False)
    SMS = models.CharField(max_length = 50, verbose_name = "문자메시지", null = True, blank = True)
    content = models.TextField(verbose_name = "내용")
    image = models.ImageField(verbose_name = "이미지", null = True, blank = True)
    
class Answer(models.Model): #답변 모델
    answer = models.TextField(verbose_name = "답변 내용")
    content = models.ForeignKey(to = 'Inquiry', on_delete = models.CASCADE, verbose_name = "참조 문의글")
    ans_writer = models.ForeignKey(to=User, on_delete = models.CASCADE, default = User, verbose_name = "생성자", related_name = 'ans_writer')
    ans_date = models.DateTimeField(verbose_name = "생성 일시", auto_now_add = True)
    ans_final_mod = models.ForeignKey(to = User, on_delete = models.CASCADE, null = True, blank = True, default = None, verbose_name = "최종 수정자", related_name = 'ans_final_mod')
    ans_final_date = models.DateTimeField(verbose_name = "최종 수정일시", auto_now = True)