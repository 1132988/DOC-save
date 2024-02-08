import os
import configparser

install_path = (r'C:/Program Files/Python38/pythonDOCX')  # Путь, куда устанавливается программа
config_path = os.path.join(install_path, "config.ini")
os.makedirs(install_path, exist_ok=True)  # Создаем папку, если она еще не существует

kvitanciya_path = os.path.join(install_path, "Kvitanciya.py")
priyomCH_path = os.path.join(install_path, "PriyomCH.py")
priyomUR_path = os.path.join(install_path, "priyomUR.py")
vozvratCH_path = os.path.join(install_path, "vozvratCH.py")
vozvratUR_path = os.path.join(install_path, "VozvratUR.py")

config = configparser.ConfigParser()
config['Paths'] = {
    'KvitanciyaPath': kvitanciya_path,
    'PriyomCHPath': priyomCH_path,
    'PriyomURPath': priyomUR_path,
    'VozvratCHPath': vozvratCH_path,
    'VozvratURPath': vozvratUR_path
}

with open(config_path, 'w') as configfile:
    config.write(configfile)

config = configparser.ConfigParser()
config.read('config.ini')
print("Выберите программу для запуска:")
print("1. Квитанция о приёме оборудования")
print("2. Приём для частных лиц")
print("3. Приём для юридических лиц")
print("4. Возврат для частных лиц")
print("5. Возврат для Юридических лиц")
choice = input("Введите номер программы для запуска: ")
if choice == "1": 
    os.system(kvitanciya_path)
elif choice == "2":
    os.system(priyomCH_path)
elif choice == "3":
    os.system(priyomUR_path)
elif choice == "4":
    os.system(vozvratCH_path)
elif choice == "5":
    os.system(vozvratUR_path)
else:
    print("Неправильный выбор")

#Beta