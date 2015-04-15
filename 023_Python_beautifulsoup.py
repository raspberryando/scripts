from bs4 import BeautifulSoup
import urllib2

url = "http://magiccards.info/query?q=%2B%2Bo!%22Counterspell%22&v=olist"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

tables=soup.findAll('table',{'cellpadding':'3'})

for table in tables:
	trs = table.findAll('tr');
	for tr in trs:
		n = 0
		for td in tr.findAll('td'):
			n = n + 1
			if (n==6):
				print(td.text.encode('ascii', 'ignore'))
