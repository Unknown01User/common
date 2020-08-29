from datetime import datetime, timedelta
from subprocess import Popen, PIPE
import pickle


# Task_1
def calculate_work_days(first_date, second_date):
    date_1 = datetime.strptime(first_date, "%d.%m.%Y")
    date_2 = datetime.strptime(second_date, "%d.%m.%Y")
    period = (date_2 - date_1).days
    all_days = 0
    for i in range(period + 1):
        day = date_1 + timedelta(i)
        print(i, day)
        if day.weekday() <= 4:
            all_days += 1
    return all_days


print(calculate_work_days("24.08.2020", "30.08.2020"))


# Task_2
def read_file(file_name):
    print('{}'.format(file_name))
    proc = Popen(['type', '{}'.format(file_name)], shell=True, stdout=PIPE, stderr=PIPE)
    proc.wait()
    result = proc.communicate()
    if proc.returncode:
        print(result[1])
    return result[0]


print(read_file("f1.txt").decode("utf8"))


# Task_3
class Human:
    name = "name"
    surname = "surname"
    age = 0
    city = "city"
    profession = "profession"

    def __init__(self, name, surname, age, city, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.profession = profession

    def __repr__(self):
        return f"Human(name='{self.name}', surname='{self.surname}', age='{self.age}', city='{self.city}', profession='{self.profession}')"


names = ['Фёдор', 'Василиса', 'Марк', 'Марфа', 'Никодим']
surnames = ['Казаков', 'Белобокина', 'Шарапов', 'Собакина', 'Худобяк']
ages = [89, 78, 85, 68, 99]
cities = ['NN', 'SP', 'MSC', 'VLC', 'LIS']
professions = ['QA', 'Project Manager', 'Team Leader', 'Programmer', 'Senior programmer']


def create_people(number):
    with open('human.data', 'wb') as f:
        people = []
        for i in range(number):
            h = Human(names[i], surnames[i], ages[i], cities[i], professions[i])
            people.append(h)
        pickle.dump(people, f)


def recover_data():
    with open('human.data', 'rb') as f:
        people = pickle.load(f)
        for human in people:
            print(human)


create_people(5)
recover_data()
