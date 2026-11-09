# Ollama WordPress Auto-Publisher

Local LLM-powered autonomous technical content generator and WordPress publisher via REST API.

## Mimari
- **İçerik Üretimi:** Yerel donanımda çalışan Ollama (`qwen2.5-coder:14b`).
- **Yayınlama Katmanı:** WordPress REST API (Application Password ile Basic Auth).
- **Format:** Yapılandırılmış JSON çıktısı (Title, Slug, Meta Description, HTML Content).

## Kurulum

1. Depoyu klonlayın veya zip dosyasını açın:
```powershell
cd nasuhakay-publisher
```

2. Bağımlılıkları yükleyin:
```powershell
pip install -r requirements.txt
```

3. Çevre değişkenlerini tanımlayın:
`.env.example` dosyasını `.env` olarak kopyalayın ve WordPress bilgilerinizi girin.

## Kullanım

Varsayılan kurumsal konu ile çalıştırma:
```powershell
python main.py
```

Özel konu vererek çalıştırma:
```powershell
python main.py "Kurumsal Altyapılarda FinOps ve Bulut Maliyet Optimizasyonu"
```
