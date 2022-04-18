from copyreg import constructor
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #

# Create your models here.
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
    final_date = models.DateTimeField(verbose_name="최종 수정일시", auto_now=True)
