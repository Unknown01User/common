def analyze_numbers_and_print_FizzBuzz():
    for i in range(0, 101):
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        if i % 15 == 0:
            print(i)
            print("FizzBuzz")


analyze_numbers_and_print_FizzBuzz()


def read_number_and_print_digit_by_digit(number):
    if len(number) != 5:
        print("The number must includes 5 digits! Please, try again!")
        return
    for index, item in enumerate(number):
        print("{} цифра равна {}".format(index+1, item))
    print("And from the end to the beginning!")
    for index, item in enumerate(number[::-1]):
        print("{} цифра равна {}".format(index+1, item))


read_number_and_print_digit_by_digit("12345")
read_number_and_print_digit_by_digit("123")


def sorting_by_choice(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)


array1 = [100, 2222222, 85, 789, 1, 1258, 1478952, 15, 58, 1, 65, 69, 78, 52, 2563, 1, 0, 3, 24, 2, 3, 7]
sorting_by_choice(array1)


def change_tab_for_whitespace(file_name, to_spaces=True):
    tab = "\t"
    whitespaces = "    "
    with open(file_name, "r+") as file_for_read:
        buffer = file_for_read.read()
        if to_spaces:
            buffer = buffer.replace(tab, whitespaces)
        else:
            buffer = buffer.replace(whitespaces, tab)
        with open("file1.txt", "wt") as file_for_rewrite:
            file_for_rewrite.write(buffer)


change_tab_for_whitespace("forRead.txt", to_spaces=True)


def replace_with_a_template(str, dictionary):
    list = str.split(" ")
    for word in list:
        if word in dictionary:
            str = str.replace(word, dictionary[word])
    return str


string123 = "Py is one of OOP language. There are 3 principles of OOP wich includes E and I and P."
dictionary1 = {'OOP': 'object oriented programming', 'Py': 'Python', 'E': 'Encapsulation',
                  'I': 'Inheritance', 'P.': 'Polymorphism.'}
print(replace_with_a_template(string123, dictionary1))