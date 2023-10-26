from flask import Blueprint, jsonify, request
import pymysql
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

posts_bp = Blueprint('posts', __name__)

db = pymysql.connect(
    host='localhost',
    user='본인 아이디',
    password='본인 비밀번호',
    database='capstone_db'
)

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT id, title, content, createdAt FROM posts')
    posts = cursor.fetchall()
    cursor.close()
    return jsonify(posts)

@posts_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT id, title, content, createdAt FROM posts WHERE id = %s', (id))
    post = cursor.fetchone()
    cursor.close()
    if post:
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404
    

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    email = data.get('email')
    if title:
        cursor = db.cursor()
        cursor.execute('INSERT INTO posts (title, content, email) VALUES (%s, %s, %s)', (title, content, email))
        db.commit()
        cursor.close()
        return jsonify({'message': 'Post created successfully'}), 201
    else:
        return jsonify({'message': 'Title is required'}), 400


@posts_bp.route('/checkUserEmail', methods=['POST'])
def check_user_email():
    data = request.get_json()
    email = data.get('email')

    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM posts WHERE email = %s', (email))
    user_email = cursor.fetchone()
    cursor.close()
    # user_email과 current_user_email을 비교하여 권한을 확인합니다.
    if user_email:
        return jsonify({'message': '권한이 있습니다.'}), 200
    else:
        return jsonify({'message': '권한이 없습니다.'}), 401
    
@posts_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    cursor = db.cursor()

    # Delete the post
    cursor.execute('DELETE FROM posts WHERE id = %s', (id,))
    db.commit()
    cursor.close()

    # Reset AUTO_INCREMENT value and reassign IDs
    cursor = db.cursor()
    cursor.execute('ALTER TABLE posts AUTO_INCREMENT = 1')
    cursor.execute('SET @COUNT = 0')
    cursor.execute('UPDATE posts SET id = @COUNT:=@COUNT+1')
    db.commit()
    cursor.close()

    return jsonify({'message': 'Post deleted successfully'}), 200

@posts_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if title:
        cursor = db.cursor()
        cursor.execute('UPDATE posts SET title = %s, content = %s WHERE id = %s', (title, content, id))
        db.commit()
        cursor.close()
        return jsonify({'message': 'Post updated successfully'}), 200
    else:
        return jsonify({'message': 'Title is required'}), 400