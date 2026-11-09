import sys
from ollama_client import generate_technical_article
from wp_client import WordPressClient

def main():
    topic = "Kurumsal ERP ve CRM Sistemlerinde Gercek Zamanli Veri Entegrasyonu Mimarisi"
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])

    print(f"[1/2] Yerel Ollama modeliyle icerik uretiliyor: {topic}")
    try:
        article = generate_technical_article(topic)
        print(f" -> Baslik: {article['title']}")
        print(f" -> Slug   : {article['slug']}")
    except Exception as e:
        print(f"[-] Icerik uretim hatasi: {e}")
        return

    print("[2/2] WordPress'e gonderiliyor...")
    try:
        wp = WordPressClient()
        post_data = wp.publish_post(
            title=article["title"],
            content=article["content"],
            excerpt=article.get("excerpt", ""),
            slug=article.get("slug", "")
        )
        print(f"[+] Basarili! Yazi ID: {post_data.get('id')}")
        print(f"[+] Yazi Linki: {post_data.get('link')}")
        print(f"[+] Durum: {post_data.get('status')}")
    except Exception as e:
        print(f"[-] WordPress API aktarim hatasi: {e}")

if __name__ == "__main__":
    main()
