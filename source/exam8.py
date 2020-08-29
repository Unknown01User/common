# 1
def get_len(arr : list):
    return arr.__len__()
# 2
def reversed(arr : list):
    for i in range(int(len(arr)/2)):
        tmp=arr[i]
        arr[i]=arr[(len(arr)-1)-i]
        arr[(len(arr)-1)-i]=tmp
    return arr
# 3
def my_range(*args):
    arr=[]
    if(len(args)==1):
        start = 0
        stop = args[0]
        step = 1
    if(len(args)==2):
        start = args[0]
        stop = args[1]
        step=1
    if(len(args)==3):
        start = args[0]
        stop = args[1]
        step= args[2]
        if(step==0):
            return  None
    while(abs(start)<stop):
        arr.append(start)
        start+=step
    return  arr
# 4

def to_title(str):
    arr=list(str)
    arr[0]=arr[0].upper()
    for i in range(1,len(arr)):
        if(arr[i-1]==' '):
            arr[i]=arr[i].upper()
    return  "".join(arr)
# 5
def count_symbol(str,sym):
    count=0
    for ch in str:
        if(ch==sym):
            count+=1
    return  count
# 6
def myformat(string,*args):
    str_len=len(string)
    i=0
    while(i<str_len):
        val_number=0
        if(string[i]=='{'):
            end=i
            while(string[end]!='}'):
                end+=1
            val_number=int(string[i+1:end])
            string=string[:i]+str(args[val_number])+string[end+1:]
            i=0
            str_len=len(string)
        i+=1
    return string
# 7
import os.path
def copy_file(src,dst):
    try:
        input_file = open(src)
    except FileNotFoundError:
        raise FileNotFoundError
    if(os.path.isfile(dst)):
        raise FileExistsError
    output_file= open(dst,'wb')
    with open(src,"rb") as input_file:
        byte = input_file.read(1)
        while byte:
            # Do stuff with byte.
            byte = input_file.read(1)
            output_file.write(byte)
import pathlib
import os
# 8
def copy_dir(src,dst):
    try:
        pathlib.Path(src)
    except FileNotFoundError:
        raise FileNotFoundError
    if(pathlib.Path(dst).is_dir()):
        raise FileExistsError
    os.mkdir(dst)
    for file in pathlib.Path(src).iterdir():
        if file.is_file():
            copy_file(file.absolute(),dst+'\\'+file.name)
        if file.is_dir():
            copy_dir(file.absolute(),dst+"\\"+file.name)
# 9
class User:
    name=""
    age=0
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return age
class Worker(User):
    salary=0
    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        self.salary=salary
john=Worker()
john.setAge(25)
john.setSalary(1000)
jack=Worker()
jack.setAge(26)
jack.setSalary(2000)
print("Sum of salary : "+str(john.getSalary()+jack.getSalary()))
import math
class Money:
    rub=0
    cop=0
    dollar_course=70
    def to_total(self):
        return self.rub+self.cop/100
    def from_total(self,total):
        self.rub=math.trunc(total)
        self.cop=(total-math.trunc(total))*100
    def __init__(self,rub,cop=None):
        if(cop==None):
            self.from_total(rub)
        else:
            self.rub+=rub
            self.cop+=cop
    def __str__(self):
        return str(self.rub)+","+str(self.cop)
    def __add__(self, other):
        return Money(self.to_total() +other.to_total())
    def __truediv__(self, other):
        return Money(self.to_total() / other.to_total())
    def __floordiv__(self, other):
        return Money(self.to_total() // other.to_total())
    def __sub__(self, other):
        return Money(self.to_total() - other.to_total())
    def __mul__(self, other):
        return Money(self.to_total() * other.to_total())
    def __gt__(self, other):
        return self.to_total()>other.to_total()
    def __lt__(self, other):
        return self.to_total()<other.to_total()
    def __eq__(self, other):
        return self.to_total()==other.to_total()
    def to_dollars(self):
        return self.to_total()/self.dollar_course
