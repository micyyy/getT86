import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.font_manager as fm

def main(code, days):    
    conn = sqlite3.connect('inv.db')

    sql = "SELECT date, total from INV where code = '{}' order by date desc LIMIT {};".format(code, days)
    df = pd.read_sql_query(sql, conn)
    
    df.sort_values('DATE', ascending = True, inplace=True)
    
    if len(df) == 0:
        print('no data')
        return
    
    my_title = '{} 近50天三大法人買賣超'.format(code)
    df.plot(kind = 'bar', title = my_title)

    plt.show()

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        code = sys.argv[1]  
        days = sys.argv[2]
    else:
        print('Usage: {} CODE DAYS'.format(sys.argv[0]))
        exit()        
    
    main(code, days)