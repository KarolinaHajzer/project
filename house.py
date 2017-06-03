from bs4 import BeautifulSoup
import bs4 as bs
import requests
import urllib.request
import sys

base_url = "http://www.house.pl/pl/pl/ona/sprawdz-to/promotion-pl"
soup  = BeautifulSoup(requests.get(base_url).content,"lxml")

result = [t.text for t in soup.select("body")
          if "rabat" in t.text
          or "sale" in t.text
          or "promocja" in t.text
          or "%" in t.text
          or "zniżka" in t.text
          or "obniżka" in t.text
          ]

orig_stdout = sys.stdout
f = open("wynik_house.txt","w")
sys.stdout = f

for element in result:
    print(element)

sys.stdout = orig_stdout
f.close()