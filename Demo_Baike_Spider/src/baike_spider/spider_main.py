#coding:utf8

'''
Created on 2016年8月11日

@author    : chenxihang

@describe  : 本爬虫程序主要用来爬取百度百科Python词条1000条相关数据
             用到的类有url管理器、html下载器、html解析器、html输出器
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer
from warnings import catch_warnings

# 爬虫总调程序
class SpiderMain(object):
    
    # 初始化url管理器、下载器、解析器、输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    #爬虫方法    
    def craw(self, root_url):
        #统计当前url编号
        count = 1
        self.urls.add_new_url(root_url)
        
        # 是否有新的url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                #打印当前爬取的是第几个url
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.downloader(new_url)
                
                #解析出新的url和内容
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)    
                
                #爬取到100个,退出
                if count == 100 :
                    break
                count = count + 1
            
            except:
                print 'craw failed'
            
        #输出器输出html页面
        self.outputer.output_html()

#函数主入口,用来启动整个爬虫程序
if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
