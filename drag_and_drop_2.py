# Este programa (ahora sí) hace un "drag and drop" de un circulo
# This code is intended to do "drag and drop" to an circle

# if you left the circle aout of the window, press r

import tkinter as tk
import math as M

droped = "¡Agarrame!"
holding = "¡Sueltame!"
selecting = False
cursor = ()

def handler(event):
    global canvas, text, circle, cursor, selecting
    select(circle,event)
    if selecting:
        cursor = (event.x,event.y)
        if int(event.type) == 4:
            canvas.itemconfigure(
                text,
                text=holding
                )
            canvas.itemconfigure(
                circle,
                fill="#62040C",
                outline="#A20208"
            )
            some(event)
        elif int(event.type) == 5:
            canvas.itemconfigure(
                text,
                text=droped
                )
            canvas.itemconfigure(
                circle,
                fill="#0C0462",
                outline="#0802A2"
            )
            selecting = False

def some(event):
    global canvas, text, circle, selecting, cursor
    if selecting:
        dx, dy = event.x-cursor[0], event.y-cursor[1]
        cursor = (event.x, event.y)
        canvas.move(text,dx,dy)
        canvas.move(circle,dx,dy)

def reset(event):
    global canvas, circle, text, selecting
    if not selecting:
        canvas.coords(circle,100,100,500,500)
        canvas.coords(text,300,300)

def select(circle, event):
    global selecting
    x0,y0,x1,y1 = canvas.coords(circle)
    # obtain radious of circle
    radious = abs(x1-x0)//2
    # obtain center coords of circle
    cx, cy = x0+radious, y0+radious
    # obtain distance between center and cursor
    distance = M.sqrt((event.x-cx)**2+(event.y-cy)**2)
    # compare if distance is less or equal to the radious
    selecting = distance <= radious

window = tk.Tk()
window.resizable(False,False)
window.title("Arrastra y suelta (Drag and drop)")
window.bind("<KeyPress-r>", reset)
window.bind("<KeyPress-R>", reset)

canvas = tk.Canvas(window,width=600,height=600,bg="#0A0A0A")
canvas.bind("<Button-1>", handler)
canvas.bind("<B1-Motion>",some)
canvas.bind("<ButtonRelease-1>", handler)

circle = canvas.create_oval(
    100,100,
    500,500,
    fill="#0C0462",
    outline="#0802A2",
    width=3
    )

text = canvas.create_text(
    300,300,
    text=droped,
    font=("Open Sans",28,"bold"),
    fill="#F0F0F0"
    )

canvas.pack()

tk.mainloop()
