a = [27, 10, 42, 36]

def my_enumerate(a):
    for i in range(len(a)):
        print("{}:{}".format(i, a[i]))

my_enumerate(a)

def my_max(x):
    flag = True
    while flag:
        flag = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True

my_max(a)
print(a)

