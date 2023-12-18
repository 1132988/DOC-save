#Поиск по базе данных (взяты таблицы kvitanciya и priyom_ch)
import sqlite3
# Подключение к базе данных
conn = sqlite3.connect('trial_guarantee.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Выполнение поискового запроса
search_term = input("Введите критерий поиска: ")
cursor.execute("SELECT * FROM kvitanciya JOIN priyom_ch WHERE kvitanciya.snsrv LIKE ? OR priyom_ch.act LIKE ? OR kvitanciya.phone LIKE ?", ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))

# Получение результатов поиска
results = cursor.fetchall()

# Вывод результатов
if not results:
    print("не найдено")
else:
    for row in results:
        print(row)

# Закрытие соединения
conn.close()
