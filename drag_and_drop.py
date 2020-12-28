# Esto es un programa que hace "drag and drop"... bueno mas o menos xD
# This code is intended to do "drag and drop" to an object (kind of)

import tkinter as tk

def handler(event):
    global canvas, text, square
    if int(event.type) == 4:
        canvas.itemconfigure(
            text,
            text=":o"
            )
        canvas.itemconfigure(
            square,
            fill="#62040C",
            outline="#A20208"
        )
        some(event)
    elif int(event.type) == 5:
        canvas.itemconfigure(
            text,
            text=";)"
            )
        canvas.itemconfigure(
            square,
            fill="#0C0462",
            outline="#0802A2"
        )

def some(event):
    global canvas, text, square
    canvas.coords(text,event.x,event.y)
    canvas.coords(square,event.x-200,event.y-200,event.x+200,event.y+200)

window = tk.Tk()
window.resizable(False,False)
window.title("Test graficos")

canvas = tk.Canvas(window,width=600,height=600,bg="#0A0A0A")
canvas.bind("<Button-1>", handler)
canvas.bind("<B1-Motion>",some)
canvas.bind("<ButtonRelease-1>", handler)

square = canvas.create_rectangle(
    100,100,
    500,500,
    fill="#0C0462",
    outline="#0802A2",
    width=3
    )

text = canvas.create_text(
    300,300,
    text=";)",
    font=("Open Sans",28,"bold"),
    fill="#F0F0F0"
    )

canvas.pack()

tk.mainloop()
