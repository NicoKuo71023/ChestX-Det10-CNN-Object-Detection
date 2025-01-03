from flask import request, jsonify, current_app

from app.model import predict
import os

@current_app.route('/predict', methods=['POST'])
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
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    print(f"檔案已接收並儲存於: {file_path}")
    prediction = predict(file_path)
    
    print(prediction)
    return jsonify({"prediction": prediction})


