import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- AYARLAR ---
# BURAYA KENDİ API KEY'İNİZİ YAZIN (Tırnaklar içinde kalsın)
API_KEY = "AIzaSyC3pD1eJCSdZAHslTTukr51Kk3Zhkvb_pg"

genai.configure(api_key=API_KEY)

# --- GEMINI MODEL AYARLARI ---
def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-2.0-flash')
    # Finansal Analist Promptu
    prompt = """
    Sen deneyimli bir Borsa İstanbul teknik analistisin. Bu grafik görselini analiz et.
    Yanıtı şu formatta ve Türkçe olarak ver:
    
    1. 📊 **Trend:** (Yükseliş/Düşüş/Nötr) - Kısaca nedenini açıkla.
    2. 📉 **İndikatörler:** RSI veya Stoch RSI değerlerini oku ve yorumla (Aşırı Alım/Satım mı?).
    3. 💡 **Sinyal:** (AL / SAT / İZLE) - Neden bu kararı verdiğini belirt.
    4. 🛡️ **Seviyeler:**
       - Destek: Fiyat
       - Direnç: Fiyat
    
    Yatırım tavsiyesi değildir uyarısını en alta ekle.
    """
    response = model.generate_content([prompt, image])
    return response.text

# --- ARAYÜZ (FRONTEND) ---
st.set_page_config(page_title="AI Borsa Analisti", page_icon="📈")

st.title("📈 AI Destekli Borsa Analisti")
st.write("Grafiğin ekran görüntüsünü yükleyin, yapay zeka yorumlasın.")

uploaded_file = st.file_uploader("Bir Grafik Resmi Seçin...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Resmi ekranda göster
    image = Image.open(uploaded_file)
    st.image(image, caption='Yüklenen Grafik', use_container_width=True)
    
    # Butona basınca analiz et
    if st.button("Analiz Et 🚀"):
        with st.spinner('Yapay Zeka grafiği inceliyor...'):
            try:
                # Gemini'ye gönder
                result = get_gemini_response(image)
                
                # Sonucu göster
                st.success("Analiz Tamamlandı!")
                st.markdown("### 🤖 Analist Yorumu:")
                st.write(result)
            except Exception as e:
                st.error(f"Hata oluştu: {e}")