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
1

class landing: # landing frame
    def __init__(self):
        self.landing = Frame(root)
        self.landing.grid()
        self.landing['bg'] = '#A288E3'
        a = Label(self.landing, text="Maths Helper", font="fixedsys 40 bold", background="#A288E3")
        a.grid(column=0,row=0)

        def printValue():

            global pname
            pname = player_name.get()
            if pname == '':
                messagebox.showwarning("Error","Enter your username")
                __init__(self)
            else:
                pass
            Label(self.landing, text=f'Welcome, {pname}!', font="fixedsys",background="#A288E3").grid(column=0,row=5)
            write=open("write.txt","a")
            write.write(f'{pname}\n')
            write.write("\n")
            write.close()
            next = Button(self.landing, text="Next", font="fixedsys",command=levelselectionbutton)
            next.grid(column=0,row=7)

        player_name = Entry(self.landing, font="fixedsys")
        player_name.grid(column=0,row=3)

        b = Label(self.landing, text="Enter your username:", font="fixedsys", background='#A288E3')
        b.grid(column=0,row=2)
        
        Button(self.landing, text="Next", font="fixedsys", padx=10, pady=5,command=printValue).grid(column=0,row=4)

        def levelselectionbutton():
            self.landing.grid_forget()
            levelselection = Frame(root)
            levelselection.grid()
            levelselection['bg'] = '#A288E3'
            b = Label(levelselection,text=f'Welcome {pname}!', font="fixedsys 20 bold", background='#A288E3')
            b.grid(column=0,row=0)
            a = Label(levelselection, text="Please choose your level!", font="fixedsys 20 bold", background='#A288E3')
            a.grid(column=0,row=1)
            
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
                    
                    playcount += 1
                    def questions():
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
                                return correct, score
                            else: # incorrect 
                                score -= 1
                                Label(lvlone, text=f"Incorrect, You have {score} points.").grid(column=2,row=4)
                                return score
                        def submit(): # submit answer, call answercheck
                            answercheck()
                            ansubmit.grid_forget()
                            nextquestion = Button(lvlone, text="Next Question", command=next)
                            nextquestion.grid(column=1,row=5)
                            return score
                        def next(): # next question
                            questions()
                            return score

                        samplequestion = Label(lvlone, text=f'{a} + {b} =', font="fixedsys 20 bold", background='#A288E3')
                        samplequestion.grid(column=1,row=3,sticky=W)
                        answer = Entry(lvlone)
                        answer.grid(column=2,row=3)
                        ansubmit = Button(lvlone, text="Confirm", command=submit)
                        ansubmit.grid(column=1,row=4)
                        return score
                    
                    
                    questions()
                    def backlvlone():
                        levelselectionbutton()
                        lvlone.grid_forget()
                    claimscorebtn = Button(lvlone, text="Return to level selection", command=backlvlone)
                    claimscorebtn.grid(column=20,row=10)

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

                global score
                score = 0
                global playcount
                playcount = 0
                def questions():
                    a = rand.randrange(1,20,1)
                    b = rand.randrange(1,5,1)
                    def answercheck(): # check answer and give result
                        c = a * b
                        d = answer.get()
                        global score
                        d = int(d)
                        c = int(c)
                        if d == c:
                            score += 1
                            correct = Label(lvltwo, text=f"Correct! You have {score} points.").grid(column=2,row=4)
                            ansubmit.grid_forget()
                            return correct, score
                        else: # incorrect 
                            score -= 1
                            Label(lvltwo, text=f"Incorrect, You have {score} points.").grid(column=2,row=4)
                            return score
                    def submit(): # submit answer, call answercheck
                        answercheck()
                        ansubmit.grid_forget()
                        nextquestion = Button(lvltwo, text="Next Question", command=next)
                        nextquestion.grid(column=1,row=5)
                        return score
                    def next(): # next question
                        questions()
                        return score
                    samplequestion = Label(lvltwo, text=f'{a} x {b} =', font="fixedsys 20 bold", background='#A288E3')
                    samplequestion.grid(column=1,row=3,sticky=W)
                    answer = Entry(lvltwo)
                    answer.grid(column=2,row=3)
                    ansubmit = Button(lvltwo, text="Confirm", command=submit)
                    ansubmit.grid(column=1,row=4)
                    return score
                questions()
                def backlvltwo():
                    levelselectionbutton()
                    lvltwo.grid_forget()
                claimscorebtn = Button(lvltwo, text="Return to level selection", command=backlvltwo)
                claimscorebtn.grid(column=20,row=10)

            def lvlthree(): # LEVEL THREE (One digit multiplication, worth 3 points per question)
                levelselection.grid_forget()
                lvlthree = Frame(root)
                lvlthree.grid()
                lvlthree['bg'] = '#A288E3'
                Label(lvlthree, text="Level three", font='fixedsys 20 bold', background='#A288D3').grid(column=1,row=2,sticky=W)

                global score
                score = 0
                global playcount
                playcount = 0
                def questions():
                    a = rand.randrange(1,10,1)
                    b = rand.randrange(1,10,1)
                    def answercheck(): # check answer and give result
                        c = a / b
                        d = answer.get()
                        global score
                        d = int(d)
                        c = int(c)
                        if d == c:
                            score += 1
                            correct = Label(lvlthree, text=f"Correct! You have {score} points.").grid(column=2,row=4)
                            ansubmit.grid_forget()
                            return correct, score
                        else: # incorrect 
                            score -= 1
                            Label(lvlthree, text=f"Incorrect, You have {score} points.").grid(column=2,row=4)
                            return score
                    def submit(): # submit answer, call answercheck
                        answercheck()
                        ansubmit.grid_forget()
                        nextquestion = Button(lvlthree, text="Next Question", command=next)
                        nextquestion.grid(column=1,row=5)
                        return score
                    def next(): # next question
                        questions()
                        return score
                    samplequestion = Label(lvlthree, text=f'{a} ÷ {b} =', font="fixedsys 20 bold", background='#A288E3')
                    samplequestion.grid(column=1,row=3,sticky=W)
                    answer = Entry(lvlthree)
                    answer.grid(column=2,row=3)
                    ansubmit = Button(lvlthree, text="Confirm", command=submit)
                    ansubmit.grid(column=1,row=4)
                    return score
                questions()
                def backlvlthree():
                    levelselectionbutton()
                    lvlthree.grid_forget()
                claimscorebtn = Button(lvlthree, text="Return to level selection", command=backlvlthree)
                claimscorebtn.grid(column=20,row=10)

            lvlone = Button(levelselection,text="Level 1", font="fixedsys",command=lvlonee)
            lvlone.grid(column=0,row=2)
            leveltwo = Button(levelselection,text="Level 2", font="fixedsys",command=lvltwo)
            leveltwo.grid(column=0,row=3)
            levelthree = Button(levelselection,text="Level 3", font="fixedsys",command=lvlthree)
            levelthree.grid(column=0,row=4)


landing()
root.mainloop()

