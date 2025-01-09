const { createApp, ref, onMounted } = Vue;

const app = createApp({
  setup() {
    const file = ref(null); // 儲存單一檔案
    const previewImage = ref(null); // 預覽單一圖片
    const prediction = ref(null); // 儲存預測結果
    const prediction_render = ref([]);
    const isTableVisible = ref(false);
    // 處理拖曳事件
    const handleDrop = async (event) => {
      event.preventDefault(); // 阻止預設行為
      event.stopPropagation();

      // 取得拖曳檔案
      const droppedFile = event.dataTransfer.files[0];

      // 檢查是否為圖片
      if (droppedFile && droppedFile.type.startsWith('image/')) {
        file.value = droppedFile; // 更新檔案

        // 預覽圖片
        const reader = new FileReader();
        reader.onload = (e) => {
          previewImage.value = e.target.result;
          localStorage.setItem('previewImage', previewImage.value);
        };
        reader.readAsDataURL(droppedFile); // 讀取圖片數據

        // 上傳檔案 (非阻塞)
        await uploadFile(droppedFile);
      } else {
        alert('請拖曳圖片檔案！');
      }
    };

    // 上傳檔案到後端
    const uploadFile = async (file) => {
      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await fetch("http://localhost:5000/predict", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          console.log('上傳成功！');
          const data = await response.json(); // 解析回應結果
          console.log('回應資料:', data);
          prediction.value = data;
          isTableVisible.value = true;
          // 將結果轉換為渲染陣列
          prediction_render.value = Object.entries(data.prediction)
            .filter(([key, value]) => value > 0) // 只保留數量大於 0 的疾病
            .map(([key, value]) => ({ disease: key, amount: value }));
        } else {
          console.log('上傳失敗！');
        }
      } catch (error) {
        console.error('錯誤:', error);
      }
    };

    return {
      file,
      previewImage,
      prediction,
      handleDrop,
      isTableVisible,
      prediction_render
    };
  },
});

app.mount('#app');
