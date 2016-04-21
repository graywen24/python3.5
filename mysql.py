__author__ = 'wenwen'
print( "hello world" )


import pymysql
import pymysql.cursors



     #Get a database connection, note if it is UTF-8Type, need
conn = pymysql.connect(host='172.16.226.134',user='root',passwd='P@ssw0rd',db='mysql', port=3306)
cur = conn.cursor()
cur.execute("SELECT  Host,User,account_locked FROM user")
#print(cur.description)
data = cur.fetchall()

for d in data :
    print("host : "+str(d[0])+' user: '+d[1]+"  locked: "+d[2])

cur.close()
conn.close()







