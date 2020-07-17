# coding:utf8
#-------------------------------------------------------------------------------
# Name:        test_urllib2
# Purpose:     To test urllib2
#
# Author:      Zhang Yingjie
#
# Created:     16-07-2020
# Copyright:   (c)  2020
# python2.x: urllib2  -> python3.x: urllib.request
# python2.x: cookielib  -> python3.x: cookiejar
#-------------------------------------------------------------------------------
import urllib.request
from http import cookiejar

url = "https://www.baidu.com/s?wd=cookielib&rsv_spt=1&rsv_iqid=0xa0ad4e9600001a4a&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=78040160_14_pg&ch=8&rsv_enter=1&rsv_dl=tb&oq=module%2520%2526%252339%253Burllib%2526%252339%253B%2520has%2520no%2520attribute%2520%2526%252339%253Brequest%2526%252339%253B&rsv_t=4d47uwtYFITeuE8ERDaVxNP%2BZxUlyMIfw3pUJ1RgvBLBmOIKEJazYlO%2FdxKBTOvnDYEUYPw&rsv_btype=t&inputT=599&rsv_pq=d7319b7e00000ba8&rsv_n=2&rsv_sug3=16&rsv_sug1=14&rsv_sug7=100&rsv_sug2=0&rsv_sug4=599"

print("Method One")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))
print()

print("Method Two")
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(url)
print(response2.getcode())
print(len(response2.read()))
print()

print("Method Three")
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
print()