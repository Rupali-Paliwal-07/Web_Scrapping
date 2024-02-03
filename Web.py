import requests

# URL of the website you want to request
url = "https://www.google.com"

#Send a HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful(status code 200)
if response.status_code == 200:

         # print the content of teh response (HTML content of teh Google)
        print(response.text)
else:
        print(f"Failed to retrieve content.Status code: {response.status_code}")

