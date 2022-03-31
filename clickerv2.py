import tkinter
from tokenize import Number
from turtle import back, width
window = tkinter.Tk()

window.title('ClickerV2')
window.geometry('300x300')
window.resizable(0,0)
nummer = 0
def update ():
    if nummer < 0 :
        window.config(background='red')
    if nummer > 0 :
        window.config(background='green')
    if nummer == 0 :
        window.config(background='grey')

def up():
    global nummer
    nummer += 1
    window.update()
    box1.configure(text=nummer)
    update()

def down():
    global nummer
    nummer -= 1
    window.update()
    box1.update()
    box1.configure(text=nummer)
    update()



window.configure(background='grey')
buttonUp = tkinter.Button(window,width=35, height=3,command=up,)
buttonUp.pack(
    pady=(30, 0)
)
buttonUp.configure(text='UP')

box1 = tkinter.Label(
    window,
    width=35,height=3,
    text=(nummer),
    bg="white",
    fg="black"
)
box1.pack(
  pady=25
)

buttonDown = tkinter.Button(window,width=35, height=3,command=down)
buttonDown.pack()
buttonDown.configure(text='down')

window.mainloop()