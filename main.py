import webscrapping as ws
import csvhandle
import pagefinder
import analysis
import time
FILEPATH = 'data.csv'
URL = 'https://portal.gupy.io/'

''' THIS FILE CONTAINS THE MAIN ALGORITHM TO WEBSCRAPE GUPY WEBSITE
    AND ANALYZE EXTRACTED DATA'''

def makeurl(name): 
    #this function get the url for a certain company based on its name
    #once that gupy's url follow this pattern: https://COMPANY.gupy.io/
    url = 'https://' + name + '.gupy.io/'
    return url

csvhandle.initFile(FILEPATH) #csv file setup

visited = [] #store companies that were already webscrapped

while True:
    possible_visits =[] #store gupy suggested companies
    to_visit = [] #store companies from 'possible_visits' that weren't visited yet
    possible_visits = pagefinder.findpages(URL) 
    time.sleep(1) #these sleep functions block the execution due to rate-limiting  
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
    time.sleep(5)

