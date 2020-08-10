from django.core.management.base import BaseCommand

from shop.models import Tag


class Command(BaseCommand):
    help = 'Add test tag'

    def add_arguments(self, parser):
        parser.add_argument('tag_name', type=str)

    def handle(self, *args, **options):
        tag_name = options.get('tag_name', None)
        if tag_name is None or tag_name == '':
            self.stdout.write(self.style.ERROR('No input tag name'))
        else:
            Tag.objects.create(name=tag_name)
            self.stdout.write(self.style.SUCCESS('Successfully create tag name'))
