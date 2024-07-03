#leap year
n = int(input())
if (n %4==0 and n%100!=0 ) or n%400==0:

    print("yes")
else:
    print("NO")

# reverse number
n  = int(input())
reverse = 0
while (n>0):
    last = n%10
    reverse = (reverse *10) +last
    n = n//10
print(reverse)


# reverse number or string

n = int(input())
str = str(n)
print(str[::-1])

# count the number
n = 1234
count = 0
while(n>0):
    last = n%10
    count = count +1
    n = n//10
print(count)    

# amstrong numbr yes OR no
num = int(input())
sum =0
temp = num
while temp>0:
    digit = temp %10
    sum = sum + digit**3
    temp= temp//10
if num == sum:
    print(num,"true")
else:
    print(num,"false")


# print all division numbers of  an integer
n = int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end =" ")
   
         
# if we want t calculate th esum of al division number
def divisorSum(self, n):
        # pass
        sum = 0
        for i in range(1, n+1):
            if n % i == 0:
                sum += i 
  


# print prime numbers
n = int(input())
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
          print(i,end = " ")

          
# check number is prime or not
num = int(input())
if num > 1:
    for i in range(2, int(num/2)+1):
       
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    
    
# print HCF of two integers

n1 = int(input())
n2 = int(input())
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        print(i,end =" ")
    
