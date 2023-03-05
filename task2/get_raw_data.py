import requests
import datetime
import json
import mysql.connector
import sqlite3
import os

#creat db/table
os.remove('./stock.db')
conn = sqlite3.connect('stock.db')
c = conn.cursor()
c.execute('''CREATE TABLE financial_data
       (
       symbol           TEXT    NOT NULL,
       date           TEXT    NOT NULL,
       open_price           TEXT    NOT NULL,
       close_price           TEXT    NOT NULL,
       volume           TEXT    NOT NULL
       );''')
conn.commit()
conn.close()
print ("db/table create")




def financial_data(symbol):
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+symbol+"&apikey=2D3RLZPNOAWTCN3S"
    r = requests.get(url)
    data = r.json()
    Meta = data["Meta Data"]
    Daily = data["Time Series (Daily)"]


    list_meta = []
    today = datetime.date.today()
    two_week_ago = today - datetime.timedelta(days=14)
    date = two_week_ago
    for i in range(14): 
        date += datetime.timedelta(days=1)

        try:                      
            Daily_loop = Daily[str(date)]
            dict_process = {
                    'symbol': Meta["2. Symbol"], 
                    'date': str(date), 
                    'open_price': Daily_loop["1. open"], 
                    'close_price': Daily_loop["4. close"], 
                    'volume': Daily_loop["6. volume"]
            }
            list_meta.append(dict_process)
            #print(dict_process)

            try:
                c.execute("INSERT INTO financial_data (symbol,date,open_price,close_price,volume) \
                            VALUES ('"+Meta["2. Symbol"]+"', '"+str(date)+"', '"+Daily_loop["1. open"]+"', '"+Daily_loop["4. close"]+"', '"+Daily_loop["6. volume"]+"' )")
                conn.commit()
            except:
                print("Error")
                conn.rollback()


            pass

        except:                   
            #print('Holiday')
            pass
    jsonStr = json.dumps(list_meta)
    conn.close()
    return jsonStr


AAPL=financial_data("AAPL")
print(AAPL)
IBM=financial_data("IBM")
print(IBM)
print("Done")

