#Возврат для частных лиц
import os
import re
import sys
import sqlite3
import datetime
from docxtpl import DocxTemplate
from datetime import datetime
import locale
#from yaml import scan
from setup import files

locale.setlocale(locale.LC_ALL, 'Russian')
def check_miss(): #Проверка по количеству символов для: серийного номера и неисправности
    if len(sn)>=5 and len(note)>=9 and snsrv:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно сохранить файл, вводите данные полностью!!!')
        print('Серийный номер должен иметь 5 символов! Ваше количество:', len(sn), '. Ошибки, количество символов (минимум 5):', snsrv)
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")
def yes_not(): #Возможность перезаписи файла (отказались)
    print("Вы хотите перезаписать файл?")
    answer = input('Введите Y или N: ')
    answer = answer.title()
    if answer == "Y":
        print("Создаём новый файл")
        doc.save(f'D:/Documents/{act}возвратЧЛ.docx')  # Место куда сохраняется этот файл
    else:
        print("Оставлено без изменений")
def folders(): #Проверка и создание папки
    folder_way = f'D:/Documents/{data_y}/{data_f}/{snsrv}'
    if not os.path.exists(folder_way):
        os.makedirs(folder_way)
        print("Папка создана")
    else:
        print("Папка уже существует")
def sn_server(): # Находим индекс "SSF" и ещё 6 цифр серийного номера сервера или рабочей станции из примечания (код этой функции задействован, сама функция - нет)
    index = note.find("SSF")
    snserv_dir = note[index:index+9]
    print(snserv_dir)
def check_file(): #Проверка на наличие файла
    test = f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}возвратЧЛ.docx'
    if os.path.exists(test) and os.path.isfile(test):
        print(f"Есть файл с таким названием {act}возвратЧЛ.docx")
        print('Размер:', os.path.getsize(test) // 1024, 'Кб')
        print('Перезаписать файл нельзя, отредактируйте квитанцию', f'{act}возвратЧЛ.docx вручную!')
        sys.exit(1)
        input("Нажмите Enter для закрытия программы")
    else:
        doc.save(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}возвратЧЛ.docx')  # Место куда сохраняется этот файл
        print("Файл сохранен")
def database_and_filecheck(): #Создание базы данных ВОЗМОЖНО МОГУТ БЫТЬ ПРОБЛЕМЫ.
    test = f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}возвратЧЛ.docx'
    if os.path.exists(test) and os.path.isfile(test):
        print(f"Есть файл с таким названием {act}возвратЧЛ.docx")
        print('Размер:', os.path.getsize(test) // 1024, 'Кб')
        print('Перезаписать файл нельзя, отредактируйте квитанцию', f'{act}возвратЧЛ.docx вручную!')
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")
    else:
        conn = sqlite3.connect('trial_guarantee.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vozvrat_ch (id INTEGER PRIMARY KEY, act INTEGER, sn TEXT, snsrv TEXT, note TEXT, act_p INTEGER)''')
        cursor.execute("INSERT INTO vozvrat_ch (act, snsrv, note, sn) VALUES (?, ?, ?, ?)", (act, snsrv, note, sn)) #,act_p))
        conn.commit()
        conn.close()
        
        conn = sqlite3.connect('trial_guarantee.db')
        cursor = conn.cursor()
        cursor.execute("SELECT priyom_ch.act FROM priyom_ch JOIN vozvrat_ch ON priyom_ch.snsrv = vozvrat_ch.snsrv") #Думать над этим!!!
        act_p = cursor.fetchall()
        act_p = re.sub("[(|,|)]","", str(act_p[1]))
        print(act_p)
        cursor.execute("INSERT INTO vozvrat_ch (act_p) VALUES (?)", (act_p,))
        cursor.execute("DELETE FROM vozvrat_ch WHERE (act IS NULL OR act_p IS NULL) OR (act = '' OR act_p = '')")
        cursor.execute("INSERT INTO vozvrat_ch (act, snsrv, note, sn, act_p) VALUES (?, ?, ?, ?, ?)", (act, snsrv, note, sn, act_p))
        conn.commit()
        conn.close()           
        
        context = {'act': act, 'model': model, 'sn': sn, 'note': note, 'act_p': act_p, 'date': data, 'name': name, 'nam': nam} #Подумать.
        doc.render(context)
        doc.save(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}возвратЧЛ.docx')  # Место куда сохраняется этот файл
        print("Файл сохранен")
def naming():  #Кто делал файл
    print("Кто делал этот файл?")
    answer = input('Введите 1 (COM1), 2 (COM2), 3 (COM3): ')
    answer = answer.title()
    if answer == "1":
        name = "Начальник производства"
        nam = "Имя 1"
    elif answer == "2":
        name = "Главный инженер"
        nam = "Имя 2"
    else:
        name = "Специалист"
        nam = "Имя 3"    
    print(name)
    print(nam)
    return name, nam
   
#doc = DocxTemplate(r'C:\Users\Администратор\Programs\pythonDOCX\Акт_возвратаЧЛ.docx')
doc = DocxTemplate(files('Акт_возвратаЧЛ.docx'))
print("Акт возврата для частных лиц")
act = input('Акт №: ')
model = input('модель: ')
sn = input('Serial Number оборудования: ')
note = input('Что было сделано? Написать из какого сервера: ')
who = input('Кто делал акт?: ')
#act_p = input('Ранее принято по акту приёма: ') #Думать над этим
name, nam = naming()

index = note.find("SSF")  # Находим индекс начала "SSF"
snserv_dir = note[index:index+9]
print(snserv_dir)  # Выводим результат
snsrv = snserv_dir

check_miss()

data = (input('Введите дату: '))
data_object = datetime.strptime(data, '%Y%m%d')
data = data_object.strftime('%d %B %Y')
data_f = data_object.strftime('%m %Y')
data_y = data_object.strftime('%Y')

#context = {'act': act, 'model': model, 'sn': sn, 'note': note, 'act_p': act_p, 'date': data} #Подумать.
#doc.render(context)
folders()
#database()
#check_file()
database_and_filecheck()
input("Нажмите Enter для закрытия программы")