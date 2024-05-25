from django.db import models


# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )


def __str__(self):
    return f'General Setting: {self.name}'


class Meta:
    verbose_name = 'General Setting'
    verbose_name_plural = 'General Settings'
    ordering = ('name',)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',

    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

