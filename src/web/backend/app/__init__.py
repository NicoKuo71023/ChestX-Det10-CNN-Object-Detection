from flask import Flask
import os
from flask_cors import CORS

def create_app():
    # 建立 Flask 應用
    appp = Flask(__name__)
    CORS(appp)
    # 設定檔案儲存路徑
    UPLOAD_FOLDER = 'app/static/uploads/'
    appp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # 確保儲存資料夾存在
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # 使用 app_context 避免循環匯入
    with appp.app_context():
        import app.routes

    return appp