import webscrapping as ws
import csvhandle
import pandas as pd

url = 'https://globo.gupy.io/'
FILEPATH = 'data.csv'

scrapped = ws.webscrape(url)
csvhandle.addInfo(scrapped, FILEPATH)