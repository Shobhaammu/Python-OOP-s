def _prime(num):
    if num==1:
        return False
    elif num>1:
        for i in range(2,num):
            if (num%1)==0:
                return True
        return(i,'times',num//i,'is',num)
    else:
        return False
num=int(input('enter a number'))
print(_prime(num))    