import requests
from bs4 import BeautifulSoup

def scrape_topic(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    posts = soup.find_all("div", class_="cooked")
    return [post.get_text() for post in posts]

# Example topic
posts = scrape_topic("https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939")
for post in posts:
    print(post)
