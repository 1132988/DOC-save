#Приём для частных лиц
import sys
import os
import sqlite3
from docxtpl import DocxTemplate
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'Russian')
def sn_server(): # Находим индекс "SSF" и ещё 6 цифр серийного номера сервера или рабочей станции из примечания (код этой функции задействован, сама функция - нет)
    index = note.find("SSF")  
    snserv_dir = note[index:index+9]  
    print(snserv_dir)
def yes_not(): #Возможность перезаписи файла (отказались)
    print("Вы хотите перезаписать файл?")
    answer = input('Введите Y или N: ')
    answer = answer.title()
    if answer == "Y":
        print("Создаём новый файл")
        doc.save(f'D:/Documents/{act}приёмЧЛ.docx')  # Место куда сохраняется этот файл
    else:
        print("Оставлено без изменений")
def check_miss(): #Проверка по количеству символов для: серийного номера оборудования и неисправности
    if len(wrong)>=5 and len(sn)>=5 and len(note)>=9 and snsrv:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно сохранить файл, вводите данные полностью!!!')
        print('Серийный номер должен иметь 5 символов! Ваше количество:', len(sn), '. Ошибки, количество символов (минимум 5):', len(wrong), '. Проверьте правильность введения SN Сервера или рабочей станции: ', snsrv)
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")      
def folders(): #Проверка и создание папки
    folder_way = f'D:/Documents/{data_y}/{data_f}/{snsrv}'
    if not os.path.exists(folder_way):
        os.makedirs(folder_way)
        print("Папка создана")
    else:
        print("Папка уже существует")
def check_file(): #Проверка на наличие файла
    test = f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}приёмЧЛ.docx'
    if os.path.exists(test) and os.path.isfile(test): 
        print(f"Есть файл с таким названием {act}приёмЧЛ.docx")
        print('Размер:', os.path.getsize(test) // 1024, 'Кб')
        print('Перезаписать файл нельзя, отредактируйте квитанцию', f'{act}приёмЧЛ.docx вручную!')
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")
    else:
        doc.save(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}приёмЧЛ.docx')  # Место куда сохраняется этот файл
        print("Сохранён новый файл")
def database(): #Создание базы данных
    conn = sqlite3.connect('trial_guarantee.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS priyom_ch (id INTEGER PRIMARY KEY, act INTEGER, wrong TEXT, sn TEXT, snsrv TEXT, note TEXT)''')
    cursor.execute("INSERT INTO priyom_ch (act, snsrv, note, sn, wrong) VALUES (?, ?, ?, ?, ?)", (act, snsrv, note, sn, wrong))
    conn.commit()
    conn.close()    
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

doc = DocxTemplate(r'C:\Users\Администратор\Programs\pythonDOCX\Акт_приемаЧЛ.docx') #Шаблон от которого заполняется файл
print("Акт приёма для частных лиц")
act = input('Акт №: ')
model = input("Модель: ")
sn = input('Serial Number оборудования: ')
wrong = input('Заявленная Неисправность: ')
note = input('Примечание (Обязательно ввести SN Сервера или рабочей станции, далее по желанию): ')
name, nam = naming()

index = note.find("SSF")  # Находим индекс начала "SSF"
snserv_dir = note[index:index+9]  
print(snserv_dir)  # Выводим результат
snsrv = snserv_dir

check_miss() #Проверка по количеству символов для: серийного номера оборудования и неисправности

data = (input('Введите дату: ')) 
data_object = datetime.strptime(data, '%Y%m%d')
data = data_object.strftime('%d %B %Y')  #Перевод даты из вида "20010101" в "01 январь 2001"
data_f = data_object.strftime('%m %Y')
data_y = data_object.strftime('%Y')

context = {'act': act, 'model': model, 'sn': sn, 'wrong': wrong , 'note': note , 'date': data, 'name': name, 'nam': nam}
doc.render(context)

folders() #Проверка на наличие папки и её создание
check_file() #Проверка на наличие файла
database()
input("Нажмите Enter для закрытия программы")
