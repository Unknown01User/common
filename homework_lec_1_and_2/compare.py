# list1=[1, 2.7, "Hi", 1] # for testing
# list2=[1, 2.7, "Hi", 1] # for testing

list1=input("Enter list1 with '[]' or '()' and ',' ")
list2=input("Enter list2 with '[]' or '()' and ',' ")

def compare_lists(list1,list2):
    count = 0                                        # for now that this is end of lists
    if ((type(list1) == type(list2)) and (len(list1)==len(list2))): # compare type and length of our lists
        for i in list1:
            if id(i) == id(list2[(list1.index(i))]): # or if (type(i)== type(list2[(list1.index(i))]) and i==list2[(list1.index(i))]):
                count += 1                           # if compare type and value of our lists is True
                if len(list1) == count:              # this is the last element of our list
                    return True
    return False    # if at least one condition isn't made

print("Result of list1 = ", list1, "and", "list2 = ", list2)
print("is ", compare_lists(list1,list2))