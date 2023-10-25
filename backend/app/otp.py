from flask import Blueprint, jsonify
import pyotp

otp_bp = Blueprint('ot', __name__)

# 사용할 시크릿 키를 설정합니다. 이 부분을 실제로 안전한 값으로 대체해야 합니다.
SECRET_KEY = pyotp.random_base32(length=32)

@otp_bp.route('/generate-otp', methods=['POST'])
def generate_otp():
    totp = pyotp.TOTP(SECRET_KEY, digits=4)  # 4자리 OTP 생성
    otp = totp.now()
    return jsonify({"otp": otp})