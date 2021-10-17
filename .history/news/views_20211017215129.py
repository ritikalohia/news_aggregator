from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times
ht_r = requests.get("https://www.thehindu.com/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')

ht_headings = ht_soup.find_all('h2')

ht_headings = ht_headings[0:-13] # removing footers

ht_news = []
for ht1 in ht_headings:
    ht_news.append(ht1.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news,
'ht_news': ht_news})