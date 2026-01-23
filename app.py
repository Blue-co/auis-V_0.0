from flask import Flask
# 아까 만든 블루프린트를 불러옵니다.
from routes.auiss import auiss_bp
from routes.setting import setting_bp

app = Flask(__name__)

# 블루프린트 등록 (이게 핵심입니다!)
app.register_blueprint(auiss_bp)
app.register_blueprint(setting_bp)

@app.route('/')
def index():
    return "메인 페이지입니다."

if __name__ == '__main__':
    app.run(debug=True)
