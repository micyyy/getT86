import sys
import sqlite3

def main(date):
    conn = sqlite3.connect('inv.db')

    c = conn.cursor()
    
    SQL = "SELECT date, code, fi, it, dl, total from INV where date = \'{}\' order by total desc LIMIT 50".format(date)
    cur = c.execute(SQL)
    
    for row in cur:
        print(row)
           
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        date = sys.argv[1]   
    else:
        print('Usage: {} DATE'.format(sys.argv[0]))
        exit()
        
    main(date)
