import requests, json
from bs4 import BeautifulSoup

#url = 'https://portal.gupy.io/'

url = 'https://tigre.gupy.io/'

def getHtml(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    #getting html
    return soup

def separateJobList(soup):
    joblist = soup.find("body").find("ul") 
    # this works as long as the job lists is the first list in the website
    return joblist

def getJobInfo(joblist):
    joblistdivs = joblist.findAll('div') 
    #gets divs containing job info
    filtered_info = []
    #this array will store 3 strings containing info from each announce: JOB NAME, WORKPLACE, JOB TYPE 
    for i in range(len(joblistdivs)):
        if i%4: #removes job announcement 
            filtered_info.append(joblistdivs[i].get_text())
    return filtered_info

def getApplyAddress(joblist):
    addresses =[]
    #this array will store the job candidature address
    jobsatributes = joblist.findAll('a')
    for i in jobsatributes:
        addresses.append(url+i.get('href'))
    return addresses

def joinDataArrays(filtered_info, addresses):
    finaldata =[]
    iter_address = iter(filtered_info)
    for i in range(len(addresses)):
        for j in range(0,3):
            finaldata.append((next(iter_address)))
        finaldata.append((addresses[i]))
    return finaldata
    
a = getHtml('https://tigre.gupy.io/')
b = separateJobList(a)
c = getJobInfo(b)
d = getApplyAddress(b)
e = joinDataArrays(c, d)