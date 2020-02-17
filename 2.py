array = [int(i) for i in input().split()]
def my(array):
    i = 0
    for i in range(len(array) - 1):
        if i%2==1:
            del array[i]
        i+=1
    return array
print (my(array))