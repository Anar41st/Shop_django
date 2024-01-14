from django.db import models

class Employees(models.Model):
    name = models.CharField('ФИО', max_length=30)
    numb = models.IntegerField('Номер телефона')
    post = models.CharField('Должность', max_length=30)
    salary = models.IntegerField('З\П')
    bonus = models.IntegerField('Процент премии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Models(models.Model):
    color = models.CharField('Цвет', max_length=30)
    memory = models.IntegerField('Память')
    count = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Telephone(models.Model):
    name = models.CharField('Название', max_length=20)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Clients(models.Model):
    name = models.CharField('ФИО', max_length=20)
    numb = models.IntegerField('Номер телефона')
    mail = models.CharField('Почта', max_length=50)
    color = models.CharField('Цвет', max_length=30)
    count = models.IntegerField('Количество')
    telephonemod = models.CharField('Модель', max_length=20)
    empl = models.CharField('ФИО сотрудника', max_length=30, blank=True, null=True)
    memory = models.IntegerField('Память', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
class Feedback(models.Model):
    fio = models.CharField('имя', max_length=30)
    feed = models.TextField('Отзыв')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'