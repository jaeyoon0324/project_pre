from django.core.management.base import BaseCommand
from search.crawler import crawl_and_save

class Command(BaseCommand):
    help = 'Crawl data and save to the database'

    def handle(self, *args, **kwargs):
        crawl_and_save()
        self.stdout.write(self.style.SUCCESS('Successfully crawled and saved data'))
