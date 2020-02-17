array = [int(i) for i in input().split()]
num = int(input())
def my(array, num):
    i=0
    for i in range(len(array)):
        if i>=num:
            array[i]=array[i]*array[i]
        i+=1
    return array
print(my(array, num))