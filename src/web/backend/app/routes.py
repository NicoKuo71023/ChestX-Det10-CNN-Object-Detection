from flask import Flask, request, jsonify
from Module.model_predict import predict
import os

app = Flask(__name__)

# 設定檔案儲存路徑
UPLOAD_FOLDER = 'data/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 確保儲存資料夾存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict_route():
    # 確保有檔案傳入
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    # 取得檔案
    file = request.files['file']

    # 檢查檔案是否為空
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 儲存檔案到本地（測試用）
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    print(f"檔案已接收並儲存於: {file_path}")
    prediction = predict(file_path)
    
    print(prediction)
    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)