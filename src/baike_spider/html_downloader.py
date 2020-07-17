# coding:utf8
#-------------------------------------------------------------------------------
# Name:        html_downloader
# Purpose:     Download html
#
# Author:      Zhang Yingjie
#
# Created:     17-07-2020
# Copyright:   (c)  2020
#-------------------------------------------------------------------------------
import urllib.request

class HtmlDownloader(object):
    

    def download(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    
    
    



