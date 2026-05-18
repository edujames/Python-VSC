from tkinter import *

raiz = Tk()

raiz.title("Mi primera ventana")

raiz.geometry("400x300")

#raiz.resizable(0,0)

raiz .config(bg="blue")

miFrame =Frame(raiz, width="300", height="125")

miFrame.pack()

miFrame.config(bg="red")

#miFrame.config(width="300", height="250")

miFrame.config(relief="sunken", bd=35)

miFrame.config(cursor="pirate")

miLabel = Label(miFrame, text="Tkinter Screen Test", fg="white", bg="black", font=("Comic Sans MS", 12, "bold"))
miLabel.place(x=40, y=10)


miGif1 = PhotoImage(file="dancing-baby-gif-90s-website-design.gif")

miGif2 = PhotoImage(file="200.gif")



miFrame2 = Frame(raiz, width="600", height="225", bg="black")
miFrame2.pack()

miFrame3 = Frame(raiz, width="600", height="225", bg="grey")
miFrame3.pack()

miLabel2 = Label(miFrame2, image=miGif1)
miLabel2.place(x=40, y=50)

miLabel3 = Label(miFrame3, image=miGif2)
miLabel3.place(x=200, y=50)

cuadroTexto = Entry(miFrame, font=("Comic Sans MS", 12))
cuadroTexto.grid(row=1, column=0, padx=10, pady=10)




raiz.mainloop()

