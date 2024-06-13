from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.utils.text import slugify

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        ordering = ['-id']
        verbose_name = 'Bo\'lim'
        verbose_name_plural = 'Bo\'limlar'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        ordering = ['-id']
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'


class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Aftor")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    body = models.TextField(verbose_name="Matni")
    photo = models.ImageField(upload_to='blogs/images/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])
    ], verbose_name="Rasmi")
    video = models.FileField(upload_to='blogs/videos/', null=True, blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
                             verbose_name="Videosi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Bo'limi")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Teglar")
    slug = models.SlugField(max_length=50, verbose_name="Manzil")
    created_time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.author}: {self.title}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Blog, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])


    class Meta:
        db_table = 'blogs'
        ordering = ['-created_time']
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.blog.title}"

    class Meta:
        db_table = 'comments'
        ordering = ['-created_time']
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class Like(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.blog.title}"

    class Meta:
        db_table = 'likes'
        ordering = ['-created_time']
        verbose_name = 'Layk'
        verbose_name_plural = 'Layklar'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_time']
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'
