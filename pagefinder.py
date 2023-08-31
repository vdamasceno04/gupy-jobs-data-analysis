import requests
from bs4 import BeautifulSoup

url = 'https://portal.gupy.io/'

def getHtml(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    #getting html
    return soup

def separateSuggestedCompanies(soup):
    companies_list = soup.find("body").find("ol") 
    # this works as long as the companies list is the first list in the website
    return companies_list

def getCompanyAddresses(companies_list):
    addresses = [] #this array will store suggested companies gupy link
    companies_attributes = companies_list.findAll('a')
    for i in companies_attributes:
        addresses.append(i.get('href'))
    return addresses

def filterAddresses(addresses): #get company's name based on its url
    names =[]
    for i in addresses:
        aux = i.replace('https://', '')
        names.append(aux.split('.gupy.io/', 1)[0])
    return names #returns suggested companies names

def findpages(url):
    soup = getHtml(url)
    companies_list = separateSuggestedCompanies(soup)
    addresses = getCompanyAddresses(companies_list)
    return(filterAddresses(addresses))