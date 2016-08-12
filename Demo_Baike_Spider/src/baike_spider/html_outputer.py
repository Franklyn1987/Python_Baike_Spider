#coding:utf8

'''
Created on 2016年8月11日

@author: chenxihang
'''

# html页面输出器
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    # 收集数据
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    # 将数据存到一个html中
    def output_html(self):
        fout = open('python_baike_output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        # ascii编码要改成utf-8编码,这个记得换，要不然会出现乱码的。。。。。
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode("utf-8"))
            fout.write("<td>%s</td>" % data['summary'].encode("utf-8"))
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
    



