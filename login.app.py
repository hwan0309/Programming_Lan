# app.py
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__, template_folder='./templates')

# 루트 URL에 대한 라우트 추가
@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/login.html')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()

    # 데이터베이스에서 사용자 검색
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    connection.close()

    if user:
        return redirect(url_for('success'))
    else:
        # 로그인 실패 시 다시 로그인 페이지로 리디렉션
        return redirect(url_for('index'))


@app.route('/chart')
def success():
    #https://stackoverflow.com/참조
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)



