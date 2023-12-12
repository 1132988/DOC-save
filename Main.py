import os
print("Выберите программу для запуска:")
print("1. Квитанция о приёме оборудования")
print("2. Приём для частных лиц")
print("3. Приём для юридических лиц")
print("4. Возврат для частных лиц")
print("5. Возврат для Юридических лиц")
choice = input("Введите номер программы для запуска: ")

if choice == "1": 
    os.system(r'C:\"Program Files"\Python38\pythonDOCX\Kvitanciya.py')
elif choice == "2":
    os.system(r'C:\"Program Files"\Python38\pythonDOCX\PriyomCH.py')
elif choice == "3":
    os.system(r'C:\"Program Files"\Python38\pythonDOCX\priyomUR.py')
elif choice == "4":
    os.system(r'C:\"Program Files"\Python38\pythonDOCX\vozvratCH.py')
elif choice == "5":
    os.system(r'C:\"Program Files"\Python38\pythonDOCX\VozvratUR.py')
else:
    print("Неправильный выбор")
