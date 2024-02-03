import requests
import concurrent.futures
from bs4 import BeautifulSoup

# Function to scrape quotes from a URL
def scrape_quotes(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and print quotes from the webpage (modify this part)
            quotes = soup.find_all('span', class_='text')
            for quote in quotes:
                print(quote.text)
            print(f"Processed {url}")

        else:
            print(f"Failed to retrieve data from {url}")

    except Exception as e:
        print(f"An error occurred while processing {url}: {str(e)}")

# List of URLs to crawl (replace with your own URLs)
urls_to_crawl = [
    'http://quotes.toscrape.com/page/1/',
    'http://quotes.toscrape.com/page/2/',
    'http://quotes.toscrape.com/page/3/',
    'http://quotes.toscrape.com/page/4/',
    'http://quotes.toscrape.com/page/5/'
    # Add more URLs as needed
]

# Number of concurrent threads to use for crawling
num_threads = 4  # Adjust as needed

# Create a ThreadPoolExecutor with the specified number of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Submit crawling tasks for each URL
    futures = [executor.submit(scrape_quotes, url) for url in urls_to_crawl]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)

print("Crawling completed.")
