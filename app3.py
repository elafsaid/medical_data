import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

# إعداد القارئ باستخدام EasyOCR
reader = easyocr.Reader(['en'], gpu=False)
# عنوان التطبيق
st.title("تطبيق قراءة النتائج الطبية")

# تحميل صورة من المستخدم
uploaded_image = st.file_uploader("قم بتحميل صورة للنتيجة الطبية", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # عرض الصورة المحملة
    image = Image.open(uploaded_image)
    st.image(image, caption="الصورة المحملة", use_column_width=True)

    # تحويل الصورة إلى numpy array للمعالجة باستخدام OpenCV
    image_np = np.array(image)

    # تشغيل EasyOCR لقراءة النص من الصورة
    with st.spinner("جاري قراءة النصوص من الصورة..."):
        results = reader.readtext(image_np)

    # عرض النتائج
    st.subheader("النتائج المقروءة من الصورة:")
    for (bbox, text, prob) in results:
        st.write(f"النص: {text} (ثقة: {prob:.2f})")
