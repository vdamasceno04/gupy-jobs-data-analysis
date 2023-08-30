import pandas as pd
import csv
import os

def isEmpty(filepath): #check if csv file is empty
    if os.path.getsize(filepath) == 0:
        return True
    return False

def doesExist(filepath): #check if csv file exists
    if os.path.exists(filepath):
        return None
    with open(filepath, 'w'):
        pass

def initFile(filepath): #initialize .csv headers
    doesExist(filepath)
    if isEmpty(filepath):
    # Create a new column with calculated values
        initialheader = ['Company', 'JobName', 'Location', 'JobType', 'ApplyAddress']
        # Write the updated DataFrame back to a CSV file
        with open(filepath, 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                            fieldnames=initialheader)
            dw.writeheader()


def addInfo(scrapped, filepath):
    df = pd.read_csv(filepath) #read file
    new_record = []
    for i in scrapped: #fills an array with values for dataframe rows
        new_record.append(i)    
        if len(new_record) == 5: 
            print(new_record)
            df.loc[len(df)] = new_record #add row to dataframe
            new_record = [] #reset array

    df.to_csv(filepath, index=False) #sends dataframe to .csv file

def getLocation(filepath):
    df = pd.read_csv(filepath, usecols = ['Location'], low_memory = True)
    aux = df['Location']
    location = aux.values.tolist()
    return location

def getVisited(filepath):
    visited = []
    filtered_visited = []
    df = pd.read_csv(filepath, usecols = ['Company'], low_memory = True)
    aux = df['Company']
    visited = aux.values.tolist()
    for i in visited:
        if i not in filtered_visited:
            filtered_visited.append(i)
    return filtered_visited