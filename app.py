{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d245640-5bba-4635-b776-0fcbd5d3b5ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a77b390a-5856-4efb-b00f-f0bcc2df33ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-03 14:35:58.701 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ENG.Elaf\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "st.title(\"Medical Diagnosis Prediction\")\n",
    "st.write(\"توقع ما إذا كانت نتيجة الاختبار تشير إلى وجود مرض بناءً على البيانات الطبية.\")\n",
    "\n",
    "# إدخال البيانات\n",
    "age = st.number_input(\"Age\", 0, 100)\n",
    "gender = st.selectbox(\"Gender\", [\"Male\", \"Female\"])\n",
    "symptom1 = st.number_input(\"Symptom 1 Score\", 0, 10)\n",
    "symptom2 = st.number_input(\"Symptom 2 Score\", 0, 10)\n",
    "\n",
    "# توقع النتيجة\n",
    "if st.button(\"Predict\"):\n",
    "    input_data = np.array([[age, gender, symptom1, symptom2]])  # يجب تحويل المدخلات الرقمية إن لزم\n",
    "    prediction = model.predict(input_data)\n",
    "    st.write(\"Prediction:\", \"Positive\" if prediction == 1 else \"Negative\")\n",
    "    st.write(f\"Model Accuracy: {accuracy:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "5641c82e-39df-42e4-9f4a-9e08a3cd28b7",
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
