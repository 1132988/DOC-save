#Visual
import PySimpleGUI as sg
import os
layout = [
    [sg.Text('Выберите программу для запуска:')],
    [sg.Text('1. Квитанция о приёме оборудования'), sg.Button("Кнопка 1")],
    [sg.Text('2. Приём для частных лиц'), sg.Button("Кнопка 2")],
    [sg.Text('3. Приём для юридических лиц'), sg.Button("Кнопка 3")],
    [sg.Text('4. Возврат для частных лиц'), sg.Button("Кнопка 4")],
    [sg.Text('5. Возврат для Юридических лиц'), sg.Button("Кнопка 5")],
    
    [sg.Cancel("Закрыть")]
]
window = sg.Window('PyDocx_V0.3', layout)

while True:
    event, values = window.read()
    print(event, values) #debug
    if event in (None, 'Кнопка 1'):
        os.system("Kvitanciya.py")
    elif event in (None, 'Кнопка 2'):
        os.system("PriyomCH.py")
    elif event in (None, 'Кнопка 3'):
        os.system("priyomUR.py")
    elif event in (None, 'Кнопка 4'):
        os.system("vozvratCH.py")
    elif event in (None, 'Кнопка 5'):
        os.system("VozvratUR.py")
    elif event in (None, 'Exit', 'Закрыть'):
        break
        
