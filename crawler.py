import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited_links = set()

def crawl(url, domain, depth=2):
    if depth == 0 or url in visited_links:
        return []

    visited_links.add(url)
    content = []

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return []

        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        text = extract_useful_text(soup)
        if text:
            content.append(text)

        links = soup.find_all("a", href=True)
        for link in links:
            href = link['href']
            full_url = urljoin(url, href)
            parsed = urlparse(full_url)

            if parsed.netloc == domain and full_url not in visited_links:
                content.extend(crawl(full_url, domain, depth=depth - 1))

    except Exception as e:
        print(f"Error crawling {url}: {e}")

    return content

def extract_useful_text(soup):
    for tag in soup(["script", "style", "header", "footer", "nav", "noscript"]):
        tag.decompose()

    body = soup.find("body")
    if not body:
        return ""

    text_elements = body.find_all(["p", "li", "h1", "h2", "h3", "h4"])
    text = " ".join([el.get_text(strip=True) for el in text_elements if el.get_text(strip=True)])
    return text
