from tkinter import *


root = Tk()
def btn_click():
    login = loginInput.get()
    password = passField.get()
    info_str = f'dannie:{str(login)}, {str(password)}'
    messagebox.showinfo(title='Nazvaniya', message='info_str')

#root['bg'] = '#fafafa'
root.title('Парсинг из СС')

root.geometry('300x250')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()
frame = Frame(root, bg='red')
frame.place( relx=0.15, rely=0.15,  relwidth=0.7, relheight=0.7)

title = Label(frame, text='tekst podskazka', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Ok', bg='yellow')
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()



root.mainloop()
