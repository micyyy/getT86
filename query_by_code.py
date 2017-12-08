import sys
import sqlite3

def main(code):
    conn = sqlite3.connect('inv.db')

    c = conn.cursor()
    
    SQL = "SELECT date, code, fi, it, dl, total from INV where code = \'{}\' order by date desc LIMIT 50".format(code)
    cur = c.execute(SQL)
    
    for row in cur:
        print(row)
           
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        code = sys.argv[1]   
    else:
        print('Usage: {} CODE'.format(sys.argv[0]))
        exit()
        
    main(code)
