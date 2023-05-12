
def return_last_element(tuple_item):
    return tuple_item[-1]

list1 = [ (2,5) , (1,2) , (4,4) , (2,3) , (2,1)]
list2 = sorted(list1 ,  key= return_last_element)
print(list2)