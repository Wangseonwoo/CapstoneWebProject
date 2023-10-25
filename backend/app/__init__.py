from flask import Flask
from flask_cors import CORS
import pymysql

# MySQL 데이터베이스 연결 설정
db = pymysql.connect(
    host='localhost',
    user='sunwoo',
    password='Zxcvb0860!',
    database='capstone_db'
)

def create_app():
    app = Flask(__name__)
    # CORS 설정
    CORS(app, origins=["http://localhost:5173", "http://localhost:8080"], supports_credentials=True)

    from .routes import posts_bp
    from .signup import signup_bp
    from .login import login_bp
    from .find import find_bp
    from .otp import otp_bp

    # 블루프린트 등록
    app.register_blueprint(posts_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(find_bp, url_prefix='/find')
    app.register_blueprint(otp_bp)
    
    return app
