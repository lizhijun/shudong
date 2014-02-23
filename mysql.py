import MySQLdb

try:
    conn=MySQLdb.connect(host="localhost",user="root",passwd="toor",db="iyourl",port=3306,charset="utf8",unix_socket="/tmp/mysql.sock")
    cur=conn.cursor()
    #count=cur.execute('select * from tags')
    #print count
    cur.execute('create database if not exists shudong')
    conn.select_db('shudong')
    cur.execute('create table cughole(id int,content varchar(255))')
     
    value=[1,'hi rollen']
    cur.execute('insert into cughole values(%s,%s)',value)
     
    values=[]
    for i in range(4):
        values.append((i,'hi rollen'+str(i)))
         
    cur.executemany('insert into cughole values(%s,%s)',values)
 
    cur.execute('update cughole set content="I am rollen" where id=3')
 
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "MySQL Error %d: %s" % (e.args[0],e.args[1])

