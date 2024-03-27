from tkinter import *
#from PIL import ImageTk, Image
import random

h = Tk()
h.geometry("500x500")
h.title("D.A.D.O")
h.configure(background="lightyellow")



    

#u = ImageTk.PhotoImage(Image.open("yu.jpg"))

p1 = Label(h, text = "jugador 1", bg="forest green")
p1.place(relx= 0.1, rely = 0.3, anchor=CENTER)

p2 = Label(h, text = "jugador 2", bg="forest green")
p2.place(relx= 0.9, rely = 0.3, anchor=CENTER)

p1d = Label(h, bg="red", fg ="lime")
p1d.place(relx= 0.1, rely = 0.4, anchor=CENTER)

p2d = Label(h, bg="red", fg="lime")
p2d.place(relx= 0.9, rely = 0.4, anchor=CENTER)

r = Label(h, bg="light green", fg="gray")
r.place(relx= 0.5, rely = 0.5, anchor=CENTER)

p1s = 0
def pb1():
    global p1s
    ram = random.randint(1,6)
    r["text"] = "Numero del jugador1: " + str(ram)
    p1b["text"] = str(ram)
    p1s = p1s + ram
    p1d["text"] = "" + str(ram)

p2s = 0
def pb2():
    global p2s
    ram2 = random.randint(1,6)
    r["text"] = "Numero del jugador2: " + str(ram2)
    p1b2["text"] = str(ram2)
    p2s = p2s + ram2
    p2d["text"] = "" + str(ram2)

   

p1b = Button(h, command=pb1)
p1b.place(relx = 0.1, rely = 0.6, anchor = CENTER)

p1b2 = Button(h, command=pb2)
p1b2.place(relx = 0.9, rely = 0.6, anchor = CENTER)




h.mainloop()