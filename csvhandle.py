import pandas as pd
import csv
import os

#THIS FILE CONTAINS FUNCTIONS TO HANDLE CSV FILE CREATION AND EDITING

def isEmpty(filepath): #check if csv file is empty
    if os.path.getsize(filepath) == 0:
        return True
    return False

def doesExist(filepath): #check if csv file exists
    if os.path.exists(filepath):
        return None
    with open(filepath, 'w'):
        pass

def initFile(filepath): #check if file exists and is empty, if so, initialize its headers
    doesExist(filepath)
    if isEmpty(filepath):
    # Create a new column with calculated values
        initialheader = ['Company', 'JobName', 'Location', 'JobType', 'ApplyAddress']
        # Write the updated DataFrame back to a CSV file
        with open(filepath, 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                            fieldnames=initialheader)
            dw.writeheader()

def addRow(scrapped, filepath): #create row for a scrapped job 
    df = pd.read_csv(filepath) 
    new_record = []
    for i in scrapped: #fills an array with values for dataframe rows
        new_record.append(i)    
        if len(new_record) == 5: 
            print(new_record)
            fixMismatchedColumns(df, new_record) #avoid mismatching number of columns due to analyse columns
            df.loc[len(df)] = new_record #add row to dataframe
            new_record = [] #reset array

    df.to_csv(filepath, index=False) #sends dataframe to .csv file

def fixMismatchedColumns(df, row): #fills row with empty values if needed
    n_columns = len(df.columns)
    if n_columns > len(row):
        while n_columns > len(row):
            row.append('')
    
def addColumn(name, info, filepath): #add generic column
    df = pd.read_csv(filepath) #read file
    df[name] = info
    df.to_csv(filepath, index=False)

def getLocation(filepath): #get location column info
    df = pd.read_csv(filepath, usecols = ['Location'], low_memory = True)
    aux = df['Location']
    location = aux.values.tolist()
    return location

def getCompanies(filepath): #get company column info
    companies = []
    df = pd.read_csv(filepath, usecols = ['Company'], low_memory = True)
    aux = df['Company']
    companies = aux.values.tolist()
    return companies

def getVisited(filepath): #get company column info with no repetitions
    visited = getCompanies(filepath)
    filtered_visited = []
    for i in visited:
        if i not in filtered_visited:
            filtered_visited.append(i)
    return filtered_visited

def getColumnSize(filepath):
    random_column = getLocation(filepath)
    n = len(random_column)
    return n