from os import name
import random as rand
from tkinter import messagebox


class Student:
    tries = 0
    score = 0


    def __init__ (self, pname, page, score):
        self.name = pname
        self.age = page
        self.score = score

    def difficulty(self):
        range1 = range(1,8)
        range2 = range(9,16)
        if self.age in range1:
            randnum = 10
        elif self.age in range2:
            randnum = 20
        else:
            randnum = 30
        return randnum