"""
«Игра в «крестики-нолики». Для двух участников. Поле размером не менее 40х40.
Компьютер определяет наличие пяти одинаковых символов в линию
"""
from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('Курсовая работа Богданов М. 19-ИЭ-1')

work = True
arr = []
count = 0
turn = 0

#Функция главного меню с информацией об авторе работы
def autor():
    messagebox.showinfo(title="Автор", message="Работу выполнил студент\n2 курса группы 19-ИЭ-1\nБогданов Максим Дмитриевич")

#Функция перезапуска игры
def restart():
    global count
    count = 0
    global work
    work = True
    
    for row in range(40):
        for col in range(40):
            arr[row][col]['text'] = ' '
            arr[row][col]['background'] = 'lavender'
    
#Функция, вызываемая нажатием на кнопку, определяет текущий ход и запускает проверку победы
def click(row, col):
    global turn, count
    if count % 2 == 0:
        turn = 0
    else: turn = 1
    
    if turn == 1:
        if work and arr[row][col]['text'] == ' ':
            arr[row][col]['text'] = 'X'
            count += 1
            win_check('X')
            
    if turn == 0:
        if work and arr[row][col]['text'] == ' ':
            arr[row][col]['text'] = 'O'
            count += 1
            win_check('O')


#Проверяется каждое возможное выигрышное состояние из 5 клеток
def win_check(symbol):
    for i in range(36):
        for n in range(40):
            line_check(arr[n][i], arr[n][i+1], arr[n][i+2], arr[n][i+3], arr[n][i+4], symbol) #проверка горизонтали
            line_check(arr[i][n], arr[i+1][n], arr[i+2][n], arr[i+3][n], arr[i+4][n], symbol) #проверка вертикали

    for i in range(36):
        for n in range(36):
            line_check(arr[n][i], arr[n+1][i+1], arr[n+2][i+2], arr[n+3][i+3], arr[n+4][i+4], symbol) #проверка косой верх лево
            line_check(arr[i][n+4], arr[i+1][n+3], arr[i+2][n+2], arr[i+3][n+1], arr[i+4][n], symbol) #проверка косой верх право


#Проверяется одинаковость символов в линии и в этом случае выделяет выигрышную комбинацию на поле
def line_check(a1,a2,a3,a4,a5,symbol):
    if a1['text'] == symbol and a2['text'] == symbol and a3['text'] == symbol and a4['text'] == symbol and a5['text'] == symbol:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = a5['background'] = 'pink'
        global work
        work = False
     
#Построение поля 40 на 40
for row in range(40):
    line = []
    for col in range(40):
        button = Button(root, text=' ', width=2, height=1, 
                        font=('Verdana 8 bold'), background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    arr.append(line)

newButton = Button(root, text='Новая игра', command=restart)
newButton.grid(row=40, column=0, columnspan=40, sticky='nsew')

mainMenu = Menu( root )
root.config(menu = mainMenu)

mainMenu.add_command(label = "Сведения об авторе", command = autor)

root.mainloop()
