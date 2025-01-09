
import onnxruntime as ort
import cv2
import numpy as np


def image_preprocess(image_file):
    # 將 Flask 接收的檔案轉換為 NumPy 陣列
    file_bytes = np.frombuffer(image_file.read(), np.uint8)

    # 使用 OpenCV 解碼圖片並轉換為灰階
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    # 確認圖片是否讀取成功
    if img is None:
        raise ValueError("無法解析圖片，請檢查格式!")
    # Resize the image
    img_resized = cv2.resize(img, (128, 128))

    # Normalize pixel values
    img_resized = img_resized / 255.0

    # Convert to numpy array
    input_image = np.array(img_resized, dtype=np.float32)
    input_data = np.expand_dims(input_image, axis=0) 
    input_data = np.expand_dims(input_data, axis=0)
    return input_data

def predict(image_file):
    input_data = image_preprocess(image_file)
    columns_name = ['Atelectasis', 'Calcification', 'Consolidation', 'Effusion', 'Emphysema', 'Fibrosis', 'Fracture', 
                  'Mass', 'Nodule', 'Pneumothorax']
    # Input shape: (batch_size, channel, w, h)
    # 加載 ONNX 模型
    session = ort.InferenceSession("app/static/models/CNN_classification_model.onnx")

    # 獲取模型的輸入名稱
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

   # 執行推論
    outputs = session.run([output_name], {input_name: input_data})
    binary_output = (outputs[0][0] > 0.5).astype(int)
    # 查看結果
    predict_result = {}
    for i in range(len(columns_name)):
        predict_result[columns_name[i]]=binary_output[i]
    print("Model output:", binary_output)
    return predict_result