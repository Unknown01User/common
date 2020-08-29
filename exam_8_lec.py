from itertools import zip_longest


# Task 1
def get_len(the_list):
    count = 0
    for i in the_list:
        count += 1
    return count


li = [1, 2, 3]
print("#Task 1:", get_len(li))


# Task 2
def my_revrsed(the_list):
    i = 0
    j = len(the_list) - 1
    while i < j:
        the_list[i], the_list[j] = the_list[j], the_list[i]
        i += 1
        j -= 1
    return the_list


li_1 = [1, 2, 3, 5, 8, 9]
print("#Task 2:", my_revrsed(li_1))


# Task 3
def my_range(*args):
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
    i = start
    if step < 0:
        while i > stop:
            yield i
            i += step
    else:
        while i < stop:
            yield i
            i += step


print("#Task 3:", list(my_range(8, 5, -1)))


# Task 4
def to_title(string):
    list_1 = string.split(" ")
    list_2 = []
    for i in list_1:
        if i:
            list_2.append(i.replace(i[0], i[0].upper()))
    return " ".join(list_2)


print("#Task 4:", to_title("python python  python"))


# Task 5
def count_symbol(string, symbol):
    count = 0
    for i in string:
        if symbol == i:
            count += 1
    return count


print("#Task 5:", count_symbol("python python  python", "p"))

# Extra Task2
""" 
x = [[1, 2, 3, 4]]*3 - создаст 3 элемента листа, которые будут ссылаться на 1 и тот же экземпляр листа [1, 2, 3, 4], 
отсюда проблема - при изменении x[0] изменятся также остальные
 y = [[1, 2, 3, 4] for _ in range(3)] - создаст 3 разных экземпляра листа, изменения y[0] не повлияет на другие
"""


# Extra Task3
class Counter:
    _COUNT = 0

    def __init__(self):
        Counter._COUNT += 1

    @classmethod
    def get_instances_number(cls):
        return cls._COUNT


c = Counter()
b = Counter()
print("#Extra Task3:", c.get_instances_number())


# Extra Task4
def make_dict(key_list, value_list):
    my_dict = {}
    my_zip = zip
    if len(key_list) > len(value_list):
        my_zip = zip_longest
    for key, value in my_zip(key_list, value_list):
        my_dict[key] = value
    return my_dict

print("#Extra Task4:",make_dict([1,2,3], ["one", "two", "three"]))
print("#Extra Task4:",make_dict([1,2,3], ["one", "two"]))
print("#Extra Task4:",make_dict([1,2], ["one", "two", "three"]))


#Task 9
class User():
    name = "name"
    age = 0

    def __init__(self, name, age):
        self.name = name

    def set_name(self, name):
        self.name = name
        self.age = age


    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

class Woker(User):
    salary = 0

    def __init__(self, name, age, salary):
        super(Woker, self).__init__(name, age)
        self.salary = salary


    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


Jonh = Woker('Jonh', 25, 1000)
Jack = Woker('Jack', 26, 2000)
sum_salary = Jonh.get_salary() + Jack.get_salary()
print("Task 9:",sum_salary)
