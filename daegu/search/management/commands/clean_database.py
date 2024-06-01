from django.core.management.base import BaseCommand
from daegu.data_cleaner import clean_database

class Command(BaseCommand):
    help = 'Clean the database by removing unsuitable posts'

    def handle(self, *args, **kwargs):
        clean_database()
        self.stdout.write(self.style.SUCCESS('Successfully cleaned the database'))
