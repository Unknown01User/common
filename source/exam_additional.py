#1
#Поиск работает в основном быстрее для set и dict т.к это hash таблицы.
#Перебор элементов быстрее в list и tuple,т.к это обычные массивы а set  и dict для этого не предназначены.
#2
#Разница в том, что в первом случае массив будет содеержать три указателя на дин и тот же массив.
# Если мы изменим элемент в одном из подмассивов то соответственно все элементы будут с этим измененением, т.к указываеют на один и тот же.
#Во втором случае будет создано три копии массива и ситуация описанная выше не повторится
#3
class Counter:
    count=0
    def __init__(self):
       Counter.count+=1
    @classmethod
    def get_count(cls):
        return cls.count
#4
def create_dict(keys,vals):
    result={}
    i=0
    length=min(len(keys),len(vals))
    while i<length:
        result[keys[i]]=vals[i]
        i+=1
    length=len(keys)
    while i <length:
        result[keys[i]]=None
        i+=1
    return result
