import time
import random
import os


class Man:
    name = "name"

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


    @classmethod
    def solve_task(cls):
        print("I`m not ready!")


class Pupil(Man):

    @classmethod
    def solve_task(cls):
        print("Pupil is thinking...")
        random_time = random.randint(3, 6)
        print(random_time)
        time.sleep(random_time)
        print("I`m not ready!")



class WrapStrToFile(object):

    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def content(self):
        if (not self.file_path):
            print("File doesn`t exist!")
        with open(self.file_path, "r+") as file_for_read:
            buffer = file_for_read.read()
            print(buffer)

    @content.setter
    def content(self, value):
        with open(self.file_path, "a") as file_for_rewrite:
            file_for_rewrite.write(value)


    @content.deleter
    def content(self):
        os.remove(self.file_path)



w = WrapStrToFile("Read.txt")
w.content
string = "Python is one of object oriented programming language. There are 3 principles of object oriented programming wich includes " \
      "Encapsulation and Inheritance and Polymorphism."

w.content = string
del w.content