import requests
from bs4 import BeautifulSoup

#THIS FILE CONTAINS FUNCTIONS USED TO WEBSCRAPE A COMPANY'S JOBS OPENINGS, LOCATIONS, TYPES, AND URL TO APPLY

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
    #this array will store 3 strings containing info from each announce: JOB NAME, LOCATION, JOB TYPE 
    for i in range(len(joblistdivs)):
        if i%4: #removes job announcement 
            filtered_info.append(joblistdivs[i].get_text())
    return filtered_info

def getApplyAddress(url, joblist):
    addresses =[]
    #this array will store the job candidature address
    jobsatributes = joblist.findAll('a')
    for i in jobsatributes:
        addresses.append(url+i.get('href'))
    return addresses

def joinDataArrays(url, filtered_info, addresses):
    finaldata =[]
    url = url.replace('https://', '')
    companyName = url.split('.gupy.io/', 1)[0] #get company's name from URL
    iter_address = iter(filtered_info)
    for i in range(len(addresses)):
        finaldata.append(companyName)
        for j in range(0,3):
            finaldata.append((next(iter_address)))
        finaldata.append((addresses[i]))
    return finaldata

def webscrape(url):
    soup = getHtml(url)
    joblist = separateJobList(soup)
    filtered_info = getJobInfo(joblist)
    addresses = getApplyAddress(url, joblist)
    return(joinDataArrays(url, filtered_info, addresses))
