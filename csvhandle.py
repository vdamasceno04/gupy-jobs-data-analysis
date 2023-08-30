import pandas as pd

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

def getVisited(filepath):
    visited = []
    filtered_visited = []
    df = pd.read_csv(filepath, usecols = ['Company'], low_memory = True)
    visited = df.values.tolist()
    for i in visited:
        if i not in filtered_visited:
            filtered_visited.append(i)
    return filtered_visited