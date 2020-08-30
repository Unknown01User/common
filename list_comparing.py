# сравнивает 2 списка
def comparing_list(a, b):
    #сравниваем, присутствует один и тот же элемент (х)в разных списках
    result = [x for x in a + b if x not in a or x not in b] 
    if not result:
        print("Списки одинаковые")
        return True
    else:
        print("Списки не одинаковые")
        return False
list1 = input("Добавьте первый список для сравнения через , в []: ")
list2 = input("Добавьте второй список для сравнения через , в []: ")
comparing_list(list1, list2)
