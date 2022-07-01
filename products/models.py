from operator import mod
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

# 클래스명은 대문자로 시작 + 단수형으로 하고
# META 클래스로 테이블 이름을 따로 지정해주자


class menu(models.Model):
    name = models.CharField(max_length=45)


class categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey(menu, on_delete=models.CASCADE)


class drinks(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(categories, on_delete=models.CASCADE)


class images(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey(drinks, on_delete=models.CASCADE)


class alergy(models.Model):
    name = models.CharField(max_length=45)


class alergy_drink(models.Model):
    alergy = models.ForeignKey(alergy, on_delete=models.CASCADE)
    dring = models.ForeignKey(drinks, on_delete=models.CASCADE)


class sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_oz = models.CharField(max_length=45)


class nutritions(models.Model):
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=2)
    drink = models.ForeignKey(drinks, on_delete=models.CASCADE)
    size = models.ForeignKey(sizes, on_delete=models.CASCADE)
