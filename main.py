import webscrapping as ws
import csvhandle
import pagefinder

FILEPATH = 'data.csv'
URL = 'https://portal.gupy.io/'

def makeurl(name):
    url = 'https://' + name + '.gupy.io/'
    return url

tovisit =[]
visited = csvhandle.getVisited((FILEPATH))
while True:
    tovisit = pagefinder.findpages(URL)
    for j in tovisit:
        if j not in visited:
            company_url = makeurl(j)
            scrapped = ws.webscrape(company_url)
            csvhandle.addInfo(scrapped, FILEPATH)
            visited.append(j)
            
#print(csvhandle.getVisited(FILEPATH))