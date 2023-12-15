x=int(input('Enter First Number: '))
y=int(input('Enter Second Number: '))
z=int(input('Enter Third Number: '))
if(x>y)and(x>z):
    print(x,' is greater than ',y,'and',z)
elif(y>z)and(y>x):
    print(y,' is greater than ',x,'and',z)
else:
        print(z,' is greater than ',y,'and',x)

