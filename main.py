import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

app = Tk()
app.title("math thing")

def try_again():
   try_again.1=random.choice(num)
   try_again.2 = random.choice(num)
   thing=label(app, text="test")
    
# def submit?

# def result

app.geometry("300x300")
start = Button(app, text="Start", command=try_again)
start.place(relx=0.5, rely=1)
