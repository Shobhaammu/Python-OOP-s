#ARMSTRONG  NUMBER
num=int(input('enter anumber'))
def is_armstrong(num):
    temp=num
    armstrong_sum=0
    num_digits=len(str(num))
    
    while temp>0:
        digit=temp%10
        armstrong_sum+=digit**num_digits   
        temp//=10
    return num==armstrong_sum
print(is_armstrong(num))

