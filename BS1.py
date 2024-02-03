from bs4 import BeautifulSoup
import requests


url = "https://jpmorgan.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.string
print("Page title:", title)

first_paragraph = soup.find('p')
if first_paragraph:
    print("First Paragraph:", first_paragraph.text)
else:
    print("No ,<p> element found on the page.")

for link in soup.find_all('a'):
    print("Hyperlink:", link.get('href'))