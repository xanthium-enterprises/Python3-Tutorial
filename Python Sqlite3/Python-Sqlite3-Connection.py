# Python Sqlite3 Access

import sqlite3


try:
    sqlite_conn = sqlite3.connect(':memory:')     # Create Database in Memory
    #sqlite_conn = sqlite3.connect('sqlite_db.db')# Create Database in Disk

    sqlite_cursor = sqlite_conn.cursor()          # Create a Cursor object

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
    
    
finally:
    if sqlite_conn:
        sqlite_conn.close()
        print("The SQLite connection is closed")



