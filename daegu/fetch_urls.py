import sqlite3

def get_urls_from_db(db_path):
    # 데이터베이스 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 'url' 칼럼을 모두 가져오는 SQL 쿼리
    query = 'SELECT url FROM search_post'  # search_post를 실제 테이블 이름으로 바꾸세요

    # SQL 쿼리 실행
    cursor.execute(query)

    # 결과를 가져와서 리스트에 저장
    rows = cursor.fetchall()
    urls = [row[0] for row in rows]

    # 연결 닫기
    conn.close()

    return urls

if __name__ == "__main__":
    db_path = './db.sqlite3'
    urls = get_urls_from_db(db_path)
