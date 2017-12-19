import requests
from datetime import date, timedelta
import time
import sqlite3
import json

today = date.today().strftime('%Y%m%d')

def retrieve_inv_data(today):
    URL = 'http://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALLBUT0999'.format(today)
    req = requests.get(URL)

    jdata = json.loads(req.text)

    if jdata['stat'] != 'OK':
        print('{} data not OK'.format(today))
        return

    conn = sqlite3.connect('inv.db')    
    c = conn.cursor()
    
    date = today
    exchange = 'TSE'

    c.execute("SELECT count(*) from INV where date = ?", (today, ))
    
    result = c.fetchone()
    
    if result[0] > 0:
        print('skipped {}'.format(today))
        return
    
    for data in jdata['data']:
        code =  data[0]
        fi =  int(data[4].replace(',', '')) + int(data[7].replace(',', ''))
        it =  int(data[10].replace(',', ''))
        dl =  int(data[11].replace(',', ''))
        total = int(data[18].replace(',', ''))
        
        c.execute("INSERT INTO INV (EXCHANGE, DATE, CODE, FI, IT, DL, TOTAL) VALUES(?, ?, ?, ?, ?, ?, ?)", (exchange, date, code, fi, it, dl, total, ))

    conn.commit() 

if __name__ == '__main__':
    for i in range(1):
        mydate = date.today() + timedelta(days = -i)
        smydate = mydate.strftime('%Y%m%d')
        
        print(smydate)
        retrieve_inv_data(smydate)
        
        time.sleep(5)
