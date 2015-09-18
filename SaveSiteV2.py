# -*- coding: utf-8 -*-
import requests
from os import path
from os import makedirs
from bs4 import BeautifulSoup as bs4

site = 'http://ptstmn.ru'
site2 = 'http://ptstmn.github.io'
error1 = '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8 >'
error2 = '© 2010 ПромТехСервис'
error3 = '<a href="http://columna.ru" title="Создание сайта">Cоздание сайта</a> — Columna'
noerror1 = ''
noerror2 = '© 2015 ПромТехСервис'
noerror3 = '<a href="http://vgit.ru" title="Поддержка сайта">Поддержка сайта — Студия ИТ решений VG</a>'
#Сохранение файла
def SavingFile(file, link = ''):
    if file == site2 or file == site2 + '/':
        return False
    if not (file.find('.ru')>0):
        if FileExist(file):
            link = site + '/' + link
            link = requests.get(link)
            FilePath = path.dirname(file)
            if not (FilePath == ''):
                if not (path.exists(FilePath)):
                    makedirs(FilePath)
            #Картинки
            if file[-3:] == 'png' or file[-3:] == 'jpg' or file[-4:] == 'jpeg' or file[-3:] == 'ico':
                OpenFile = open(file, "wb")
                OpenFile.write(link.content)
                OpenFile.close()
            #JavaScript and CSS
            elif file[-2:] == 'js' or file[-3:] == 'css':
                r = requests.get(link.url)
                with open(file, "wb") as code:
                    code.write(r.content)
            #Остальное в частности HTML
            else:
                if file == '':
                    return False
                OpenFile = open(file, 'w', encoding='utf8')
                text = link.text
                text = text.replace(site, site2)
                text = text.replace(error1, noerror1)
                text = text.replace(error2, noerror2)
                text = text.replace(error3, noerror3)
                with OpenFile:
                    for char in text:
                        OpenFile.write(char)
                OpenFile.close()
            return True
        else:
            return False
    else:
        return False

#Поиск ссылок на сохраненной странице
def FindHref(file):
    OpenFile = open(file, 'r', encoding='utf8')
    CurrentPage = bs4(OpenFile, "html5lib")
    OpenFile.close()
    a = CurrentPage.find_all('a')
    se = set()
    for i in a:
        try:
            href = i.attrs['href']
            if href.find( '.ru' ) > -1:
                flag = False
            elif href.find( '.jpg' ) > -1 or href.find( '.png' ) > -1 or href.find( '.jpeg' ) > -1\
                 or href.find( '.js' ) > -1 or href.find( '.css' ) > -1 or href.find( '.ico' ) > -1:
                flag = False
            else:
                flag = True
            if flag:
                se.add(href)
        except KeyError:
            pass
    return se

#Поиск картинок
def FindPict(file):
    OpenFile = open(file, 'r', encoding='utf8')
    CurrentPage = bs4(OpenFile, "html5lib")
    OpenFile.close()
    pict = CurrentPage.find_all('img')
    se = set()
    for i in pict:
        try:
            href = i.attrs['src']
            se.add(href)
        except KeyError:
            pass
    return se

#Поиск картинок в CSS
def FindPictInCSS(file):
    OpenFile = open(file, 'r', encoding='utf8')
    se = set()
    for i in OpenFile.readlines():
        if i.find('url')>-1:
            url = i[i.find('url')+6:i.find(')',i.find('url'))]
            se.add(url)
    OpenFile.close()
    return se

#Поиск JavaScrypt
def FindJS(file):
    OpenFile = open(file, 'r', encoding='utf8')
    CurrentPage = bs4(OpenFile, "html5lib")
    OpenFile.close()
    pict = CurrentPage.find_all('script', attrs={'type' : 'text/javascript'})
    se = set()
    for i in pict:
        try:
            href = i.attrs['src']
            se.add(href)
        except KeyError:
            pass
    return se

#Поиск CSS
def FindCSS(file):
    OpenFile = open(file, 'r', encoding='utf8')
    CurrentPage = bs4(OpenFile, "html5lib")
    OpenFile.close()
    pict = CurrentPage.find_all('link', attrs={'type' : 'text/css'})
    se = set()
    for i in pict:
        try:
            href = i.attrs['href']
            se.add(href)
        except KeyError:
            pass
    return se

#Поиск ICO
def FindICO(file):
    OpenFile = open(file, 'r', encoding='utf8')
    CurrentPage = bs4(OpenFile, "html5lib")
    OpenFile.close()
    pict = CurrentPage.find_all('link', attrs={'type' : 'image/x-icon'})
    se = set()
    for i in pict:
        try:
            href = i.attrs['href']
            se.add(href)
        except KeyError:
            pass
    return se

#Проверка существования файла
def FileExist(file):
    return(not(path.exists(file)))

def SaveCSS(whatt = set()):
    while whatt.__len__()>0:
        j = whatt.pop()
        if j[:1]=='/':
            j = j[1:]
        SavingFile(j, j)
        PIC = FindPictInCSS(j)
        while PIC.__len__()>0:
            pic = PIC.pop()
            if pic[:1]=='/':
                pic = pic[1:]
            SavingFile(pic, pic)

def SaveICO(whatt = set()):
    while whatt.__len__()>0:
        j = whatt.pop()
        if j[:1]=='/':
            j = j[1:]
        SavingFile(j, j)

def SavePict(whatt = set()):
    while whatt.__len__()>0:
        j = whatt.pop()
        if j[:1]=='/':
            j = j[1:]
        SavingFile(j, j)

def SaveJS(whatt = set()):
    while whatt.__len__()>0:
        j = whatt.pop()
        if j[:1]=='/':
            j = j[1:]
        SavingFile(j, j)

def SaveHTML(page = 'index.html'):
    #HTML
    if SavingFile(page, page):
        #ICO
        whatt = FindICO(page)
        SaveICO(whatt)
        #Pict
        whatt = FindPict(page)
        SavePict(whatt)
        #JS
        whatt = FindJS(page)
        SaveJS(whatt)
        #CSS
        whatt = FindCSS(page)
        SaveCSS(whatt)
        #Other HTML
        links = FindHref(page)
        while links.__len__()>0:
            i = links.pop()
            if i[:1]=='/':
                i = i[1:]
            print(i)
            SaveHTML(i)

SaveHTML()