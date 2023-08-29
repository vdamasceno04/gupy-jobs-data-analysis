headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
import requests, json
from bs4 import BeautifulSoup
import re

#url = 'https://portal.gupy.io/'

url = 'https://tigre.gupy.io/'

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

print("foi")
#print(soup)
print("\n\n")

parent = soup.find("body").find("ul")
  
# finding all <li> tags
text = list(parent.descendants)
nomes =[]
titulos = parent.findAll(attrs={"aria-label": True} )
for i in titulos:
    nomes.append(["aria-label"])
#works well printing the jobs title

trabalho =[]

funcao = parent.findAll('div')
funcao_tratada = []

for i in range(len(funcao)):
    if i%4:
       funcao_tratada.append(funcao[i])
descricao =[]
for i in funcao_tratada:
    descricao.append((i.get_text()))


links =[]
prox = parent.findAll('a')
for i in prox:
    links.append(i.get('href'))

#print(links)
for i in range(len(links*4)):
    print(descricao[i]);
    if i%3: 
        print(links[i])
    print("\n")
#funcao = parent.findAll('div', class_=lambda class_list: any(class_item.startswith('sc-d868c80d-5') for class_item in class_list))
#funcao = parent.findAll('div', class_=re.compile('r\b' + 'sc-d868c80d-5'))
#for i in funcao:
#    trabalho.append([i])

#print(len(funcao))
#print(trabalho)

#funcao = parent.findAll('div', text=lambda text: 'sc-d868c80d-5' in text)
#print(nomes)
#print(text)