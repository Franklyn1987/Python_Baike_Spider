#coding:utf8

'''
Created on 2016年8月11日

@author: chenxihang
'''
import urllib2

#html下载器
class HtmlDownloader(object):

    def downloader(self,url):
        if url is None:
            return None
        
        #urllib2请求url内容
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()