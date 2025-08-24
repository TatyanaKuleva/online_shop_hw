from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание продукта",
        help_text="Опишите функционал продукта",
    )
    images = models.ImageField(
        upload_to="catalog/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="загрузите изображение",
    )
    category = models.ForeignKey(
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите категория продукта",
        related_name='products'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Цена продукта",
        help_text="Укажите цену продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания продукта",
        help_text="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукы"
        ordering = ["name", "description", "updated_at"]

    def __str__(self):
        return f"{self.name} из категории {self.category} с датой  последнего обновления {self.updated_at}"


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
