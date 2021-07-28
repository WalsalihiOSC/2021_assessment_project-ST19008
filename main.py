from tkinter import * # import tkinter
from tkinter import messagebox # import messagebox
from PIL import ImageTk,Image # import imagetk
from time import * # import time
import random as rand # import random
from random import *

# config
root = Tk()
root.title("Maths Helper")
root.geometry("400x300")
root.resizable(False,False)
root['bg'] = '#A288E3'


class landing: # landing frame
    def __init__(self):
        self.landing = Frame(root)
        self.landing.grid()
        self.landing['bg'] = '#A288E3'
        a = Label(self.landing, text="Maths Helper", font="fixedsys 40 bold", background="#A288E3")
        a.grid(column=0,row=0)

        def printValue():
            pname = player_name.get()
            Label(self.landing, text=f'Welcome, {pname}!', font="fixedsys",background="#A288E3").grid(column=0,row=5)
            write=open("write.txt","a")
            write.write(f'{pname}\n')
            write.write("\n")
            write.close()
            next = Button(self.landing, text="Next", font="fixedsys",command=levelselectionbutton)
            next.grid(column=0,row=7)

        player_name = Entry(self.landing, font="fixedsys")
        player_name.grid(column=0,row=3)
        b = Label(self.landing, text="Enter your name:", font="fixedsys", background='#A288E3')
        b.grid(column=0,row=2)
        Button(self.landing, text="Next", font="fixedsys", padx=10, pady=5,command=printValue).grid(column=0,row=4)

        def levelselectionbutton():
            self.landing.grid_forget()
            levelselection = Frame(root)
            levelselection.grid()
            levelselection['bg'] = '#A288E3'
            a = Label(levelselection, text="Please choose your level!", font="fixedsys 20 bold", background='#A288E3')
            a.grid(column=0,row=0)

            def lvlone(): # LEVEL ONE (one digit addition and subtraction, worth 1 point per question)
                levelselection.grid_forget()
                lvlone = Frame(root)
                lvlone.grid()
                lvlone['bg'] = '#A288E3'
                Label(lvlone, text="Level one", font="fixedsys 20 bold", background='#A288E3').grid(column=1,row=1,sticky=W)

                num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                a = rand.randrange(1,10,1)
                b = rand.randrange(1,10,1)

                samplequestion = Label(lvlone, text=f'{a} + {b} =', font="fixedsys 20 bold", background='#A288E3')
                samplequestion.grid(column=1,row=3,sticky=W)

                answer = Entry(lvlone)
                answer.grid(column=2,row=3)

                ansubmit = Button(lvlone, text="Confirm")
                ansubmit.grid(column=1,row=4)


            def lvltwo(): # LEVEL TWO (Two digit addition and subtraction, worth 2 points per question)
                levelselection.grid_forget()
                lvltwo = Frame(root)
                lvltwo.grid()
                lvltwo['bg'] = '#A288E3'
                Label(lvltwo, text="Level two", font="fixedsys 20 bold", background='#A288E3').grid(column=1,row=2,sticky=W)

            def lvlthree(): # LEVEL THREE (One digit multiplication, worth 3 points per question)
                levelselection.grid_forget()
                lvlthree = Frame(root)
                lvlthree.grid()
                lvlthree['bg'] = '#A288E3'
                Label(lvlthree, text="Level three", font='fixedsys 20 bold', background='#A288D3').grid(column=1,row=3,sticky=W)

            lvlone = Button(levelselection,text="Level 1", font="fixedsys",command=lvlone)
            lvlone.grid(column=0,row=2)
            leveltwo = Button(levelselection,text="Level 2", font="fixedsys",command=lvltwo)
            leveltwo.grid(column=0,row=3)
            levelthree = Button(levelselection,text="Level 3", font="fixedsys",command=lvlthree)
            levelthree.grid(column=0,row=4)


landing()
root.mainloop()

