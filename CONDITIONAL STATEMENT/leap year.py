#leap year or not year:
year=int(input('Enter a year:'))
if(year%4==0 and year%100!=0):
    print(year,'is Leap Year')
else:
    print(year,'is Not A Leep Year')
    
