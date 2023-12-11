import os
print("Выберите программу для запуска:")
print("1. Квитанция о приёме оборудования")
print("2. Приём для частных лиц")
print("3. Приём для юридических лиц")
print("4. Возврат для частных лиц")
print("5. Возврат для Юридических лиц")
choice = input("Введите номер программы для запуска: ")

if choice == "1":
    os.system('Kvitanciya.py')
elif choice == "2":
    os.system('PriyomCH.py')
elif choice == "3":
    os.system('priyomUR.py')
elif choice == "4":
    os.system('vozvratCH.py')
elif choice == "5":
    os.system('VozvratUR.py')
else:
    print("Неправильный выбор")
    
input()
