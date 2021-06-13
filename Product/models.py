from django.db import models

# Create your models here.

class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name="Satıcı")
    title = models.CharField(max_length= 50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    price = models.IntegerField(verbose_name="Fiyat")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title