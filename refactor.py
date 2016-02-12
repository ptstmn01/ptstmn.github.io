# -*- coding: utf-8 -*-
import os
path = __file__[:-11]

def en(path=path):
  path_collection = []
  for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
      fullpath = os.path.join(dirpath, file)
      path_collection.append(fullpath)
  return path_collection

#Изменение содержимого всех вайлов в папке и подпапках
def refactor():
  allfile = en()
  for file in allfile:
    #Только для html файлов
    if file.find('/all') > -1:
      continue
    if file[-5:] == ".html":
      openfile = open(file, "r", encoding="utf-8")
      text = openfile.read()
      #Исправление\замена текста
      er1 = '''ptstmn.github.io'''
      nr1 = '''ptstmn.ru'''
      text = text.replace(er1, nr1)
      #***Исправление\замена текста
      openfile.close()
      openfile = open(file, "w", encoding="utf-8")
      openfile.write(text)
      openfile.close()

#Прочитать файл
def read_file(filename):
  t = open(filename, "rb")
  #t = codecs.open(filename, encoding="utf-8")
  res = t.read()
  t.close()
  return res

#При запуске common.py
if __name__ == "__main__":
  refactor()
