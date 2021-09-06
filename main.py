from os import write
from tkinter import * # import tkinter
from tkinter import messagebox # import messagebox
from time import * # import time
import random as rand # import random
from student import Student

# config
root = Tk()
root.title("Maths Helper")
root.geometry("400x300")
root['bg'] = '#FFFFFF'

class landing: # landing frame
    def __init__(self):
        self.landing = Frame(root)
        self.landing.grid()
        self.landing['bg'] = '#FFFFFF'
        a = Label(self.landing, text="MathsHelper", font="arial 30 bold", background="#1dde8f")
        a.grid(column=0,row=0,padx=(43,0),pady=(0,90))

        Label(self.landing, text="Welcome to", font="arial 15", background="white").grid(column=0,row=0,padx=(23,0),pady=(0,170))

        def printValue():
            global pname
            pname = player_name.get()
            global page
            page = player_age.get()

            if pname == '':
                messagebox.showwarning("Error","Enter your username")
                __init__(self)
            else:
                pass

            if page == '' and int and float:
                messagebox.showwarning("Error","Enter your age")
                __init__(self)
            else:
                pass

            page = int(page)

            if page > 100:
                messagebox.showwarning("Error","Invalid Input")
                __init__(self)
            else:
                pass
            pname = Student.name
            page = Student.age

            #self.name = Student.studentlist[0]
            #self.age = Student.studentlist[1]
            #self.score1 = Student.studentlist[2]
            #self.score2 = Student.studentlist[3]
            #self.score3 = Student.studentlist[4]
            #self.student = Student(self.name, self.age, self.score1, self.score2, self.score3)

            write=open("write.txt","a")
            write.write(f'{pname}\n')
            write.write("\n")
            write.close()

            next = Button(self.landing, text="Next", font="arial",activebackground='#1dde8f', command=levelselectionbutton)
            next.grid(column=0,row=7,pady=(0,0),padx=(50,0))

        player_age = Entry(self.landing, font="arial",highlightthickness=3,highlightbackground='#1dde8f',highlightcolor='#ffd770')
        player_age.grid(column=0,row=0,pady=(80,0),padx=(50,0),ipadx=10,ipady=6)
        playerage_label = Label(self.landing, text="Enter your age:", font="arial",background='#FFFFFF')
        playerage_label.grid(column=0,row=0,pady=(50,0),padx=(50,0))

        player_name = Entry(self.landing, font="arial",highlightthickness=3,highlightbackground='#1dde8f',highlightcolor='#ffd770')
        player_name.grid(column=0,row=0,pady=(200,0),padx=(50,0),ipadx=10,ipady=6)
        b = Label(self.landing, text="Enter your username:", font="arial",background='#FFFFFF')
        b.grid(column=0,row=0,pady=(160,0),padx=(50,0))

        Button(self.landing, text="Done", font="arial",background="#FFFFFF",activebackground='#1dde8f',command=printValue).grid(column=0,row=4,padx=(60,0),pady=(10,0))
        def levelselectionbutton():
            self.landing.grid_forget()
            levelselection = Frame(root)
            levelselection.grid()
            levelselection['bg'] = '#FFFFFF'
            b = Label(levelselection,text=f'Signed in as: {pname}', font="arial 20 bold", background='#1dde8f')
            b.grid(column=0,row=0,padx=90)
            a = Label(levelselection, text="Please choose your level!", font="arial 20 bold", background='#1dde8f')
            a.grid(column=0,row=1)
            def lvlonee(): # LEVEL ONE
                levelselection.grid_forget()
                lvlone = Frame(root)
                lvlone.grid()
                lvlone['bg'] = '#FFFFFF'
                Label(lvlone, text="Level one: Addition", font="arial 20 bold", background='#FFFFFF').grid(column=1,row=1,sticky=W,pady=(0,50))
                global score
                score = 0
                global playcount
                playcount = 0
                while True:
                    playcount += 1
                    def questions():
                        a = rand.randrange(1,20,1)
                        b = rand.randrange(1,20,1)
                        def answercheck(): # check answer and give result

                            c = a + b
                            d = answer.get()
                            global score
                            if d == '':
                                messagebox.showwarning("Error","Enter your answer")
                                questions
                            else:
                                pass
                            d = int(d)
                            c = int(c)


                            if d == c:
                                score += 1
                                correct = Label(lvlone, text=f"Correct! You have {score} points.").grid(column=1,row=1,sticky=W)
                                ansubmit.grid_forget()
                                return correct, score
                            else: # incorrect 
                                score -= 1
                                Label(lvlone, text=f"Incorrect, You have {score} points.").grid(column=1,row=1,sticky=W)
                                return score
                        def submit(): # submit answer, call answercheck
                            answercheck()
                            ansubmit.grid_forget()
                            nextquestion = Button(lvlone, text="Next Question", width=10,height=2, command=next)
                            nextquestion.grid(column=1,row=5,sticky=W)
                            return score
                        def next(): # next question
                            questions()
                            samplequestion.grid_forget()
                            return score
                        samplequestion = Label(lvlone, text=f'{a} + {b} =', font="arial 22 bold", background='#1dde8f')
                        samplequestion.grid(column=1,row=3,sticky=W)
                        answer = Entry(lvlone, highlightthickness=3,highlightbackground='#1dde8f',highlightcolor='#ffd770')
                        answer.grid(column=2,row=3,ipadx=10,ipady=6,padx=(10,0))
                        
                        ansubmit = Button(lvlone, text="Confirm", width=10,height=2, command=submit)
                        ansubmit.grid(column=1,row=4,sticky=W)
                        return score
                    questions()
                    def backlvlone():
                        score = Student.s1
                        write=open("write.txt","a")
                        write.write(f'Level one: {score}\n')
                        write.write("\n")
                        write.close()
                        levelselectionbutton()
                        lvlone.grid_forget()
                    claimscorebtn = Button(lvlone, text="Return to level selection", command=backlvlone)
                    claimscorebtn.grid(column=2,row=10)
                    if playcount == 5:
                        break
                    else: 
                        break 
            def lvltwo(): # LEVEL TWO
                levelselection.grid_forget()
                lvltwo = Frame(root)
                lvltwo.grid()
                lvltwo['bg'] = '#FFFFFF'
                Label(lvltwo, text="Level two: Multiplication", font="arial 20 bold", background='#FFFFFF').grid(column=1,row=1,sticky=W,pady=(0,50))
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
                            c = a * b
                            d = answer.get()
                            global score
                            if d == '':
                                messagebox.showwarning("Error","Enter your answer")
                                questions
                            else:
                                pass
                            d = int(d)
                            c = int(c)
                            if d == c:
                                score += 1
                                correct = Label(lvltwo, text=f"Correct! You have {score} points.").grid(column=1,row=1,sticky=W)
                                ansubmit.grid_forget()
                                return correct, score
                            else: # incorrect 
                                score -= 1
                                Label(lvltwo, text=f"Incorrect, You have {score} points.").grid(column=1,row=1,sticky=W)
                                return score
                        def submit(): # submit answer, call answercheck
                            answercheck()
                            ansubmit.grid_forget()
                            nextquestion = Button(lvltwo, text="Next Question", width=10,height=2, command=next)
                            nextquestion.grid(column=1,row=5,sticky=W)
                            return score
                        def next(): # next question
                            questions()
                            samplequestion.grid_forget()
                            return score
                        samplequestion = Label(lvltwo, text=f'{a} x {b} =', font="arial 22 bold", background='#1dde8f')
                        samplequestion.grid(column=1,row=3,sticky=W)
                        answer = Entry(lvltwo, highlightthickness=3,highlightbackground='#1dde8f',highlightcolor='#ffd770')
                        answer.grid(column=2,row=3,ipadx=10,ipady=6,padx=(10,0))
                        ansubmit = Button(lvltwo, text="Confirm", width=10,height=2, command=submit)
                        ansubmit.grid(column=1,row=4,sticky=W)
                        return score
                    questions()
                    def backlvltwo():
                        score = Student.s2
                        write=open("write.txt","a")
                        write.write(f'Level two: {score}\n')
                        write.write("\n")
                        write.close()
                        levelselectionbutton()
                        lvltwo.grid_forget()
                    claimscorebtn = Button(lvltwo, text="Return to level selection", command=backlvltwo)
                    claimscorebtn.grid(column=2,row=10)
                    if playcount == 5:
                        break
                    else: 
                        break             
            def lvlthree(): # LEVEL THREE
                levelselection.grid_forget()
                lvlthree = Frame(root)
                lvlthree.grid()
                lvlthree['bg'] = '#FFFFFF'
                Label(lvlthree, text="Level three: Division", font="arial 20 bold", background='#FFFFFF').grid(column=1,row=1,sticky=W,pady=(0,50))
                global score
                score = 0
                global playcount
                playcount = 0
                while True:
                    playcount += 1
                    def questions():
                        a = rand.randrange(1,20,1)
                        b = rand.randrange(1,5,1)
                        def answercheck(): # check answer and give result
                            c = a / b
                            d = answer.get()
                            global score
                            if d == '':
                                messagebox.showwarning("Error","Enter your answer")
                                questions
                            else:
                                pass
                            d = int(d)
                            c = int(c)
                            if d == c:
                                score += 1
                                correct = Label(lvlthree, text=f"Correct! You have {score} points.").grid(column=1,row=1,sticky=W)
                                ansubmit.grid_forget()
                                return correct, score
                            else: # incorrect 
                                score -= 1
                                Label(lvlthree, text=f"Incorrect, You have {score} points.").grid(column=1,row=1,sticky=W)
                                return score
                        def submit(): # submit answer, call answercheck
                            answercheck()
                            ansubmit.grid_forget()
                            nextquestion = Button(lvlthree, text="Next Question", width=10,height=2, command=next)
                            nextquestion.grid(column=1,row=5,sticky=W)
                            return score
                        def next(): # next question
                            questions()
                            samplequestion.grid_forget()
                            return score
                        samplequestion = Label(lvlthree, text=f'{a} ÷ {b} =', font="arial 22 bold", background='#1dde8f')
                        samplequestion.grid(column=1,row=3,sticky=W)
                        answer = Entry(lvlthree, highlightthickness=3,highlightbackground='#1dde8f',highlightcolor='#ffd770')
                        answer.grid(column=2,row=3,ipadx=10,ipady=6,padx=(10,0))
                        ansubmit = Button(lvlthree, text="Confirm", width=10,height=2, command=submit)
                        ansubmit.grid(column=1,row=4,sticky=W)
                        return score
                    questions()
                    def backlvlthree():
                        score = Student.s3
                        write=open("write.txt","a")
                        write.write(f'Level one: {score}\n')
                        write.write("\n")
                        write.close()
                        levelselectionbutton()
                        lvlthree.grid_forget()
                    claimscorebtn = Button(lvlthree, text="Return to level selection", command=backlvlthree)
                    claimscorebtn.grid(column=2,row=10)                    
                    if playcount == 5:
                        break
                    else: 
                        break 
            lvlone = Button(levelselection,text="Level 1", font="arial", activebackground='#1dde8f', command=lvlonee)
            lvlone.grid(column=0,row=2,pady=(10,0))
            leveltwo = Button(levelselection,text="Level 2", font="arial", activebackground='#1dde8f', command=lvltwo)
            leveltwo.grid(column=0,row=3,pady=(10,0))
            levelthree = Button(levelselection,text="Level 3", font="arial", activebackground='#1dde8f', command=lvlthree)
            levelthree.grid(column=0,row=4,pady=(10,0))
            def newuser():
                write=open("write.txt","a")
                write.write(f'********************************')
                write.write("\n")
                write.close()
                levelselection.grid_forget()
                landing()
                root.mainloop()
            newuserbtn = Button(levelselection, text="New User", font="arial", command=newuser)
            newuserbtn.grid(column=0,row=10,pady=(60,0))
            def save():
                write=open("write.txt","a")
                write.write(f'********************************')
                write.write("\n")
                write.close()
                root.destroy()
            savebtn = Button(levelselection, text="Save and exit", font="arial", command=save)
            savebtn.grid(column=0,row=11,pady=10)
landing()
root.mainloop()

