from tkinter import *
#from PIL import ImageTK, Image

h = Tk()
h.geometry("500x500")
h.title("D.A.D.O")
h.configure(background="lightyellow")

#u = ImageTk.PhotoImage(Image.open("yu.jpg"))

p1 = Label(h, text = "jugador 1", bg="forest green")
p1.place(relx= 0.1, rely = 0.3, anchor=CENTER)

p2 = Label(h, text = "jugador 2", bg="forest green")
p2.place(relx= 0.9, rely = 0.3, anchor=CENTER)

p1d = Label(h, bg="forest green")
p1d.place(relx= 0.1, rely = 0.4, anchor=CENTER)

p2d = Label(h, bg="forest green")
p2d.place(relx= 0.9, rely = 0.4, anchor=CENTER)

r = Label(h, bg="light green", fg="gray")
r.place(relx= 0.5, rely = 0.5, anchor=CENTER)

p1b = Button(h)
p1b.place(relx = 0.1, rely = 0.6, anchor = CENTER)

p1b2 = Button(h)
p1b2.place(relx = 0.9, rely = 0.6, anchor = CENTER)

h.mainloop()