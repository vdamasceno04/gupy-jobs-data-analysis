import webscrapping as ws
import pandas as pd

url = 'https://globo.gupy.io/'

a = ws.getHtml(url)
b = ws.separateJobList(a)
c = ws.getJobInfo(b)
d = ws.getApplyAddress(url, b)
e = ws.joinDataArrays(url, c, d)

df = pd.read_csv('data.csv')
print('csv: \n')

new_record = ['Apple', 'CEO', 'Colombo', 'Trainee']
df.loc[len(df)] = new_record

print(df)