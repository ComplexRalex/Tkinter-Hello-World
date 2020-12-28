import tkinter as tk

def handler(event):
    global canvas, text
    if int(event.type) == 4:
        canvas.itemconfigure(text, text="Hello world!")
    elif int(event.type) == 5:
        canvas.itemconfigure(text, text="¡Hola mundo!")

window = tk.Tk()
window.resizable(False,False)
window.title("Test graficos")

canvas = tk.Canvas(window,width=600,height=600,bg="#0A0A0A")
canvas.bind("<Button-1>", handler)
canvas.bind("<ButtonRelease-1>", handler)

circle = canvas.create_oval(
    100,100,
    500,500,
    fill="#101010",
    activefill="#0A0260",
    outline="#202020",
    activeoutline="#0600A0",
    width=3,
    activewidth=9
    )

text = canvas.create_text(
    300,300,
    text="¡Hola mundo!",
    font=("Open Sans",28,"bold"),
    fill="#808080",
    activefill="#F0F0F0"
    )

canvas.pack()

tk.mainloop()
