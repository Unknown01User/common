import datetime
import time
import itertools

def chargen():
    for c in '0123456789':
        yield c


words = [c + c for c in chargen()][:10]
print(words)


def multiplier(m, source=[1, 2, 3]):
    return [m * i for i in source]


print(multiplier(2, [2, 4, 8]))


class MyContextManager:
    def __enter__(self):
        print("Start time: {}".format(datetime.datetime.now().time()))
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Finish time: {}, duration: {:.3f}".format(datetime.datetime.now().time(), time.time() - self.start_time))


with MyContextManager():
    list_1 = [23, 125, 89, 56, 58, 58, 100, 2222222, 85, 789, 1, 1258, 1478952, 15, 58, 3, 24, 2, 3, 7]
    time.sleep(1)
    list_2 = [i*365 for i in list_1]
    print(list_2)


def get_3_lists_return_1(list1, list2, list3):
    new_list = []
    new_list.extend(list1)
    new_list.extend(list2)
    new_list.extend(list3)
    print(new_list)
    return new_list


get_3_lists_return_1([1, 2, 3], [4, 5, 6], [7, 8, 9])


def return_words_longer_than_5(the_list):
    return [item for item in the_list if len(item) >= 5]


print(return_words_longer_than_5(['Hello', 'i', 'write', 'cool', 'code']))


def show_all_combinations(string):
    return [i for i in itertools.permutations(string)]

print(show_all_combinations("password"))
