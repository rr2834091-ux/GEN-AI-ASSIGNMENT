#Fibonacci series:
n=15
a=0
b=1
for i in range(n):
    print(a,end='')
    c=a+b
    a=b
    b=c
print(b)
print('-'*30)
#Reverse String:
text='DNEIRF'
reverse=''
for ch in text:
    reverse=ch+reverse
print(reverse)
