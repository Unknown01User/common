#1
def my_len(lst: list):
    i = 0
    for n in lst:
        i += 1
    return i

print(my_len([1,2,3]))
print(my_len([]))

#2
def my_reversed(lst: list):
    return lst[::-1]

print(my_reversed([1,2,3]))

#3
class WrongArgumentsException(Exception):
    pass

def my_range(*args):
    try:
        if (len(args) == 1):
            start = 0
            step = 1
            stop = args[0]
        elif(len(args) == 2):
            start = 0
            step = args[1]
            stop = args[0]
        elif(len(args) == 3):
            start, stop, step = args
        else:
            raise WrongArgumentsException()
        for arg in args:
            if type(arg) is not int:
                raise WrongArgumentsException()
        if (step == 0):
            raise WrongArgumentsException()

        lst = []
        i = 0
        if (step > 0):
            if (start >= stop):
                raise WrongArgumentsException()
            while (start+step * i < stop):
                lst.append(start + step * i)
                i += 1
        elif(step < 0):
            if (start <= stop):
                raise WrongArgumentsException()
            while (start+step * i > stop):
                lst.append(start + step * i )
                i += 1
        return lst
    except WrongArgumentsException:
        print("Arguments are wrong")

print(my_range(10, 2))
print(my_range(-10, -3))
print(my_range(-10, -3, 'q'))

#4
#first variant
def to_title1(line: str):
    lst = [word.capitalize() for word in line.split(' ')]
    return ("".join(el+' ' for el in lst))

print(to_title1("qwe asd zxc"))

#second variant
def to_title2(line: str):
    return line.title()

print(to_title1("qwe asd zxc"))

#5
def count_symbol(line: str, symb: str):
    lst = [ch for ch in line if ch == symb]
    return len(lst)

print(count_symbol("qweasdq", "q"))

#6

#7
from os import path

class FileExistException(Exception):
    pass

def my_copyfile(source: str, destination: str):
    try:
        if (path.isfile(destination)):
            raise FileExistException()
        with open(source, "r") as fIn:
            line = fIn.read()
        with open(destination, "w") as fOut:
            fOut.write(line)
    except FileNotFoundError:
        print("File "+source+" not found")
    except FileExistException:
        print("File " + destination + " is exist")

my_copyfile("./test1.txt", "./out.txt")
my_copyfile("./test.txt", "./out.txt")
my_copyfile("./test.txt", "./out.txt")

#8
import shutil as sh
def my_copydir(source: str, destination: str):
    try:
        dirSource = ("%r"%source)[1:-1]
        dirDest1 = ("%r"%destination)[1:-1]
        sh.copytree(dirSource, dirDest)
    except FileExistsError:
        print(dirDest+" is exist")
my_copydir(".\qwe",".\asd" )