# #recursive function 
# def func(num):
    
#     #base case
#     if num == 1:
#         return 1
    
#     #recursive case
#     else:
#         return num + func(num-1)
    
# #main program
# while True:
#     num = int(input("Enter a Number: "))

#     if num == -1:
#         break
#     else:
#         print("Output:", func(num))



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

# def Multiply (M,n):
#     if (n == 1):
#         return M
#     else:
#         return M + Multiply(M, n-1)

# while True:  
#     M = int(input("Enter the first number: "))
#     n = int(input("Enter the second number: "))

#     if n == -1:
#         break
#     else:
#         print("The product of", M, "and", n, "is", Multiply(M,n))



"""Consider the following recursive sequence of numbers: 
 
2,1,0.5,0.25,0.125. . . . 
 
a) Design a recursive Python function to produce the above output when a user 
enters an integer from the keyboard. 
b) Use the loop to run the program and display the correct output until user input -1. 
c) Sample Output: 
 
Enter number:1 
Output:2 
Enter number:2 
Output:1 
Enter number:3 
Output:0.5 
Enter number: -1 
Output: Finished"""


def sequence(x):
    if x == 1:
        return 2
    else:
        return sequence(x-1)/2	
    
while True:

    x = int(input("Enter a Number: "))

    if x == -1:
        print("Output: Finished")
        break
    else:
        print("Output:", sequence(x))






