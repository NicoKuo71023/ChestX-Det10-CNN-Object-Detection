const { createApp, ref } = Vue;

const app = createApp({
  setup() {
    const files = ref([]); // 儲存檔案列表
    const previewImages = ref([]); // 預覽圖片陣列

    // 處理拖曳事件
    const handleDrop = async (event) => {
      event.preventDefault(); // 阻止預設行為
      event.stopPropagation();
      // 取得拖曳檔案
      const droppedFiles = event.dataTransfer.files;

      for (let i = 0; i < droppedFiles.length; i++) {
        const file = droppedFiles[i];

        // 檢查是否為圖片
        if (file.type.startsWith('image/')) {
          files.value.push(file); // 加入檔案列表

          // 預覽圖片
          const reader = new FileReader();
          reader.onload = (e) => {
            previewImages.value.push(e.target.result); // 將圖片的 base64 加入預覽區
          };
          reader.readAsDataURL(file); // 讀取圖片數據

          // 上傳檔案
          await uploadFile(file);
        } else {
          alert('請拖曳圖片檔案！');
        }
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
        } else {
          console.log('上傳失敗！');
        }
      } catch (error) {
        console.error('錯誤:', error);
      }
    };

    return {
      files,
      previewImages, // 返回預覽圖片陣列
      handleDrop,
    };
  },
});

app.mount('#app');
