import random
from tkinter import *
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
root.geometry("300x300")
root.resizable(False,False)

#Create Class
class landing:
    def __init__(self):
        self.landing = Frame(root)
        self.landing.grid()

        mylabel = Label(self.landing, text="Maths Helper").grid(column=1,row=1,sticky=W)
        username = Entry(self.landing, text="Username: ").grid(column=2,row=2,sticky=W)
        Label(self.)

landing()
root.mainloop()

def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="correct! hell yeah")
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(app, text="wrong")
        wrong.place(relx=0.3, rely=0.2)

# question + try again
def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(app, text=f"{try_again.num1update}+{try_again.num2update}")
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update

#app.geometry("300x300")
#app.resizable(False, False)
#start = Button(app, text="Start",command= try_again)
#start.place(relx=0.45, rely=0.2)

#solving = Entry(app)
#solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
#submit = Button(app, text="Submit", command=lambda: submt(solving))
#submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
#try_again = Button(app, text="Try Again", command=try_again)
#try_again.place(relx=0.39, rely=0.9)

# config/settings
#root.title("Maths Helper")


