from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'Обёртка'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='порядок отображения',
        )
    wrapper = models.OneToOneField(
        Wrapper,
        verbose_name='Обёртка',
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping,
                                      verbose_name='Топпинги')
    is_on_main = models.BooleanField('На главной', default=False)
    output_order = models.PositiveSmallIntegerField(default=100)

    class Meta:
        ordering = ('output_order', 'title')
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title
