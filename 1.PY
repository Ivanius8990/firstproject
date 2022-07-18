from tkinter import *
def clicked():
    lbl.configure(text="Кнопка нажата!!")
window = Tk()
window.title("Добро пожаловать!")
window.geometry('350x200')
lbl = Label(window, text="Привет!")
lbl.grid(column=0, row=0)
btn = Button(window, text="Нажми меня", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
