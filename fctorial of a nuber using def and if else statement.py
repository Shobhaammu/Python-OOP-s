n=int(input('enter a number:'))
def factorial(n):
    fact=1  
    for i in range(1,n+1):
        fact*=i
    return fact
result=factorial(n)
print(result)
               (or)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input('enter a number:'))
print(factorial(n))    

 