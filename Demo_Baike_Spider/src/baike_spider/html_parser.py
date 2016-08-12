#coding:utf8

'''
Created on 2016年8月11日

@author: chenxihang
'''
from bs4 import BeautifulSoup
import re
import urlparse

#html解析器
class HtmlParser(object):
    
    #解析全部新的url方法：两个参数(新的url、新的内容)
    def _get_new_urls(self, page_url, soup):
        
        new_urls = set()
        # /view/123.htm
        # 使用正则来匹配url
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            # 拼接全url路径
            # print link,page_url,new_url
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
            
        return new_urls    
    
    #解析全部新的数据
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        # url
        res_data['url'] = page_url
        
        #标题 <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node
        
        #概述 <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        #返回新的解析数据
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        #用BeautifulSoup解析新的url
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
