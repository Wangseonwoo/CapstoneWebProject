from flask import Blueprint, jsonify, request
import pymysql

login_bp = Blueprint('login', __name__)
db = pymysql.connect(
    host='localhost',
    user='본인 아이디',
    password='본인 비밀번호',
    database='capstone_db'
)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({'message': '로그인 성공'}), 200
    else:
        return jsonify({'message': '로그인 실패', 'error': '이메일 또는 비밀번호가 일치하지 않습니다.'}), 401
