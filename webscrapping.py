headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
import requests, json
from bs4 import BeautifulSoup

#url = 'https://portal.gupy.io/'

url = 'https://tigre.gupy.io/'

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

print("foi")
#print(soup)
print("\n\n")

"""print(
    soup.find("p", class_="pv-entity__secondary-title t-14 t-black t-normal")
    .find_next(text=True)
    .strip()
)"""
parent = soup.find("body").find("ul")
  
# finding all <li> tags
text = list(parent.descendants)
nomes =[]
titulos = parent.findAll(attrs={"aria-label": True} )
for i in titulos:
    nomes.append(["aria-label"])

print(nomes)
#print(text[0])