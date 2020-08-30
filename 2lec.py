# принимает 2 числа и выводит большее

def max_number(a, b):
    if a > b:
        c = a
    else:
        c = b
    print("Большее число: {}".format(c))
x = int(input("Введите число а: \n"))
y = int(input("Введите число b: \n"))
max_number(x, y)

# принимает 2 числа и возвращает большее

def max_return (a, b):
    c = a if(a < b) else b
    return c

x = int(input("Введите число а: \n"))
y = int(input("Введите число b: \n"))
max_number(x, y)
