import requests
from bs4 import BeautifulSoup
ip='119.160.119.116'
url = 'https://whatismyipaddress.com/ip/'+ip
response=requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
result=soup.find_all('table')#getting all tables in webpage

z=[]
for z1 in result:#combining result into 1 list
    z=z+z1.find_all('tr')
cleandata=[]
for row in z:#getting clean table data
    colsdata = row.find_all('td')
    colsdata = [x.text.strip() for x in colsdata]
    cleandata.append([x for x in colsdata if x])
cleandata2=[]
for row in z:#getting clean table heading
    colshead = row.find_all('th')
    colshead = [y.text.strip() for y in colshead]
    cleandata2.append([x for x in colshead if y])
finalresult=[]
finalresult=[a+b for a,b in zip(cleandata2, cleandata)]#combining two list

finalresult





