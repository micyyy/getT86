import sqlite3


def create_inv():
    conn = sqlite3.connect('inv.db')

    c = conn.cursor()


    c.execute('''CREATE TABLE INV
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EXCHANGE TEXT NOT NULL,
        DATE TEXT NOT NULL,
        CODE TEXT NOT NULL,
        FI INTEGER,
        IT INTEGER,
        DL INTEGER,
        TOTAL INTEGER);''')

    conn.commit()

def create_daily():    
    conn = sqlite3.connect('daily.db')

    c = conn.cursor()

    c.execute('''CREATE TABLE DAILY
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EXCHANGE TEXT NOT NULL,
        DATE TEXT NOT NULL,
        CODE TEXT NOT NULL,
        OPEN INTEGER,
        HIGH INTEGER,
        LOW INTEGER,
        CLOSE INTEGER,
        VOLUME INTEGER);''')
        
    conn.commit()

if __name__ == '__main__':
    create_inv()
    create_daily()