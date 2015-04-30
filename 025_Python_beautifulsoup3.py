from bs4 import BeautifulSoup
import urllib2
import sqlite3


url = "http://magiccards.info/query?q=%2B%2Bo!%22Counterspell%22&v=olist"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

tables=soup.findAll('table',{'cellpadding':'3'})

db =  sqlite3.connect('db.sqlite')
cursor = db.cursor()
cursor.execute("CREATE TABLE cartas (id INTEGER PRIMARY KEY, nombre TEXT, tipo TEXT, coste TEXT, rareza TEXT, artista TEXT, edicion TEXT);")
db.commit()

for table in tables:
        trs = table.findAll('tr');
        for tr in trs:
                n = 0
                campos = []
                for td in tr.findAll('td'):
                        campos.append(td.text.encode('ascii', 'ignore'))
                        n = n + 1
                        if (n==6):
                                print(campos)
                                cursor.execute("INSERT INTO cartas (nombre, tipo, coste, rareza, artista, edicion) VALUES (?,?,?,?,?,?);", campos)
                                campos=[]
db.commit()
db.close()
