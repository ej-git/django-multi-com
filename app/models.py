from django.db import models
from django.utils import timezone
 
 
class Company(models.Model):
    """企業."""
 
    company_name = models.CharField('企業名', max_length=255)
    store_name = models.CharField('店舗名', max_length=255)
    thumbnail = models.ImageField('ロゴ', upload_to='images/')
    title = models.CharField('タイトルタグ', max_length=255)
    message = models.TextField('メッセージ')
    created_at = models.DateTimeField('作成日', default=timezone.now)
 
    def __str__(self):
        return self.company_name


class Book(models.Model):
    """予約."""

    date = models.DateTimeField('予約日時', default=timezone.now)
    target = models.ForeignKey(
        Company, verbose_name='企業', on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.date)
 