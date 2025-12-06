import google.generativeai as genai

# API Key'inizi buraya yapıştırın
genai.configure(api_key="AIzaSyC3pD1eJCSdZAHslTTukr51Kk3Zhkvb_pg")

print("--- Kullanılabilir Modeller ---")
for m in genai.list_models():
    # Sadece içerik üretebilen modelleri listele
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)