"""print ("hello world")
number1=2
n2=2.45
n3='vibhanshu'
#python automatcally interprets whether the variable is of char int or float type
print(number1,n2,n3)
#list
nums=[]
# to add items use append()
nums.append(21)
nums.append(34.5)
nums.append("string")
print (nums)

#input()

name= input("what is ur name")
print ("hello", name)
#example 2 in this if u go without using "to int" converter int() then you will see that the output will be concatenated version of two nos
#because the returned data from input() is a string
num1=int(input("enter first no"))
num2=int(input("enter sec no"))
num3=num1+num2
print("sum=", num3)

print (True +True +True)
print (True +False +False)"""

a=None 
print(a==None)
#the expression x and y first evaluates x; if x is false its value is returned
#otherwise, y is evaluated and the resulting value is returned
b= 10 and 60 and 40
print(b)
#The expression x or y first evaluates x; if x is true, its value is returned;
# otherwise, y is evaluated and the resulting value is returned.
c=20 or 40
print(c)

"""x=None
y=1
print (x==y)
#used for debugging purposes
assert x==1,"this is how you can add your error to the assert keyword"
"""
# use of del: initialising list  
a = [1, 2, 3] 
  
# printing list before deleting any value 
print ("The list before deleting any value") 
print (a) 
  
# using del to delete 2nd element of list 
del a[1] 
  
# printing list after deleting 2nd element 
print ("The list after deleting 2nd element") 
print (a) 

