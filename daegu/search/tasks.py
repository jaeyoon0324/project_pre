
from celery import shared_task
from .crawler import crawl
from .models import CrawledData

@shared_task
def crawl_and_save():
    data = crawl()
    for item in data:
        CrawledData.objects.create(title=item['title'], link=item['link'])
