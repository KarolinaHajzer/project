from bs4 import BeautifulSoup
import bs4 as bs
import requests
import urllib.request
import sys
import re

base_url = "https://www.superpharm.pl/super-pharm/gazetki-i-foldery/promocje.html"
soup  = BeautifulSoup(requests.get(base_url).content,"lxml")

slowa = ["promocja","rabat",u"zniżka", "przecena", u"wyprzedaż", "%", "okazja"]
wyniki = {}

for item in slowa:
    result = soup.body.findAll(text=re.compile(item))
    wyniki[item] = result


orig_stdout = sys.stdout
f = open("wynik_superpharm.txt","w")
sys.stdout = f

print(wyniki)


sys.stdout = orig_stdout
f.close()
