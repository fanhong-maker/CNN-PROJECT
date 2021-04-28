# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:22:54 2021

@author: 26601
"""


import urllib.request as ur
import os
import re 

#print(os.getcwd())
#//jandan.net/girl/MjAyMTA0MTAtMTI3#comments
#//jandan.net/girl/MjAyMTA0MTMtMTM2#comments

def open_pages(url):
    url = url
    res = ur.Request(url)
    res.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68')
    response = ur.urlopen(res).read()
    return response

def get_pages(pages):
    addres = []
    response = open_pages('http://jandan.net/girl')
    response= response.decode('utf-8')
    for i in range(pages+1):
        #start = response.find('current-comment-page')
        #end = response.find('MjAyMTA0MTAtMTI',start)
        #the_page = int(response[end+len('MjAyMTA0MTAtMTI')])+1
        #使用正则表达式
        #for n in range(2):
        start = response.find('current-comment-page')
        if i == 1:
            response = response
        else:
            response = response[start:]
        a = re.search(r'//jandan.net/girl/MjAyMTA0MTMtMT([A-Z]|[a-z])([w-z]|[0-5])#comments', response).span()
        addres.append('http:'+response[a[0]:a[1]])
        response = open_pages(addres[-1])
        response= response.decode('utf-8')
    return addres[1:]

def get_picture_addres(pages):
    picture_addres = []
    addres = get_pages(pages)
    for each in addres:
        a = 0
        response = open_pages(each)
        response= response.decode('utf-8')
        while True:
            a = response.find('img src',a)
            if a != -1:
                b = response.find('.jpg',a,a+255)
                if b != -1:
                    the_addres = response[a+len('img src')+2:b]+'.jpg'
                    picture_addres.append(the_addres) 
                    a = b
                else:
                    a = a+7
            else:
                break
    return picture_addres

def download_picture(filename = 'the_sexy_girl5',pages = 10):
    os.mkdir(filename)
    os.chdir(filename)
    picture_addres = get_picture_addres(pages)
    
    for addres in picture_addres:
        #print(addres)
        with open(addres.split('/')[-1],'wb') as f:
            response = open_pages('http:'+addres)
            f.write(response)
     
download_picture(pages = 40)
#addres = get_pages(6)
#print(addres)
