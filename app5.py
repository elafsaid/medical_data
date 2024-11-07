{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4702491-3399-49b4-ac5b-9d1ec78b174e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-07 15:38:53.396 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.074 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ENG.Elaf\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-11-07 15:38:54.074 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.074 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.074 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.090 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.090 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-07 15:38:54.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import easyocr\n",
    "from PIL import Image\n",
    "import numpy as np\n",
    "\n",
    "# إعداد واجهة Streamlit\n",
    "st.title(\"قارئ الصور الطبية\")\n",
    "st.write(\"قم برفع صورة للنتائج الطبية لقراءتها.\")\n",
    "\n",
    "# تحميل الصورة من المستخدم\n",
    "uploaded_image = st.file_uploader(\"اختر صورة\", type=[\"jpg\", \"jpeg\", \"png\"])\n",
    "\n",
    "# التحقق من تحميل الصورة\n",
    "if uploaded_image is not None:\n",
    "    # عرض الصورة\n",
    "    image = Image.open(uploaded_image)\n",
    "    st.image(image, caption=\"الصورة الطبية\", use_column_width=True) \n",
    "    \n",
    "    # تهيئة قارئ EasyOCR\n",
    "    reader = easyocr.Reader(['en', 'ar'])  \n",
    "    \n",
    "    # تحويل الصورة إلى صيغة مناسبة لـ EasyOCR\n",
    "    image_np = np.array(image)\n",
    "\n",
    "    # استخراج النصوص من الصورة\n",
    "    with st.spinner(\"جاري تحليل الصورة...\"):\n",
    "        results = reader.readtext(image_np)\n",
    "\n",
    "    # عرض النصوص المستخرجة\n",
    "    st.write(\"النصوص المستخرجة:\")\n",
    "    for result in results:\n",
    "        st.text(result[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "83d24692-2b01-4bba-8641-6501ca57336a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
