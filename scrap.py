#Importing request module for requesting web server
import urllib

import requests



from bs4 import BeautifulSoup
url='http://howstat.com/cricket/Statistics/Players/PlayerInnings_ODI.asp?PlayerID=3600'


page= urllib.request.urlopen(url)

#Parser
soup = BeautifulSoup(page, 'html.parser')

div = soup.find("div", { "id" : "bat" })
table = div.find("table")

for x in table:
 rows = table.find_all('tr')
 for tr in rows:
     data = []
     cols = tr.find_all('td')  # find all td tags
     for td in cols:
         data.append(td.text.strip())


#print (data)
print (data[8])











