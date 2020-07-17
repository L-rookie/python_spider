# coding:utf8
#-------------------------------------------------------------------------------
# Name:        test_beautifulSoup
# Purpose:     To test Beautiful Soup
#
# Author:      Zhang Yingjie
#
# Created:     16-07-2020
# Copyright:   (c)  2020
# Install: pip install beautifulsoup4
#-------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')  # 'html.parser':解析器

print("All Links")
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())
"""
All Links
a http://example.com/elsie Elsie
a http://example.com/lacie Lacie
a http://example.com/tillie Tillie
"""

print()

print("lacie url")
link_node = soup.find('a',href = "http://example.com/lacie")
print(link_node.name,link_node['href'],link_node.get_text())
"""
lacie url
a http://example.com/lacie Lacie
"""

print()
print("Regular expression matching")
link_node = soup.find('a',href = re.compile(r"ill")) # r: 只需要一个反斜线
print(link_node.name,link_node['href'],link_node.get_text())
"""
Regular expression matching
a http://example.com/tillie Tillie
"""

print()
print("p paragraph")
p_node = soup.find('p', class_="title") # class加下划线
print(p_node.name,p_node.get_text())
"""
p paragraph
p The Dormouse's story
"""