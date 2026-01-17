import streamlit as st

st.set_page_config(page_title="A1 Maliyet Hesapla", page_icon="🖨️")
st.title("🖨️ 3D Baskı Maliyet")
st.write("Bambu Lab A1 Combo için maliyet hesaplayıcı.")

st.subheader("🧵 Filament Bilgileri")
col1, col2 = st.columns(2)
with col1:
    fil_fiyat = st.number_input("1 KG Fiyatı (TL)", value=450.0, step=10.0)
with col2:
    harcanan = st.number_input("Harcanan (Gram)", value=50.0, step=1.0)

st.divider()

st.subheader("⚡ Enerji ve Süre")
sure = st.number_input("Baskı Süresi (Saat)", value=2.0, step=0.5)

col3, col4 = st.columns(2)
with col3:
    watt = st.number_input("Güç (Watt)", value=150.0, step=10.0)
with col4:
    elek_birim = st.number_input("Elektrik (TL/kWh)", value=2.6, step=0.1)

st.divider()

st.subheader("⚙️ Makine Yıpranması")
yazici_fiyat = st.number_input("Yazıcı Fiyatı (TL)", value=23000.0)
omur = st.number_input("Yazıcı Ömrü (Saat)", value=3000.0)

if st.button("HESAPLA", type="primary", use_container_width=True):

    m_fil = (fil_fiyat / 1000) * harcanan
    m_elek = (watt / 1000) * sure * elek_birim
    m_makine = (yazici_fiyat / omur) * sure

    toplam = m_fil + m_elek + m_makine

    # --- SONUÇ GÖSTERİMİ ---
    st.success(f"TOPLAM MALİYET: {toplam:.2f} TL")
    st.info(f"""
    **Detaylar:**
    * 🧵 Filament: {m_fil:.2f} TL
    * ⚡ Elektrik: {m_elek:.2f} TL
    * ⚙️ Makine Payı: {m_makine:.2f} TL
    """)

else:
    st.write("Sonuç için 'HESAPLA' butonuna basınız.")