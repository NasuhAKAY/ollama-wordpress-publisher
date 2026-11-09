import requests
import base64
from config import WP_SITE_URL, WP_USERNAME, WP_APP_PASSWORD, WP_POST_STATUS

class WordPressClient:
    def __init__(self):
        self.api_url = f"{WP_SITE_URL}/wp-json/wp/v2/posts"
        credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
        token = base64.b64encode(credentials.encode()).decode("utf-8")
        self.headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json"
        }

    def publish_post(self, title: str, content: str, excerpt: str = "", slug: str = "", status: str = None) -> dict:
        """
        WordPress'e yeni yazi gonderir.
        """
        payload = {
            "title": title,
            "content": content,
            "excerpt": excerpt,
            "slug": slug,
            "status": status or WP_POST_STATUS
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code not in [200, 201]:
            raise Exception(f"WordPress API Hatasi ({response.status_code}): {response.text}")

        return response.json()
