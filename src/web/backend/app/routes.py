from flask import request, jsonify, current_app
import numpy as np
from app.model import predict


    
@current_app.route('/predict', methods=['POST'])
def predict_route():
    file = request.files['file']
    # 檢查檔案是否為空
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    try:
        # 圖片預處理
        # 模型預測
        prediction = predict(file)
        
        if isinstance(prediction, dict):
            prediction = {key: int(value) for key, value in prediction.items()}
        
        # print(type(prediction["Effusion"]))
        # 回傳預測結果
        return jsonify({"prediction": prediction}), 200
        # return jsonify({'message': 'CORS is working!'})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@current_app.route('/test', methods=['GET'])
def test():
    print('test pass!!')
    return jsonify({"123": "Test"}), 200