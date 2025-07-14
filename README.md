# 🧠 Brain Tumor Detection from MRI using Deep Learning

A production-ready web application built using **TensorFlow** and **Streamlit** that detects brain tumors (Glioma, Meningioma, Pituitary, or No Tumor) from MRI images and highlights the region of interest using **Grad-CAM** visualizations.

> 📌 This project demonstrates real-world deployment of deep learning in healthcare diagnostics.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-username.streamlit.app)

---

## 📂 Project Structure

```
Brain_Tumor_Detection/
🔺 app/
🔽   └── app.py                 # Streamlit frontend + Grad-CAM
🔺 models/
🔽   └── brain_tumor_cnn.keras  # Pre-trained CNN model
🔽 requirements.txt           # Dependencies for deployment
🔽 README.md                  # This file
```

---

## 🧠 Model Overview

* Built a custom **Convolutional Neural Network (CNN)** to classify MRI images.
* Trained on a labeled dataset of brain MRIs across 4 classes:

  * `glioma`
  * `meningioma`
  * `pituitary`
  * `no tumor`
* Added **Grad-CAM** visualizations to interpret model predictions.

---

## 📊 Dataset

* Source: [Kaggle - Brain Tumor Classification (MRI)](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
* Contains separate `Training` and `Testing` folders with MRI scans.
* Total size: \~3000+ images across 4 tumor classes.

---

## 💻 Technologies Used

* `Python`
* `TensorFlow` / `Keras`
* `OpenCV`
* `Streamlit`
* `PIL` (Image handling)
* `Matplotlib` (for Grad-CAM heatmap)

---

## 🖼️ Grad-CAM Visualization

This app includes a built-in Grad-CAM implementation to highlight the region of the brain image the model is focusing on.

<p align="center">
  <img src="https://your-app-link/gradcam-screenshot.png" width="500"/>
</p>

---

## 📦 Installation & Usage (Local)

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/brain-tumor-detection.git
   cd brain-tumor-detection
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app/app.py
   ```

---

## 🌐 Deployment

This project is deployed using [Streamlit Cloud](https://streamlit.io/cloud) with a public URL. The app loads a saved `.keras` model and performs predictions instantly in the browser.

---

## 📊 Future Enhancements

* 🔁 Add backend storage (Firebase or Supabase) for uploading patient scans
* 🧠 Auto-retrain model using new data for continuous learning
* 📱 Mobile version using TensorFlow Lite
* 🧪 Add evaluation dashboard with confusion matrix, metrics, etc.

---

## 👨‍💻 Author

* **Harisharan Mishra**
  * [LinkedIn](https://www.linkedin.com/in/harisharna-mishra-a3899b246/)
