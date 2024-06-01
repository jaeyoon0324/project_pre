import requests
from bs4 import BeautifulSoup
from django.conf import settings
from search.models import Post
import django
import os

# Django 환경 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

def delete_existing_data():
    # 데이터베이스 연결
    Post.objects.all().delete()
    print("Existing data deleted.")

def crawl_and_save():
    # 기존 데이터 삭제
    delete_existing_data()

    # 첫 번째 사이트 크롤링
    url1 = "https://www.buk.daegu.kr/reserve/index.do?menu_id=00002619"
    response1 = requests.get(url1)
    webpage_content1 = response1.content

    soup1 = BeautifulSoup(webpage_content1, 'html.parser')

    go_box = soup1.find_all('span', {'class': "go_box"})

    hrefs1 = []
    for go in go_box:
        a_tag = go.find('a')
        if a_tag and 'href' in a_tag.attrs:
            hrefs1.append('https://www.buk.daegu.kr/reserve/index.do' + a_tag['href'])

    # 모든 <span> 태그 선택
    span_tags1 = soup1.find_all('span', class_='c_blue')

    # 텍스트 추출
    texts1 = [span.get_text() for span in span_tags1]

    # 데이터베이스에 저장
    for i, text in enumerate(texts1):
        post = Post.objects.create(
            title=text,
            url=hrefs1[i],
            image_url=''  # 첫 번째 사이트에서는 이미지 URL 없음
        )
        print(f'Saved: Title: {post.title}, URL: {post.url}, Image URL: {post.image_url}')

    # 두 번째 사이트 크롤링
    url2 = "http://www.tgsenior.or.kr/board/list.asp?board=notice&gubun=1"
    response2 = requests.get(url2)
    webpage_content2 = response2.content

    soup2 = BeautifulSoup(webpage_content2, 'html.parser')

    div_tags = soup2.find_all('div', {'class': "list_line01"})

    hrefs2 = []
    for div in div_tags:
        a_tag = div.find('a')
        if a_tag and 'href' in a_tag.attrs:
            hrefs2.append(a_tag['href'])

    base_url = "http://www.tgsenior.or.kr/board/"

    for href in hrefs2:
        detail_url = base_url + href
        response = requests.get(detail_url)
        webpage_content = response.content
        soup = BeautifulSoup(webpage_content, 'html.parser')
        th_tag = soup.find('th')
        title = th_tag.get_text(strip=True)

        # 클래스가 image-editor인 이미지 URL 추출
        img_tag = soup.find('img', {'class': 'image-editor'})
        if img_tag:
            image_url = img_tag['src']
            if not image_url.startswith('http'):
                image_url = base_url + image_url
        else:
            image_url = ''

        # 데이터베이스에 저장
        post = Post.objects.create(
            title=title,
            url=detail_url,
            image_url=image_url
        )
        print(f'Saved: Title: {post.title}, URL: {post.url}, Image URL: {post.image_url}')

    # 총 데이터 개수 출력
    total_posts = Post.objects.count()
    print(f'Total number of posts saved: {total_posts}')

    print('Successfully crawled and saved data from both sites.')

if __name__ == "__main__":
    crawl_and_save()
