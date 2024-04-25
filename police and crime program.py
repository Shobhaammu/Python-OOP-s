n=int(input('enter the no of times'))
availableofficers = 0
untreatedCrimes= 0

for i in range(n):
    event=int(input())
    if event == -1:  
        if availableofficers > 0:
            availableofficers -=1
        else:
            untreatedCrimes+= 1
    else:
        availableofficers+=event

print(untreatedCrimes)