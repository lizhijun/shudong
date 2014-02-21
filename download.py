# -*- Encoding: utf-8 -*-
import urllib

f = urllib.urlopen("http://page.renren.com/601694006?checked=true")

#地大树洞url: http://page.renren.com/601694006
cughole = "http://page.renren.com/601694006"

#得到一个网页的字符串file_str
file_str = f.read()

#开始爬取内容
#content_list = [] #存储爬取的信息
for i in range(1, 10):
    start_pos = file_str.find("<span class=\"status-detail\">")
    file_str = file_str[start_pos :]
    end_pos = file_str.find("</span>")
    #content_list.append(file_str[start_pos : end_pos + start_pos])
    print i, file_str[28: end_pos]
    file_str = file_str[end_pos :]
