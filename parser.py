# parser.py
import requests
from bs4 import BeautifulSoup

def parse_blog():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data