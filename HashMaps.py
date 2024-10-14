#HAshing is  == Prestoring/ fetching

# question 1
def f(number,arr):
    count = 0
    for i in arr:              # time complexity  =  o(Q*n) 
        if i == number:
            count = count +1   # count+=1 
    return count

arr = [1,2,5,1,2]      
number = 1
print(f(number,arr))
  

  # Question 2

a = list(map(int, input().split())) # how to take input of array
print(a)


n = int(input())
arr = list(map(int,input().split()))   # isme ye btaya hai ki ek 
                                        # array me konsa element kitni baar aaya hai
hash = [0] * 13
for num in arr:
    hash[num] += 1

q = int(input())
while q > 0:                # we can also use for loop for this
    q -= 1
    number = int(input())
    # fetch
    print(hash[number])


