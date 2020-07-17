# coding:utf8
#-------------------------------------------------------------------------------
# Name:        html_output
# Purpose:     Output html
#
# Author:      Zhang Yingjie
#
# Created:     17-07-2020
# Copyright:   (c)  2020
#-------------------------------------------------------------------------------


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html','w',encoding = 'utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        # ascii -> utf-8
        for data in self.datas:
            fout.write("<tr>") # line
            fout.write("<td>%s</td>" %data['url']) 
            fout.write("<td>%s</td>" %data['title']) 
            fout.write("<td>%s</td>" %data['summary']) 
            fout.write("</tr>")
            
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    
    



