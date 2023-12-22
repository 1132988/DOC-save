#Сбор акта из другой таблицы БД, и его обработка.


import sqlite3
import re
conn = sqlite3.connect('trial_guarantee.db')
cursor = conn.cursor()
cursor.execute("SELECT priyom_ch.act FROM priyom_ch JOIN vozvrat_ch ON priyom_ch.snsrv = vozvrat_ch.snsrv") #Думать над этим!!!
act_p = cursor.fetchall()
act_p = re.sub("[(|,|)]","", str(act_p[1])) #Избавляемся от повторения, а также от других знаков
print(act_p)