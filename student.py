from tkinter import *

class Student:
    studentlist = []
    name = ''
    age = ''
    s1 = ''
    s2 = ''
    s3 = ''
    score = s1 + s2 + s3
    def __init__ (self, n, page, score):
        self.name = n
        self.age = page
        self.score = score

