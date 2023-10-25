from flask import Blueprint, jsonify, request
import pymysql

signup_bp = Blueprint('signup', __name__)
db = pymysql.connect(
    host='localhost',
    user='sunwoo',
    password='Zxcvb0860!',
    database='capstone_db'
)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    phone = data.get('phone')

    try:
        cursor = db.cursor()
        
        # Check if user with the same email, name, or phone already exists
        cursor.execute('SELECT * FROM users WHERE email = %s OR name = %s OR phone = %s', (email, name, phone))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({'message': 'User with the same email, name, or phone already exists'}), 400
        
        # If no duplicate user found, proceed with signup
        cursor.execute('INSERT INTO users (email, name, password, phone) VALUES (%s, %s, %s, %s)', (email, name, password, phone))
        db.commit()
        cursor.close()
        return jsonify({'message': 'Signup successful'}), 201
    
    except Exception as e:
        db.rollback()
        return jsonify({'message': 'Signup failed', 'error': str(e)}), 400
