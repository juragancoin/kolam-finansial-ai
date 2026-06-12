import streamlit as st

st.set_page_config(
    page_title="Kolam Finansial AI",
    page_icon="⚖️",
    layout="wide"
)

col1, col2 = st.columns([1,4])

with col1:
    st.image("assets/logo.png", width=120)

with col2:
    st.title("KOLAM FINANSIAL AI")
    st.caption("Strategi • Keamanan • Ketenangan")

st.markdown("---")

st.markdown("""
## Selamat Datang

Kolam Finansial membantu masyarakat dalam:

- Pinjaman Online (Pinjol)
- Leasing & Fidusia
- Kredit Perbankan
- Sengketa Hukum

Pilih menu di sebelah kiri untuk memulai konsultasi.
""")

st.info(
    "Pilih kategori konsultasi pada sidebar untuk mendapatkan analisis awal dari AI."
)

st.markdown("---")

st.subheader("Layanan Utama")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Pinjol", "AI Advisor")

with c2:
    st.metric("Leasing", "AI Advisor")

with c3:
    st.metric("Perbankan", "AI Advisor")

with c4:
    st.metric("Hukum", "AI Advisor")

st.markdown("---")

st.caption(
    "Kolam Finansial © 2026"
)
```
