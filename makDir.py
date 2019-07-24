# -*- coding:utf-8 -*-
import exrex
import sys
#黑名单
web_band =['www','com','cn','org','edu']

rule ='{web_dic}{dic_pass}'
def url_para(url):

    if '://' in url:
        url = url.split('://')[1].replace('/','')
    if '/' in url:
        url = url.replace('/','')
        return url

def dic_create(url):
    web_pass =open("web_pass.txt",'w')
    web_pass.close()
    web_dics = url.split('.')
    for web_dic in web_dics:
        if web_dic not in web_band:
            f_pass =open('pass.txt','r')
    for dic_pass in f_pass:
        dics =list(exrex.generate(rule.format(web_dic=web_dic,dic_pass=dic_pass.strip("\n"))))
    for dic in dics:
        web_pass =open("web_pass.txt",'a+')
        web_pass.write(dic+'\n')
        web_pass.close()
if __name__ =='__main__':
    if len(sys.argv) == 2:
        dic_create(url_para(sys.argv[1]))
        sys.exit(0)
    else:
        print u'请输入url，命令如下：\n'
        print u"python %swww.demo.com" %sys.argv[0]
        sys.exit(-1)

