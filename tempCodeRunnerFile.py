
def p1(n):

    for i in range(n):                #   *****
        for j in range(n-1):        #    ***
            print(" ", end="")        #     *
        for j in range(2*i-1): 
            print("*",end="")   
        
        print()  
n = int(input())
p1(n) 
