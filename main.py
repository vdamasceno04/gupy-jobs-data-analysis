import webscrapping as ws
import csvhandle
import pagefinder
import analysis
import time

FILEPATH = 'data.csv'
URL = 'https://portal.gupy.io/'

def makeurl(name):
    url = 'https://' + name + '.gupy.io/'
    return url

csvhandle.initFile(FILEPATH)

visited = []

req = csvhandle.getVisited((FILEPATH))
for i in req:
    visited.append(i)

while True:
    possible_visits =[]
    to_visit = []
    possible_visits = pagefinder.findpages(URL)
    time.sleep(1)
    for j in possible_visits:
        if j not in visited:
            to_visit.append(j)
        
    for k in to_visit:
        company_url = makeurl(k)
        scrapped = ws.webscrape(company_url)
        csvhandle.addRow(scrapped, FILEPATH)
        visited.append(k)
        time.sleep(1)
    analysis.analyze(FILEPATH, 'Curitiba')

