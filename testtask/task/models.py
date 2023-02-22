from django.db import models

# Create your models here.
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Меню")
    description = models.TextField(max_length=255, verbose_name="Описание меню")


class MenuItem(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, related_name="children")
    menu = models.ForeignKey('Menu', on_delete=models.PROTECT)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menuitem', kwargs={'menuitem_id': self.pk})



