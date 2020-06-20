"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

x=input("enter the no whose factorial is to be found")

def fact(a):
    f=1
    if a==0:
        f=1
    else:
        while(a):
            f=f*a
            a=a-1
    return f

y=fact(int(x)) #this is an important point to remember that input() returns an string and cant be used as an operand to 
#while
print(y)