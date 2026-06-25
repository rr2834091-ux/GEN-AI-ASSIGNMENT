#Count the Even Number in a list:
lst=[10,23,36,45,52]
count=0
i=0
while i < len(lst):
    if lst[i]%2==0:
        count+=1
    i+=1
print('Even numbers:',count)
#Prime Or Not number:
n=int(input("Enter a number: ",))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print(n,'is a Prime Number')
else:
    print(n,'is Not a Prime Number')
#Find the Factorial:
n=int(input('enter a number:'))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print('factorial',fact)
#Reverse a string:
S=input('enter a string:')
reverse=''
i=len(S)-1
while i>=0:
    reverse+=S[i]
    i-=1
print('Reverse String',reverse)
#Sring Palindrome or Not
S=input('enter a string:')
reverse=''
i=len(S)-1
while i>=0:
    reverse+=S[i]
    i-=1
if S==reverse:
    print('String is Palindrome')
else:
    print('String is not palindrome')
#
numbers=[10,20,10,30,20,40,50,40]
i = 0
while i<len(numbers):#Using nested While loop
    j=i+1
    while j<len(numbers):
        if numbers[i]==numbers[j]:
            numbers.pop(j)
        else:
            j+=1
    i+=1 
print('Updated List:',numbers)



