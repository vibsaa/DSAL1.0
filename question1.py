"""Write a program which will find all such numbers which are divisible
 by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
l=[]
for i in range(2000, 3201):
    if(i%7==0):
        if(i%5!=0):
            l.append(str(i))
        
    i=i+1

#print(l)

""" here we can also use join function which is: The join() method is a 
string method and returns a string in which the elements of 
sequence have been joined by str separator.

string_name.join(iterable)

Parameters: The join() method takes iterable – objects capable
 of returning its members one at a time. 
 Some examples are List, Tuple, String, Dictionary and Set

Return Value: The join() method returns a string concatenated with 
the elements of iterable.
"""
#shown below
print (','.join(l))