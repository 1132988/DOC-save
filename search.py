import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect("trial_guarantee.db")
cursor = conn.cursor()
search_term = input("Введите критерий поиска: ")
cursor.execute("SELECT * FROM kvitanciya, priyom_ch, vozvrat_ch WHERE kvitanciya.snsrv = priyom_ch.snsrv AND priyom_ch.snsrv = vozvrat_ch.snsrv")
results = cursor.fetchall()

if not results: # Вывод результатов
    print("не найдено")
else:
    print(from_db_cursor(results))
conn.close() # Закрытие соединения