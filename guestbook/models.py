from django.db import models

# Create your models here.
from django.db import models

class Entry(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField('Сообщение', max_length=500)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f"{self.name}: {self.message[:30]}"

class student(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.IntegerField('Возраст')
    grade = models.CharField('Группа', max_length=10)
    cours = models.CharField('Курс', max_length=10)

    class Meta:
        ordering = ['name']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.name}, {self.age} лет, класс {self.grade}"
    
class group(models.Model):
    name = models.CharField('Имя группы', max_length=50)
    cours = models.CharField('Курс', max_length=10)
    quantity = models.IntegerField('Количество студентов') 

    class Meta:
        ordering = ['name']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f"{self.name}, курс {self.cours}"