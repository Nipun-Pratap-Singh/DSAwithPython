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
        
        print()  # This prints a newline character after each row
    

n = int(input())
p1(n)


