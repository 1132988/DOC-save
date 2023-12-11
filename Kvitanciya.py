
# 2. Дата приема или передачи сделать
import sys
import os
import datetime
from docxtpl import DocxTemplate

def check_miss(): #Проверка по количеству символов для: телефона, серийного номера и неисправности
    if len(wrong)>=5 and len(sn)==9 and len(phone)>=10:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно сохранить файл, вводите данные полностью!!!')
        print('Серийный номер должен иметь 9 символов! Ваше количество:', len(sn), '. Ошибки, количество символов (минимум 5):', len(wrong), '. Номер телефона должен иметь минимум 10 символов! У вас:', len(phone))
        sys.exit(1)

def check_phone(): #Проверка телефона (не используется)
    if len(phone)>=10:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно сохранить файл, так как номер введен не полностью')
        #sys.exit(1)

def check_sn(): #Проверка Serial Number (Не используется)
    if len(sn)==9:
        print("Продолжаем работу")
    else:
        print('"ERROR!" Невозможно продолжить работу, неправильно введен серийный номер')
        sys.exit(1)
        
def yes_not(): #Возможность перезаписи файла (отказались)
    print("Вы хотите перезаписать файл?")
    answer = input('Введите Y или N: ')
    answer = answer.title()
    if answer == "Y":
        print("Создаём новый файл")
        doc.save(f'D:/Documents/{act}.docx')  # Место куда сохраняется этот файл
    else:
        print("Оставлено без изменений")
def mkdir_file(): #Создание папки
# путь относительно текущего скрипта
    os.mkdir(sn)
# абсолютный путь
    os.mkdir(f'D:/Documents/{sn}')
doc = DocxTemplate("Квитанция о приёме оборудования(шаблон).docx")
act=input('Акт №: ')
wrong = input('Заявленная Неисправность: ')
phone = input('телефон: ')
sn = input('Serial Number оборудования: ')
check_miss()
context = { 'act': act, 'company' : input('Компания Клиента:  '), 'name' : input('Имя клиента:  '), 'phone': phone, 'email': input('E-mail: '), 'model': input('модель: '), 'sn': sn, 'wrong': wrong, 'note': input('Примечание: ')}
doc.render(context)
test = f'D:/Documents/{act}.docx'


if os.path.exists(test) and os.path.isfile(test):
    print(f"Есть файл с таким названием {act}.docx")
    print('Размер:', os.path.getsize(test) // 1024, 'Кб')
    print('Дата создания:', datetime.datetime.fromtimestamp(int(os.path.getctime(test))))
    print('Дата последнего открытия:', datetime.datetime.fromtimestamp(int(os.path.getatime(test))))
    print('Дата последнего изменения:', datetime.datetime.fromtimestamp(int(os.path.getmtime(test))))
    print('Перезаписать файл нельзя, отредактируйте квитанцию', f'{act}.docx вручную!')
    sys.exit(1) #Была возможность перезаписи файла с помощью функции yes_not(), На данный момент просто остановка работы программы
else:
    doc.save('D:/Documents/'f'{act}.docx') #Сохранение файла
    #os.startfile('D:/Documents/'f'{act}.docx', 'print') #Печать файла на принтере