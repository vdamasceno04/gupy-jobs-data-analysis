import csvhandle
import numpy as np

#THIS FILE CONTAINS FUNCTIONS TO ANALYZE DATA FROM THE CSV FILE

def analyze(filepath, city):
    howManyJobs(filepath)
    setHowManyCompanies(filepath)
    setJobsPerCompany(filepath)
    setJobsInACity(filepath, city)

def howManyJobs(filepath): #count how many jobs there are based on the csv column's size
    n = csvhandle.getColumnSize(filepath)
    auxvec =[n]
    for i in range(n-1):
        auxvec.append('')
    csvhandle.addColumn('Total jobs', auxvec, filepath)

def setHowManyCompanies(filepath): #create a new column containing the number of companies
    n = getHowManyCompanies(filepath)
    arraysize = csvhandle.getColumnSize(filepath)
    auxvec =[n]
    for i in range(arraysize-1):
        auxvec.append('')
    csvhandle.addColumn('Total companies', auxvec, filepath)

def getHowManyCompanies(filepath): #count how many companies exist in the csv file
    companies_names = csvhandle.getVisited(filepath)
    n = len(companies_names)
    return n

def getJobsPerCompany(filepath): #calculate mean and standard deviation 
    companies = getHowManyCompanies(filepath)
    jobs = csvhandle.getColumnSize(filepath) 
    frequency = companyFrequency(filepath)
    mean = jobs/companies
    stddev = np.std(frequency)
    result = str(int(mean)) + ' +/- ' + str(int(stddev))
    return result

def setJobsPerCompany(filepath): #create a new column containing jobs/company standard deviation value
    n = getJobsPerCompany(filepath)
    arraysize = csvhandle.getColumnSize(filepath)
    auxvec =[n]
    for i in range(arraysize-1):
        auxvec.append('')
    csvhandle.addColumn('Jobs per company', auxvec, filepath)

def companyFrequency(filepath): #get how many jobs of each company there is in the data file
    names = csvhandle.getVisited(filepath)
    frequency = [] #each key is the number of jobs offered by each company 
    allJobs = csvhandle.getCompanies(filepath)
    for i in names:
        frequency.append(allJobs.count(i)) 
    return frequency
    
def getJobsInACity(filepath, city): #count how many jobs are offered in a certain city
    locations = csvhandle.getLocation(filepath)
    handled = city.replace(" " , "").lower() #avoid mismatches due to spaces of uppercases
    k = 0
    for i in locations:
        aux = str(i).replace(" ", "").lower()
        if not aux.find(handled) == -1:
            k += 1
    return k

def setJobsInACity(filepath, city): #create a new column with the number of jobs offered in a specified city
    n = getJobsInACity(filepath, city)
    arraysize = csvhandle.getColumnSize(filepath)
    auxvec =[n]
    column_name = 'Jobs in ' + str(city)
    for i in range(arraysize-1):
        auxvec.append('')
    csvhandle.addColumn(column_name, auxvec, filepath)