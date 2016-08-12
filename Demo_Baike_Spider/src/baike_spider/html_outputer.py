#coding:utf8

'''
Created on 2016年8月11日

@author: chenxihang
'''

# 导入xlwt:excel处理框架
import xlwt 
# html页面输出器
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    # 收集数据
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    # 将结果存到一个html中
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
    
    # 将结果写入excel中
    def output_excel(self):
        
        # 创建excel文件，记得一定要加编码，要不然有的时候会出现乱码
        workbook = xlwt.Workbook(encoding = 'utf8')
        # 创建工作表
        worksheet = workbook.add_sheet('result_sheet')
        
        #xlwt中是行和列都是从0开始计算的 
        #xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位。
        #xlwt创建时使用的默认宽度为2960，既11个字符0的宽度
        #所以我们在设置列宽时可以用如下方法：
        #width = 256 * 20    256为衡量单位，20表示20个字符宽度
        first_col = worksheet.col(2)   
        first_col.width = 256*254 

        # 单元格样式
        style = xlwt.easyxf('pattern: pattern solid, fore_color red;')
        
        # 定义表格的标题栏
        worksheet.write(0,0,'url地址',style)
        worksheet.write(0,1,'标题',style)
        worksheet.write(0,2,'概述',style)
        
        row = 1
        # 写数据
        for data in self.datas:
            url = data['url']
            title = data['title']
            summary = data['summary']
            
            worksheet.write(row,0,"%s" % url)
            worksheet.write(row,1,"%s" % title)
            worksheet.write(row,2,"%s" % summary)
            
            row = row + 1
            
        # 保存表格    
        workbook.save('python_result_excel.xls')
            

