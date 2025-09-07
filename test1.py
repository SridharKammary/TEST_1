arr=[1,2,3,4,5]
for i in arr:
    print(i)
#array apprehension
arr2=[i*i for i in arr]
for i in arr2:
    print(i)

arr2.filter(lambda x:x%2==0)
print(arr2)   
#filter
arr3=list(filter(lambda x:x%2==0,arr)) 
for i in arr3:
    print(i)