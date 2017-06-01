from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import sys


sauce = urllib.request.urlopen("https://www.picodi.com/pl/top").read()

soup = bs.BeautifulSoup(sauce,"lxml")

orig_stdout = sys.stdout
f = open("wynik.txt","w")
sys.stdout = f

for paragraph in soup.find_all("p"):
    print(paragraph.text)

#print(soup.find_all("sale"))

sys.stdout = orig_stdout
f.close()