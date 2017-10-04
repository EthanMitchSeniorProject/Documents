import urllib.request as urllib2
from bs4 import BeautifulSoup

calvin_page = 'http://calvinknights.com/sports/msoc/2017-18/teams/calvin?view=profile&r=0&pos=kickers'

html_page = urllib2.urlopen(calvin_page)
soup = BeautifulSoup(html_page, 'html.parser')
table = soup.findAll("div", { "class" : "scrollable"})
print(table)

#table = soup.findAll("td", { "class" : "text pinned-col"})
#print(table)