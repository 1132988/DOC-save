import os
import sys
import datetime
from docxtpl import DocxTemplate
from datetime import datetime
import locale
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
        #sys.exit(1)
        input("Нажмите Enter для закрытия программы")
    else:
        doc.save(f'D:/Documents/{data_y}/{data_f}/{snsrv}/{act}возвратЧЛ.docx')  # Место куда сохраняется этот файл
        print("Файл сохранен")

doc = DocxTemplate(r'C:\Program Files\Python38\pythonDOCX\Акт_возвратаЧЛ.docx')
print("Акт возврата для частных лиц")
act = input('Акт №: ')
sn = input('Serial Number оборудования: ')
note = input('Примечание, что было сделано и тп (Обязательно ввести SN Сервера или рабочей станции, далее по желанию): ')

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

context = {'act': act, 'model': input('модель: '), 'sn': sn, 'note': note, 'act_p': input('Ранее принято по акту: '), 'date': data}
doc.render(context)
folders()
check_file()
input("Нажмите Enter для закрытия программы")

