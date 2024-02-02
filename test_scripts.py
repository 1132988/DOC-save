import sqlite3
import re
conn = sqlite3.connect('trial_guarantee.db')
cursor = conn.cursor()
snsrv = "*********"
#Возможно правильный запрос, проверять!!!
cursor.execute("SELECT priyom_ch.act FROM priyom_ch JOIN vozvrat_ch ON priyom_ch.snsrv = vozvrat_ch.snsrv WHERE priyom_ch.snsrv = ? AND vozvrat_ch.snsrv = ?", (snsrv, snsrv))
 #Думать над этим!!!
act_p = cursor.fetchall()
act_p = re.sub(r'\D', '', str(act_p))
print(act_p)
conn.commit()
conn.close() 