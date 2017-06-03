from bs4 import BeautifulSoup
import bs4 as bs
import requests
import urllib.request
import sys


#sauce = urllib.request.urlopen("http://answear.com/p/specjalne/secret-sale.html/p-1/r-60/o-n/k-4").read()

base_url = "https://www.picodi.com/pl/top"
soup  = BeautifulSoup(requests.get(base_url).content,"lxml")
#result = [t.text for t in soup.select("div", {"class":"ng-binding"}) if "rabat" or "promocja" in t.text]
result = [t.text for t in soup.select("p")
          if "rabat" in t.text
          or "sale" in t.text
          or "promocja" in t.text
          or "%" in t.text
          or "zniżka" in t.text
          or "obniżka" in t.text
          ]

#soup = bs.BeautifulSoup(sauce,"lxml")


orig_stdout = sys.stdout
f = open("wynik_picodi.txt","w")
sys.stdout = f


for element in result:
    print(element)
#result = map(lambda element: element.string, soup.find_all(lambda tag: "rabat" in tag.string if tag.string else False))
#print(result)

sys.stdout = orig_stdout
f.close()