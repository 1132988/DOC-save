#Квитанция приёме оборудования, печатается
import sys
import sqlite3
import os
from docxtpl import DocxTemplate as dtl
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'Russian')
def check_miss(): #Проверка по количеству символов для: телефона, серийного номера и неисправности
    if len(wrong)>=5 and len(phone)>=10 and snsrv:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно сохранить файл, вводите данные полностью!!!')
        print('Серийный номер должен иметь 9 символов! Ваше количество:', len(sn), '. Ошибки, количество символов (минимум 5):', len(wrong), '. Номер телефона должен иметь минимум 10 символов! У вас:', len(phone))
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")

def check_file(): #Проверка на наличие файла
    test = f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}.docx'
    if os.path.exists(test) and os.path.isfile(test): 
        print(f"Есть файл с таким названием {act}.docx")
        print('Размер:', os.path.getsize(test) // 1024, 'Кб')
        print('Перезаписать файл нельзя, отредактируйте квитанцию', f'{act}.docx вручную!')
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")
    else:
        doc.save(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}.docx')  # Место куда сохраняется этот файл
        print("Сохранён новый файл")
        #os.startfile(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}.docx', 'print') #Печать файла на принтере 1
        #os.startfile(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}.docx', 'print') #Печать файла на принтере 2
       
def yes_not(): #Возможность перезаписи файла (отказались)
    print("Вы хотите перезаписать файл?")
    answer = input('Введите Y или N: ')
    answer = answer.title()
    if answer == "Y":
        print("Создаём новый файл")
        doc.save(f'D:/Documents/{act}.docx')  # Место куда сохраняется этот файл
    else:
        print("Оставлено без изменений")

def folders(): #Проверка и создание папки
    folder_way = f'D:/Documents/{data_y}/{data_f}/{snsrv}'
    if not os.path.exists(folder_way):
        os.makedirs(folder_way)
        print("Папка создана")
    else:
        print("Папка уже существует")
def database():
    conn = sqlite3.connect('example_p.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, act INTEGER, phone TEXT, wrong TEXT, sn TEXT, snsrv TEXT, note TEXT)''')
    cursor.execute("INSERT INTO users (act, phone, snsrv, note, sn, wrong) VALUES (?, ?, ?, ?, ?, ?)", (act, phone, snsrv, note, sn, wrong))
    conn.commit()
    conn.close()

doc = dtl(r'C:\Program Files\Python38\pythonDOCX\Квитанция.docx')
act=input('Акт №: ')
wrong = input('Заявленная Неисправность: ')
phone = input('телефон: ')
sn = input('Serial Number оборудования: ')
note = input('Примечание (Обязательно ввести серийный номер сервера или рабочей станции!!!): ')

index = note.find("SSF")  # Находим индекс начала "SSF"
snserv_dir = note[index:index+9]  
print(snserv_dir)  # Выводим результат
snsrv = snserv_dir

check_miss()

data = (input('Введите дату: ')) 
data_object = datetime.strptime(data, '%Y%m%d')
data = data_object.strftime('%d %B %Y')  #Перевод даты из вида "20010101" в "01 январь 2001"
data_f = data_object.strftime('%m %Y')
data_y = data_object.strftime('%Y')

context = { 'act': act, 'company' : input('Компания Клиента:  '), 'name' : input('Имя клиента:  '), 'phone': phone, 'email': input('E-mail: '), 'model': input('модель: '), 'sn': sn, 'wrong': wrong, 'note': note}
doc.render(context)

folders()
check_file()
database()
input("Нажмите Enter для закрытия программы")