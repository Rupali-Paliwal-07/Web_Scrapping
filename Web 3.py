import requests
from bs4 import BeautifulSoup

def crawl_web(seed_url, max_pages):
    pages_visited = 0
    url_queue = [seed_url]

    while pages_visited < max_pages and url_queue:
        url = url_queue.pop(0)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                print(soup.title.string)

                links = [a['href'] for a in soup.find_all('a', href=True)]
                for link in links:
                    url_queue.append(link)

                pages_visited += 1
        except Exception as e:
            print(f"Error: {e}")

crawl_web("https://google.com", max_pages=10)
