#sum of all elment in list:
lst= [100,200,300,400,500]
total=0
i=0
while i < len(lst):
    total =total+lst[i]
    i+= 1
print("Sum =",total)
#Find the max element:
lst=[100,200,300,400,500]
max_value=lst[0]
i = 1
while i < len(lst):
    if lst[i] > max_value:
     max_value =lst[i]
     i+= 1
print("Maximum value:", max_value)
#Find the min element:
lst=[100,200,300,400,500]
min_value=lst[0]
i =1
while i < len(lst):
    if lst[i]<min_value:
       min_value =lst[i]
    i+= 1
print("Minimum value:", min_value)
#Find the min element:
lst=[100,200,300,400,500]
total=0
i=0
while i < len(lst):
    total+=lst[i]
    i+=1
    average=total/len(lst)
print('Average value:',average)




