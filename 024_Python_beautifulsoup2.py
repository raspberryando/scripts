from bs4 import BeautifulSoup
import urllib2
import sqlite3


url = "http://magiccards.info/query?q=%2B%2Bo!%22Counterspell%22&v=olist"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

tables=soup.findAll('table',{'cellpadding':'3'})

db =  sqlite3.connect('db.sqlite')
cursor = db.cursor()
cursor.execute("CREATE TABLE cartas (id INTEGER PRIMARY KEY, edicion TEXT);")
db.commit()

for table in tables:
        trs = table.findAll('tr');
        for tr in trs:
                n = 0
                for td in tr.findAll('td'):
                        n = n + 1
                        if (n==6):
                                edicion = td.text.encode('ascii', 'ignore')
                                print(edicion)
                                cursor.execute("INSERT INTO cartas (edicion) VALUES (:edicion);", {'edicion':edicion})
db.commit()
db.close()
