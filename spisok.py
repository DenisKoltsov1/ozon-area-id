
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver 
import os
from tkinter import *
from tkinter import ttk
import pandas as pd
import glob
import re
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
import yadisk


driver = undetected_chromedriver.Chrome()
        
global name, price,priceSkidka,nds,KomercialType,brendItem,typeItem,obiem,countItem,femal,classop,ManufacturerСountry,articul,width,linkUrl,hidth,anot,dlina,keyWord,linkUrldop,aromaClass,Sostav,keyWord1,linkUrldop1,linkBasic,linkAdditionally,linkAdditionally1,bigDopFoto,smallDopFoto,currentId,currentMassId ,i    
    
currentId = " "
currentId = id
#seconds = time.time()
#print(seconds)
#time.sleep(1)
# переход  на сайт  ozon
html = driver.get("https://www.ozon.ru/")
time.sleep(1)
#ищем  поле поиска
id = '215973958344'
kcal  =  driver.find_element(By.XPATH,"//input[contains(@class,'tsBodyL')]")
#time.sleep(1)
#вставляем  id
kcal.send_keys(id)
time.sleep(1)

#end =time.time() - seconds
#print(end)

#лупа для продолжения поиска

try:
    lupa  =  driver.find_element(By.XPATH,'//button[@type = "submit"]')
    #time.sleep(1)
    lupa.click()

    time.sleep(1)
#end =time.time() - seconds
#print(end)
except:
    pass
    print('элемент лупа не найдена')

    # клик по ссылке  продукта 


TovarNot = driver.find_element(By.XPATH,"//div[@data-widget = 'searchResultsError']")

if TovarNot :
    print('товар не найден')
else:
    print('тэг не найден')