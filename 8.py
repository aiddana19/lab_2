list1 = [int(i) for i in input().split()]
def tup(list1):
    my_t = tuple(list1) 
    res = min(my_t), max(my_t)
    return res
print (tup(list1))