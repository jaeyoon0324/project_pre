import requests
from bs4 import BeautifulSoup
from django.db import connections
from django.db.models import Model, CharField, URLField

# 정제된 데이터베이스를 사용하는 모델
class CleanedPost(Model):
    title = CharField(max_length=200)
    url = URLField(max_length=200)
    image_url = URLField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_post'
        app_label = 'cleaned'

def crawl_using_cleaned_db_data():
    # 정제된 데이터베이스에서 데이터를 불러오기
    posts = CleanedPost.objects.using('cleaned').all()

    for post in posts:
        url = post.url  # URL 칼럼이 있는 경우
        print(f"Crawling data from URL: {url}")

        # URL로부터 데이터 크롤링
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # 크롤링 로직 추가
            title = soup.title.string if soup.title else 'No title'
            print(f"Title: {title}")

            # 데이터베이스에 크롤링한 데이터 저장 (예시)
            # post.crawled_title = title
            # post.save(using='cleaned')

        else:
            print(f"Failed to retrieve data from {url}")

# Django 커맨드를 통해 실행할 수 있도록 설정
if __name__ == "__main__":
    crawl_using_cleaned_db_data()
