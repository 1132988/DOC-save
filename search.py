#Поиск по базе данных (взяты таблицы kvitanciya и priyom_ch)
import sqlite3

from numpy import result_type
conn = sqlite3.connect('trial_guarantee.db') # Подключение к базе данных
cursor = conn.cursor() # Создание курсора для выполнения SQL-запросов

# Выполнение поискового запроса
search_term = input("Введите критерий поиска: ")
cursor.execute("SELECT kvitanciya.phone, kvitanciya.snsrv, kvitanciya.sn, priyom_ch.act, priyom_ch.sn FROM kvitanciya, priyom_ch WHERE kvitanciya.snsrv = priyom_ch.snsrv")
results = cursor.fetchall()
if not results: # Вывод результатов
    print("не найдено")
else:
    for row in results:
        print("Results: ", row)

        

conn.close() # Закрытие соединения
