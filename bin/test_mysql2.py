#######!/usr/bin/python
# -*- coding: utf8 -*-

# Connector/Python is that it is pure Python you do not need anything else but Python installed. 
# MySQLdb on the other hand works only when you have MySQL libaries installed
# http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

import mysql.connector

if __name__ == "__main__":
  cnx = mysql.connector.connect(user='scott', password='tiger',
                                host='127.0.0.1',
                                database='employees')

  try:
    cursor = cnx.cursor()
    cursor.execute("""
       select 3 from your_table
    """)
    result = cursor.fetchall()
    print (result)
  finally:
    cnx.close()
