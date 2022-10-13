from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=40, allow_unicode=True)
    price = models.IntegerField(verbose_name="Цена")
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.id}: {self.name}'

