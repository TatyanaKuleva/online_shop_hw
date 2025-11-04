from django.db import models
from users.models import User


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


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
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
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите категория продукта",
        related_name="products",
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

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Отметьте, если продукт должен быть виден на сайте."
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        related_name="products",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукы"
        ordering = ["name", "description", "updated_at"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]

    def __str__(self):
        return f"{self.name} из категории {self.category} с датой  последнего обновления {self.updated_at}"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True)
    phone = models.CharField(
        max_length=20, verbose_name="Телефон", blank=True, null=True
    )
    address = models.TextField(verbose_name="Адрес", blank=True, null=True)
    website = models.URLField(verbose_name="Веб-сайт", blank=True, null=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["name"]

    def __str__(self):
        return self.name
