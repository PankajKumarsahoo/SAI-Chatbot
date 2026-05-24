import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time

BASE_URL = "https://saintellectsolutions.com/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

# ---------------------------------
# Collect All Website Links
# ---------------------------------

response = requests.get(
    BASE_URL,
    headers=headers
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

links = set()

for a in soup.find_all("a", href=True):

    href = urljoin(
        BASE_URL,
        a["href"]
    )

    if "saintellectsolutions.com" in href:

        if "mailto:" not in href:

            if "#" not in href:
                links.add(href)

print(f"\nFound {len(links)} pages\n")

# ---------------------------------
# Scrape Each Page
# ---------------------------------

pages = []

for url in sorted(links):

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = ""

        if soup.title:

            title = soup.title.text.strip()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        pages.append(
            {
                "url": url,
                "title": title,
                "content": text
            }
        )

        print(
            f"Scraped: {url}"
        )

        time.sleep(1)

    except Exception as e:

        print(
            f"Error: {url}"
        )

        print(e)

# ---------------------------------
# Save JSON
# ---------------------------------

with open(
    "data/website_data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        pages,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    f"\nSaved {len(pages)} pages to website_data.json"
)