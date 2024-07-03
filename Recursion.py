# print name n  time by using for loop
def name(name):
    for i in range(5):
        print(name )
name("nipun")
   

# print name n  time by  recursion
def function(i,n):
    if i>n:
        return
    print("nipun")
    function(i+1,n)  #time O(n)
n = int(input())     # space = O(n)
function(1,n)


# print number 1 upto N   
def number(i,n):
    if i>n:
        return
    print(i,end= " ")
    number(i+1,n)
n =int(input())
number(1,n)    



# print number N to 1
def number(i,n):
    if i<1:
        return
    print(i,end= " ")  # if i change this line
    number(i-1,n)     # to this line it works opposite
n =int(input())       #it goes 1 to N
number(n,n) 


# Sum numbers upto N
def sum(i,total):
    if i<1:
        print(total)
        return
    sum(i-1,total+i)
n = int(input())  
sum(n,0) 

# Factorial  Of n number
n= int(input())
factorial = 1
if n>=1:
 for i in range(1,n+1):
    factorial = factorial*i
 print(factorial)        



 # Factorial of Number n by using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n= int(input())
print(factorial(n))    


#rverse an array
def f(i,list,n):
    if i>=n/2 :
        return 
    list[i], list[n - i - 1] = list[n - i - 1], list[i] 
    f(i+1,list,n)
n= int(input())
list = list(map(int,input().split()))
f(0,list,n)
for i in range(n):
    print(list[i],end=" ")
    
    
# palindrome function:

def word(word):
    if word == word[::-1]:
        print(word,"is Palindrome")
    else:
        print(word," not palindrome")    
n = input("")
word(n)


# multiple Recursion Call
# Fibbonacci series
def fib(n):
     a=0
     b=1
     while(a<n):
         print(a,end=" ")
         a,b = b,(a+b)
n = int(input())
fib(n)         




