# ChestX-Det10-CNN-Object-Detection

This project focuses on classifying chest X-ray images using a basic Convolutional Neural Network (CNN). The goal is to perform a two-stage classification:
1. **Binary Classification**: Detect whether an image contains a disease.
2. **Multi-class Classification**: Identify specific diseases present in the image.

## Project Overview

Chest X-rays are commonly used for detecting chest-related abnormalities. This project simplifies the problem into two steps:
1. **Binary Classification**: Separate images into two categories: `Normal` and `Disease Present`.
2. **Disease Classification**: Further classify the diseased images into specific disease categories, such as `Fibrosis`, `Mass`, or `Nodule`.

---

## Dataset

### **Source**
https://www.kaggle.com/datasets/ztamnaja/chestxdet10dataset/data

### **Preprocessing**
- Images are resized to 224x224 pixels for consistency.
- Pixel values are normalized to the range `[0, 1]`.

---

## Model Architecture

### **Binary Classification**
A basic CNN is used for binary classification to determine if an image contains a disease or not:
- **Input**: A grayscale chest X-ray image of size 224x224.
- **Output**: A binary label (`0`: Normal, `1`: Disease Present).

#### **Architecture**
- Two convolutional layers with ReLU activation and MaxPooling.
- Fully connected layers with a Sigmoid output for binary classification.

### **Multi-class Classification**
Another CNN is used to classify diseased images into specific disease categories:
- **Input**: A grayscale chest X-ray image of size 224x224.
- **Output**: Multi-class labels representing disease categories (or multi-label for cases with multiple diseases).

#### **Architecture**
- Similar to binary classification, but the output layer uses a `Softmax` (for single-label) or `Sigmoid` (for multi-label) activation.

---

## Installation and Setup

### **Dependencies**
- Python 3.7+
- PyTorch
- torchvision
- matplotlib
- numpy
- PIL

Install the required dependencies using pip:
```bash
pip install torch torchvision matplotlib numpy pillow
