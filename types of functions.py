#1.positional parameters
#example
def add_numbers(a,b):
    return a+b
result=add_numbers(3,5)
print(result)

#2.default parameter example
def greet(name='World'):
    print('Hello,'+name+'!')
    
greet()
greet('shobha') 

#3.keyword parameter
def greet(name,greeting):
    print(greeting +',' + name+ '!')
greet(greeting='Hello', name='Shobha')  

l=[1,2,3] 
print(l)
print(*l) 

#4.argumented
def addition(*args):
    result=0
    for num in args:
        result+=num
    return result
print(addition(2,4,5,6)) 

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key + ':'+ value)
        
student_info(name='shobha',age='21',clg='BITM')        






