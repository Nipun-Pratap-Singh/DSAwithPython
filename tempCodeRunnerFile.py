
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

