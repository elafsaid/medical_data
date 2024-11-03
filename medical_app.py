{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1abeaff8-a533-4ba5-9aa6-3b10e557695b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-03 15:14:11.633 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ENG.Elaf\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "def main():\n",
    "    st.title(\"Medical Result Reader\")\n",
    "    st.write(\"Upload a medical analysis image to extract text.\")\n",
    "\n",
    "    # واجهة تحميل الصورة\n",
    "    uploaded_file = st.file_uploader(\"Choose an image...\", type=[\"jpg\", \"jpeg\", \"png\"])\n",
    "    \n",
    "    if uploaded_file is not None:\n",
    "        # قراءة الصورة\n",
    "        image = load_image(uploaded_file)\n",
    "        \n",
    "        # تحويل الصورة إلى نص\n",
    "        extracted_text = read_text_from_image(image)\n",
    "        \n",
    "        # عرض النص المقروء\n",
    "        st.write(\"Extracted Text:\")\n",
    "        st.write(extracted_text)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ac35aac-89ab-42e5-826e-a0841b03eedf",
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
