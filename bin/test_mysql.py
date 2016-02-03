#######!/usr/bin/python
# -*- coding: utf8 -*-

# Connector/Python is that it is pure Python you do not need anything else but Python installed. 
# MySQLdb on the other hand works only when you have MySQL libaries installed
# http://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

if __name__ == "__main__":
  db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
  cursor = db.cursor()
  cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
  sql = """CREATE TABLE EMPLOYEE (
           FIRST_NAME  CHAR(20) NOT NULL,
           LAST_NAME  CHAR(20),
           AGE INT,  
           SEX CHAR(1),
           INCOME FLOAT )"""

  cursor.execute(sql)
  db.close()
