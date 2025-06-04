import requests
from bs4 import BeautifulSoup

def fetch_info(topic: str) -> str:
    query = topic.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")

    text_snippets = [r.get_text() for r in results[:5]]
    return "\n".join(text_snippets)
