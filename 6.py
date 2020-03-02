array = [int(i) for i in input().split()]
num = int(input())
num2 = int(input())
array2 = [int(i) for i in input().split()]
def my(array, num, num2, array2):
    array.insert(num, array2)
    array3 = [int(i) for i in input().split()] 
    # i = 0
    # for i in range(len(array) - 1):
    #     if i > num2 - 1:
    #         del array[i]
    #     i+=1
    return array3
print (my(array, num, num2, array2))