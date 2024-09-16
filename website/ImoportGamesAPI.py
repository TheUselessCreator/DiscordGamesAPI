import random
import requests
from bs4 import BeautifulSoup

# URL of the hosted websiteapi.txt file
txt_file_url = 'https://yourwebsite.com/websiteapi.txt'

def fetch_links_from_txt():
    # Fetch the content of the websiteapi.txt file
    response = requests.get(txt_file_url)
    if response.status_code != 200:
        return []

    # Split the file content by lines and strip out any extra whitespace
    links = [link.strip() for link in response.text.splitlines() if link.strip()]
    return links

def fetch_random_link():
    # Get all links from the websiteapi.txt file
    links = fetch_links_from_txt()
    if not links:
        return "No links available."

    # Randomly select one link from the list
    page_url = random.choice(links)

    # Fetch the selected page's content
    response = requests.get(page_url)
    if response.status_code != 200:
        return f"Failed to retrieve page: {page_url}"

    # Parse the page and extract the first link (or modify this based on your use case)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find('a')['href'] if soup.find('a') else "No link found on the page."

    return link

# Example usage
if __name__ == "__main__":
    random_link = fetch_random_link()
    print(f"Random Link: {random_link}")
