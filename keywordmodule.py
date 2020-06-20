"""
#Instead of writing this massive Python code we can also code this in a different way 
  
#Python code to demonstrate working of iskeyword() 
  
# importing "keyword" for keyword operations 
import keyword 
import keyword 
# initializing strings for testing while putting them in an array 
keys = ["for", "while", "tanisha", "break", "sky", 
"elif", "assert", "pulkit", "lambda", "else", "sakshar"] 
  
for i in keys: 
     # checking which are keywords 
    if keyword.iskeyword(i): 
        print(i + " is python keyword") 
    else: 
        print(i + " is not a python keyword") """
"""
#other way of writing the same code
#Instead of writing this massive Python code we can also code this in a different way 
  
#Python code to demonstrate working of iskeyword() 
  
# importing "keyword" for keyword operations 
import keyword 
import keyword 
# initializing strings for testing while putting them in an array 
keys = ["for", "while", "tanisha", "break", "sky", 
"elif", "assert", "pulkit", "lambda", "else", "sakshar"] 
  
for i in range(len(keys)): 
     # checking which are keywords 
    if keyword.iskeyword(keys[i]): 
        print(keys[i] + " is python keyword") 
    else: 
        print(keys[i] + " is not a python keyword") """
"""
#simple usage
import keyword
x=keyword.iskeyword("string")
print(x)
"""
#to print all the keywords we use kwlist() in keyword module
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
