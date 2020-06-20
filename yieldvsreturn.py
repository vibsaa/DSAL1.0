def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   

#method 1 (x is a list )
"""x=simpleGeneratorFun()
print (x)

for value in x:  
    print(value) 
"""
#method2: 
"""
for value in simpleGeneratorFun():  
    print(value) 
"""
