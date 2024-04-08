import sqlite3
from werkzeug.security import generate_password_hash

# 데이터베이스 연결 name변경x
connection = sqlite3.connect('../templates/login.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

''')


# 사용자 데이터 준비
# 여기서는 예시로 'user1'이라는 아이디와 'password1'이라는 비밀번호를 사용합니다.
# 비밀번호는 해싱하여 저장해야 합니다.
username = '123'
password = '123'
hashed_password = generate_password_hash(password)

# 데이터베이스에 사용자 정보 저장
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

# 변경사항 커밋 및 데이터베이스 연결 종료
connection.commit()
connection.close()
