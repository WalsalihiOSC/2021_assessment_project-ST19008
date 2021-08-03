from tkinter import * # import tkinter
from tkinter import messagebox # import messagebox
from PIL import ImageTk,Image # import imagetk
from time import * # import time
import random as rand # import random

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
            
            def lvlonee(): # LEVEL ONE (one digit addition and subtraction, worth 1 point per question)

                levelselection.grid_forget()
                lvlone = Frame(root)
                lvlone.grid()
                lvlone['bg'] = '#A288E3'
                Label(lvlone, text="Level one", font="fixedsys 20 bold", background='#A288E3').grid(column=1,row=1,sticky=W)



                global score
                score = 0
                global playcount
                playcount = 0
                while True:
                    Label(lvlone, text=f"You have answered {playcount} questions.").grid(column=2,row=7)
                    def questions():
                        global playcount
                        playcount += 1
                        a = rand.randrange(1,10,1)
                        b = rand.randrange(1,10,1)
                        def answercheck(): # check answer and give result
                            c = a + b
                            d = answer.get()
                            global score
                            d = int(d)
                            c = int(c)
                            if d == c:
                                score += 1
                                correct = Label(lvlone, text=f"Correct! You have {score} points.").grid(column=2,row=4)
                                ansubmit.grid_forget()
                                return correct
                            else: # incorrect 
                                score -= 1

                                wrong = Label(lvlone, text=f"Incorrect, the answer was {c}. You have {score} points.").grid(column=2,row=4)
                                return score
                        def submit(): # submit answer, call answercheck
                            answercheck()
                            nextquestion = Button(lvlone, text="Next Question", command=next)
                            nextquestion.grid(column=1,row=5)
                            return score
                        def next(): # next question
                            questions()

                        samplequestion = Label(lvlone, text=f'{a} + {b} =', font="fixedsys 20 bold", background='#A288E3')
                        samplequestion.grid(column=1,row=3,sticky=W)
                        answer = Entry(lvlone)
                        answer.grid(column=2,row=3)
                        ansubmit = Button(lvlone, text="Confirm", command=submit)
                        ansubmit.grid(column=1,row=4)
                        return next, score
                    questions()
                    if playcount == 5:
                        break
                    else: 
                        break 







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

            lvlone = Button(levelselection,text="Level 1", font="fixedsys",command=lvlonee)
            lvlone.grid(column=0,row=2)
            leveltwo = Button(levelselection,text="Level 2", font="fixedsys",command=lvltwo)
            leveltwo.grid(column=0,row=3)
            levelthree = Button(levelselection,text="Level 3", font="fixedsys",command=lvlthree)
            levelthree.grid(column=0,row=4)


landing()
root.mainloop()

