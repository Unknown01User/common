def compare(first_collection,second_collection):
    if(len(first_collection)!=len(second_collection)):
        return False
    it=iter(second_collection)
    for elem in first_collection:
        another_elem=next(it)
        if elem != another_elem or type(elem)!=type(another_elem) :
            return  False
    return  True
list=[1,2,3,4,5,6,7]
tple=(1,2,3,4,5,6,7)
print(compare(list,tple))
