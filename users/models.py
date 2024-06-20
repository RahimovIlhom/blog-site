from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


GENDERS = (
    ('male', 'Erkak'),
    ('female', 'Ayol'),
)


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDERS, verbose_name="Jinsi")

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def get_absolute_url(self):
        return reverse('home')
