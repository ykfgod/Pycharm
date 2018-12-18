from tkinter import *
root = Tk()
root.title("«Transposition»")
root.wm_attributes("-topmost", True)
root.geometry('525x190')
root.resizable(width=False, height=False)
errordata="Введите строку!"

def main():
    text = line.get()
    a2 = ""
    i = 0
    if (line.get() == ""):
        restext.config(text=errordata)
    elif len(text) % 2 == 0:
        while i <= len(text) - 1:
            k = text[i]
            a2 = a2[:] + text[i+1] + k
            i=i+2
        restext.config(text=a2)
    else:
        sym = text[len(text)-1]
        text = text[:len(text)-1]
        while i <= len(text) - 1:
            k = text[i]
            a2 = a2[:] + text[i+1] + k
            i=i+2
        restext.config(text = a2[:] + sym)

#clear line
def clear():
    line.delete(0, 'end')
    restext.config(text="Тут будет ваша \nстрока!")
    line.focus_set()

#line label
label1= Label(root,
              text="Введите строку",
              font = "Verdana 10 bold",
              fg = "#555",
              compound=LEFT,
              )
label1.place(x=20, y=20)

#line enter
line = Entry(root,width=80)
line.place(x=20, y=45)
line.focus_set()

#butt count
actionbut = Button(root,
           text = "Зашифровать",
           width = 10,
           background="#555",
           foreground="#ccc",
           command = main)
actionbut.place(x=20, y=130)

#butt clear
clearbut = Button(root,
           text = "Отчистить",
           width = 10,
           background="#555",
           foreground="#ccc",
           command = clear)
clearbut.place(x=130, y=130)

#result label
labelres= Label(root,
              text="Зашифрованая строка: ",
              font="sans-serif 10 bold",
              fg="#555",
              compound=LEFT
              )
labelres.place(x=340, y=80)
restext= Label(root,
              text="Тут будет ваша \nстрока!",
              font="sans-serif 10",
              fg="#555",
               justify=LEFT
              )
restext.place(x=400, y=105)

root.mainloop()