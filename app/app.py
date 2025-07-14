import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image

model_path = '../models/brain_tumor_cnn.keras'
class_names = ['glioma', 'meningioma', 'pituitary', 'notumor']
img_size = 150

model = tf.keras.models.load_model(model_path)

st.title("🧠 Brain Tumor Detection from MRI")
st.markdown("Upload an MRI image, and the model will predict the tumor type.")

uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI", use_column_width=True)

    img_array = np.array(image)
    if img_array.shape[-1] != 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)

    img_array = cv2.resize(img_array, (img_size, img_size))
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    if st.button("Predict"):
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction) * 100

        st.success(f"🧠 Predicted: **{predicted_class.upper()}** ({confidence:.2f}% confidence)")