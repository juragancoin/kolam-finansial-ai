```python
import streamlit as st

from utils.ai_engine import ask_ai
from utils.prompts import PERBANKAN_PROMPT

st.title("🏦 Konsultasi Perbankan")

nama = st.text_input("Nama")
wa = st.text_input("WhatsApp")

pertanyaan = st.text_area(
    "Ceritakan masalah Anda"
)

if st.button("Analisis"):

    if pertanyaan:

        hasil = ask_ai(
            PERBANKAN_PROMPT,
            pertanyaan
        )

        st.success("Analisis Awal")

        st.markdown(hasil)

        st.link_button(
            "Konsultasi WhatsApp",
            "https://wa.me/6285124248400"
        )
```
