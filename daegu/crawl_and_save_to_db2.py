import requests
from bs4 import BeautifulSoup
import django
import os

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daegu.settings')
django.setup()

from search.models import Post, CrawledData

def get_urls_from_db():
    # 기존 데이터베이스에서 URL 가져오기
    return list(Post.objects.values_list('url', flat=True))

def save_to_new_db(title, url, content):
    # 새로운 데이터베이스에 저장
    CrawledData.objects.using('db2').create(
        title=title,
        url=url,
        content=content
    )

def crawl_buk_daegu(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 제목 추출 (필요에 따라 CSS 선택자 수정)
    title_tag = soup.find('title')  # 예: <title> 태그
    title = title_tag.get_text(strip=True) if title_tag else 'No title'

    # 본문 내용 추출 (필요에 따라 CSS 선택자 수정)
    content_tag = soup.find('div', class_='content')  # 예: <div class="content"> 태그
    content = content_tag.get_text(strip=True) if content_tag else 'No content'

    return title, content

def crawl_tgsenior(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 제목 추출 (필요에 따라 CSS 선택자 수정)
    th_tag = soup.find('th')
    title = th_tag.get_text(strip=True) if th_tag else 'No title'

    # 본문 내용 추출 (필요에 따라 CSS 선택자 수정)
    content_tag = soup.find('div', class_='content')  # 예: <div class="content"> 태그
    content = content_tag.get_text(strip=True) if content_tag else 'No content'

    return title, content

def crawl_and_save(urls):
    for url in urls:
        if 'https://www.buk.daegu.kr/' in url:
            title, content = crawl_buk_daegu(url)
        elif 'http://www.tgsenior.or.kr/' in url:
            title, content = crawl_tgsenior(url)
        else:
            print(f"Skipping URL: {url}")
            continue

        # 데이터베이스에 저장
        save_to_new_db(title, url, content)
        print(f'Saved: Title: {title}, URL: {url}')

if __name__ == "__main__":
    # 기존 데이터베이스에서 URL 가져오기
    urls = get_urls_from_db()

    # URL을 크롤링하여 데이터를 새로운 데이터베이스에 저장
    crawl_and_save(urls)

    print("Crawling and data saving to db2.sqlite3 completed.")
