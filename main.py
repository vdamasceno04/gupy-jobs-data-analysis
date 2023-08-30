import webscrapping as ws

url = 'https://globo.gupy.io/'

a = ws.getHtml(url)
b = ws.separateJobList(a)
c = ws.getJobInfo(b)
d = ws.getApplyAddress(url, b)
e = ws.joinDataArrays(c, d)

print(e)