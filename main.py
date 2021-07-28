import random
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk,Image

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# notes
# basic q+a, answer checking DONE
# issue somewhere after line 26
# transfer to different screens 
# add logo on screens
# add scoreboard at the end
# add usernames

# config
root = Tk()
root.title("Maths Helper")
root.geometry("400x300")
root.resizable(False,False)
root['bg'] = '#A288E3'

#Create Class
class landing:
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

            def lvlone():
                levelselection.grid_forget()
                lvlone = Frame(root)
                lvlone.grid()
                lvlone['bg'] = '#A288E3'

                Label(lvlone, text="Level one", font="fixedsys 20 bold", background='#A288E3').grid(column=1,row=1,sticky=W)

                def submt(var1):
                    if var1.get() == str(resultPLUS()):
                        correct = Label(lvlone, text="correct! hell yeah")
                        correct.place(relx=0.3, rely=0.2)
                    else:
                        wrong = Label(lvlone, text="wrong")
                        wrong.place(relx=0.3, rely=0.2)

                def try_again():
                    try_again.num1update = random.choice(num)
                    try_again.num2update = random.choice(num)
                    newQ = Label(lvlone, text=f"{try_again.num1update}+{try_again.num2update}")
                    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


                def resultPLUS():
                    try_again
                    return try_again.num1update + try_again.num2update

                lvlone.geometry("300x300")
                lvlone.resizable(False, False)
                start = Button(lvlone, text="Start",command= try_again)
                start.place(relx=0.45, rely=0.2)

                solving = Entry(lvlone)
                solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
                submit = Button(lvlone, text="Submit", command=lambda: submt(solving))
                submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
                try_again = Button(lvlone, text="Try Again", command=try_again)
                try_again.place(relx=0.39, rely=0.9)

            def lvltwo():
                levelselection.grid_forget()
                lvltwo = Frame(root)
                lvltwo.grid()
                lvltwo['bg'] = '#A288E3'

                Label(lvltwo, text="Level two", font="fixedsys 20 bold", background='#A288E3').grid(column=1,row=2,sticky=W)

            def lvlthree():
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



#config/settings
root.title("Maths Helper")


