#While Loop Using 5th table:
print('While loop using 5th table:')
num=1
while num<=10:
    print(num,'x5=',num*5)
    num=num+1

print('-'*10)
print('Even number:')
#Even num:
num=5
i=2
while i<=10:
    print(i,'x5=',i*num)
    i+=2
print('-'*10)
print('Odd number:')
#Odd num:
num=5
i=1
while i<=10:
    print(i,'x5=',i*num)
    i+=2
print('-'*10)
print('If Condition using Even number:')
#even number using while loop(if): 
num=5
i=2
while i<=10:
    multiply=i*num
    if multiply%2==0:
        print(i,'x5=',i*num)
    i+=1
#odd number using while loop(if):
print('-'*10)
print('If Condition using Odd number:')
num=5
i=1
while i<=10:
    multiply=i*num
    print(i,'x5=',i*num)
    i+=2
