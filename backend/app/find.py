# app/find.py

from flask import Blueprint, jsonify, request
import pymysql
import hashlib

find_bp = Blueprint('find', __name__)

# MySQL 연결 설정
db = pymysql.connect(
    host='localhost',
    user='본인 아이디',
    password='본인 비밀번호',
    database='capstone_db'
)

# 이하 find_bp에 대한 라우트 함수들을 작성합니다.
@find_bp.route('/find-email', methods=['POST'])
def find_email():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    
    if not name or not phone:
        return jsonify({'message': 'Name and phone are required'}), 400

    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT email FROM users WHERE name = %s AND phone = %s', (name, phone))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({'email': user['email']}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@find_bp.route('/reset-password-check', methods=['POST'])
def reset_password_check():
    try:
        data = request.json
        name = data['name']
        email = data['email']

        # DB에서 해당 이름과 이메일이 일치하는지 확인하는 쿼리를 실행합니다.
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE name = %s AND email = %s", (name, email))
        result = cursor.fetchone()

        if result:
            return jsonify({'matched': True}), 200
        else:
            return jsonify({'matched': False}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

# 비밀번호를 업데이트하는 엔드포인트를 작성합니다.
@find_bp.route('/submit-reset-password', methods=['POST'])
def submit_reset_password():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        new_password = data['new_password']
        # 비밀번호를 해싱하여 업데이트하는 쿼리를 실행합니다.
        cursor = db.cursor()
        cursor.execute("UPDATE users SET password = %s WHERE name = %s AND email = %s", (new_password, name, email))
        db.commit()

        return jsonify({'message': 'Password updated successfully'}), 200

    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()