import webscrapping as ws
import pandas as pd

url = 'https://globo.gupy.io/'

scrapped = ws.webscrape(url)

df = pd.read_csv('data.csv')
print('csv: \n')

new_record = []
for i in scrapped:
    new_record.append(i)
    if len(new_record) == 5:
        print(new_record)
        df.loc[len(df)] = new_record
        new_record = []

df.to_csv('data.csv') #errado, bagunçando categorias
print(df)