from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Создает стандартные группы пользователей с разрешениями'

    def handle(self, *args, **options):
        # Создаем группы
        groups_data = {
            'Модератор продуктов': [
                'add_product',
                'change_product',
                'delete_product',
                'view_product',
                'add_category',
                'change_category',
                'view_category',
            ],
            'Авторы': [
                'add_product',
                'change_product',
                'view_product',
                'view_category',
            ],
            'Пользователи': [
                'view_product',
                'view_category',
            ]
        }

        for group_name, permissions in groups_data.items():
            group, created = Group.objects.get_or_create(name=group_name)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Группа "{group_name}" создана')
                )

                for perm_codename in permissions:
                    try:
                        permission = Permission.objects.get(codename=perm_codename)
                        group.permissions.add(permission)
                    except Permission.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(f'Разрешение {perm_codename} не найдено')
                        )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Группа "{group_name}" уже существует')
                )

        self.stdout.write(
            self.style.SUCCESS('Все группы успешно созданы!')
        )



