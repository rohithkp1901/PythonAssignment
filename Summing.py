n=int(input('Enter limit: '))
s=0
i=1
while i<=n:
    print(i,end=' ')
    if i!=n:
        print('+',end=' ')
    s+=i
    i+=1
print('\nSum upto ',n,' is ',s)