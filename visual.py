from tkinter import *
from tkinter import ttk
import re
#import os
#import undetected_chromedriver 
from flashscore import parser,get_str_number,get_count,OpenPixx,addFoto
import pyperclip
'''

  303903410#c видео  
   154369096
   267911248 c dbltj 2
215973958
646065674


829002092
724581115
825952201
154369096
215973958


875752810
     '''
def bufer(event):
    q = pyperclip.paste()
    e1.insert(0, q)
    return e1
    
    return 1 

def getText(event):
    q = pyperclip.paste()
    text = e1.insert("1.0", q)

def func_parce(event):
    getText=e1.get("1.0",'end-1c')
    listId = re.findall('\d+', getText)
    print(listId)
    print(type(listId))

    

    for id in listId:
        parser(id)
        
        addFoto()

        
        file ="C:\\ozon1\\Парфюмерия.xlsx"
        r=get_str_number(file)
        count=get_count(r)
        try:
            OpenPixx(file,id,r)
        except:
            print('Проверьте: 1)Закрыт ли файл xlsx, при записи он должен быть закрыт.2) Файл должен находиться по пути C:\\ozon1\\Парфюмерия.xlsx 3) имя файла должно  быть Парфюмерия.xlsx  ')    


   
    return 1
#окно класс Tk
root = Tk() 
root.title("Парсер")
#размер окна
root.geometry("700x750")

#lbl = Label(root, text="Введите id")
label = ttk.Label(root, text="Введите id (9 цифр)")
label.pack(fill=X, padx=[279, 10], pady=20)
e1 = Text(root)
e1.pack(fill=X, padx=[60, 60], pady=30)

btn1 = ttk.Button(root,  text="вставить скопированный текст",width=40)


btn = ttk.Button(root,  text="начать парсинг",width=20)

'''
label1 = ttk.Label(root, text="вывод данных")
label1.pack(fill=X, padx=[155, 10], pady=10)
text = Text(width=25, height=5,
            fg='white', wrap=WORD)
 
text.pack()
'''
#label.pack(anchor=NW, padx=6, pady=6)
btn1.pack()
btn.pack(expand = 1)

btn1.bind("<Button-1>", getText)
btn.bind("<Button-1>", func_parce)

#show_message()
root.mainloop()

