# first loop is for rows and 2nd loop for the columns
def p1(n):

    for i in range(0, n):        #  ***
        for j in range(0, n):    #  ***
           print("*", end=" ")   #  ***
        
        print()  # This prints a newline character after each row
    

n = int(input())
p1(n)         



def p1(n):

    for i in range(n):           #  *
        for j in range(i+1):     #  **
           print("*", end=" ")   #  ***
        
        print()  
n = int(input())
p1(n)



def p1(n):

    for i in range(1,n):           #  1
        for j in range(1,i+1):     #  22
           print(i, end=" ")       #  333
        
        print()  

n = int(input())
p1(n)


def p1(n):

    for i in range(1,n):           #  1
        for j in range(1,i+1):     #  12
           print(j, end=" ")       #  123
        
        print()  
    

n = int(input())
p1(n)


def p1(n):

    for i in range(n):             #  ***
        for j in range(n-i+1):     #  **
           print("*", end="")      #  *
        
        print() 
    

n = int(input())
p1(n)


def p1(n):

    for i in range(1,n):             #  123
        for j in range(1,n-i+1):     #  12
           print(j, end="")          #  1
        
        print()  

n = int(input())
p1(n) 



def p1(n):

    for i in range(n):             #    *
        for j in range(n-i-1):     #   ***
            print(" ", end="")     #  *****
        for j in range(2*i+1): 
            print("*",end="")   
        
        print()  
n = int(input())
p1(n) 




def p1(n):

    for i in range(n,0,-1):           #   *****
        for j in range(n-i):          #    ***
            print(" ", end="")        #     *
        for j in range(2*i-1): 
            print("*",end="")   
        
        print()  
n = int(input())
p1(n) 

def p1(n):
    # Upper part of the pattern
    for i in range(n):
        for j in range(n - i - 1):   #   *
            print(" ", end="")       #  ***
        for j in range(2 * i + 1):   # ******
            print("*", end="")       #  ***
        print()                      #   *

    # Lower part of the pattern
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

n = int(input())
p1(n)



def p1(n):
    # Upper part of the pattern        #  *  
    for i in range(1, n + 1):          #  **
        print("*" * i)                 #  ***
                                       #  ****
    # Lower part of the pattern        #  ***
    for i in range(n - 1, 0, -1):      #  **
        print("*" * i)                 #  *

n = int(input())
p1(n)




def p1(n):
    current_num = 1
    for i in range(1, n + 1):            #  1       
        for j in range(i):               #  23
            print(current_num, end="")   #  456
            current_num += 1             #  789
        print()

n = int(input())
p1(n)
