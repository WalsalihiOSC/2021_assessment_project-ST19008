import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

app = Tk()
app.title("math thing")

app.geometry("300x300")
start = Button(app, text="Start", command=try_again)
