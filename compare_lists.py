list1 = [1, 1.0, "3"]
list2 = [1, 1.0, "3"]


def compare_2_lists(list_1, list_2):
    if not isinstance(list_1, (list, tuple)):
        return False
    if type(list_1) == type(list_2) and len(list_1) == len(list_2):
        for index in range(len(list_1)):
            if list_1[index] != list_2[index]:
                return False
        return True
    else:
        return False
