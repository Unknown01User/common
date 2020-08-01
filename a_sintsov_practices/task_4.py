# 1
def fizzBuzz():
    line = ""
    fizz = "Fizz"
    buzz = "Buzz"
    for i in range(1, 100):
        if (i % 3 == 0 and i % 5 == 0):
            line = line.replace(line, fizz + buzz)
        elif (i % 3 == 0):
            line = line.replace(line, fizz)
        elif (i % 5 == 0):
            line = line.replace(line, buzz)
        else:
            line = line.replace(line, str(i))
        print(line)


# 2
def numberToDigits(number: int):
    n = number
    i = len(str(n)) - 1
    count = 1
    while (n != 0):
        print("Цифра {count} равна {value}".format(count=count, value=(n // (10 ** i))))
        n %= (10 ** i)
        i -= 1
        count += 1


fizzBuzz()
numberToDigits(10819)
