from django.core.management import BaseCommand

from products.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'vegetables'},
            {'name': 'berries'},
            {'name': 'fruits'}
        ]
        Category.objects.all().delete()
        category_list_create = []
        for category_item in category_list:
            category_list_create.append(Category(**category_item))

        Category.objects.bulk_create(category_list_create)