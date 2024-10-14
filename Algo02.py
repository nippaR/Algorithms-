#recursive function 
def func(num):
    
    #base case
    if num == 1:
        return 1
    
    #recursive case
    else:
        return num + func(num-1)
    
#main program
while True:
    num = int(input("Enter a Number: "))

    if num == -1:
        break
    else:
        print("Output:", func(num))



#recursive function sample qusetion

"""
A recursive algorithm for the calculation for the multiplication of two numbers M and n  
is given below: 
 
Multiply (M,n) 
   
if (n = 1) 
return  M;                      
    
else 
return (M + Multiply(M, n-1)) 
 
a) Write a program in Python to read an integers from the keyboard for M and n. 
b) Develop a function in python named as multiply and implement the above 
recursive algorithm. 
c) Pass the input number as parameter to the function developed and get the 
multiplication of numbers as output.  
d) Use the loop to run the program and display the correct output until user input -1. 
"""	

def Multiply (M,n):
    if (n == 1):
        return M
    else:
        return M + Multiply(M, n-1)

while True:  
    M = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))

    if n == -1:
        break
    else:
        print("The product of", M, "and", n, "is", Multiply(M,n))






