
# coding: utf-8

# In[3]:

import pymysql
import getpass

pas = getpass.getpass("Input pass for ka: \n")

# Open database connection
db = pymysql.connect("localhost", "henry", pas, "ka" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()


# 

# In[ ]:



