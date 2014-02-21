# -*- Encoding: utf-8 -*-
import urllib

f = urllib.urlopen("http://page.renren.com/601694006?checked=true")

#地大树洞url: http://page.renren.com/601694006
cughole = "http://page.renren.com/601694006"

#得到一个网页的字符串file_str
file_str = f.read()

#开始爬取内容
#content_list = [] #存储爬取的信息

values = []

for i in range(1, 10):
    start_pos = file_str.find("<span class=\"status-detail\">")
    file_str = file_str[start_pos :]
    end_pos = file_str.find("</span>")
    #content_list.append(file_str[start_pos : end_pos + start_pos])
    #print i, file_str[28: end_pos]
    values.append(( i, file_str[28: end_pos]))
    file_str = file_str[end_pos :]


import MySQLdb

try:
    conn=MySQLdb.connect(host="localhost",user="root",passwd="717df5eb",port=3306,charset="utf8",unix_socket="/tmp/mysql.sock")
    cur=conn.cursor()
    #count=cur.execute('select * from tags')
    #print count
    #cur.execute('create database if not exists shudong')
    conn.select_db('shudong')
    #cur.execute('create table cughole(id int,content varchar(255))')
     
    #value=[1,'hi rollen']
    #cur.execute('insert into cughole values(%s,%s)',value)
     
    #values=[]
    #for i in range(4):
    #    values.append((i,'hi rollen'+str(i)))
         
    cur.executemany('insert into cughole values(%s,%s)',values)
 
    #cur.execute('update cughole set content="I am rollen" where id=3')
 
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "MySQL Error %d: %s" % (e.args[0],e.args[1])


