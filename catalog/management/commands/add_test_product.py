from django.core.management.base import BaseCommand, CommandError
from catalog.models import Product, Category
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = "Удаляет все существующие продукты и добавляет новые тестовые данные из фикстуры"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("все данные о продуктах удаленый"))
        call_command("loaddata", "fixtures/product_fixture.json")
        self.stdout.write(self.style.SUCCESS("Данные из фикстуры успешно загружены"))
