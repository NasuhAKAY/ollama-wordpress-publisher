import requests
import json
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

def generate_technical_article(topic: str) -> dict:
    """
    Yerel Ollama (qwen2.5-coder:14b) uzerinden teknik, 
    kurumsal standartlara uygun SEO makalesi ve meta verileri uretir.
    """
    system_prompt = (
        "Sen 20 yili askin tecrubeye sahip kidemli bir IT Direktoru ve Teknoloji Yoneticisisin. "
        "Kurumsal mimari, ERP/CRM entegrasyonlari, veri mimarisi ve dijital donusum konularinda uzmansin. "
        "Yanitini sadece ve sadece gecerli bir JSON objesi olarak ver. Markdown kod blogu (```json) ekleme. "
        "JSON Semasi:\n"
        "{\n"
        '  "title": "Ilgi cekici, kurumsal ve SEO uyumlu baslik",\n'
        '  "slug": "url-uyumlu-kisa-kod",\n'
        '  "excerpt": "Maksimum 160 karakterlik meta aciklama",\n'
        '  "content": "Giris, H2, H3 alt basliklari, madde imleri ve teknik degerlendirmeleri iceren HTML govdesi (h2, h3, p, ul, li etiketleri ile)"\n'
        "}"
    )

    user_prompt = f"Konu: {topic}\nLutfen kurumsal standartlarda derinlemesine bir makale hazirla."

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "format": "json",
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_ctx": 8192
        }
    }

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json=payload,
        timeout=180
    )
    response.raise_for_status()

    content_raw = response.json()["message"]["content"]
    return json.loads(content_raw)
