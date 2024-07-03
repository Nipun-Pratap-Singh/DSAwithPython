def f(number,arr):
    count = 0
    for i in arr:
        if i == number:
            count = count +1
    return count

arr = [1,2,5,1,2]      
number = 1
print(f(number,arr))