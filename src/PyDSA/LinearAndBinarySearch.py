def linearSearch(arr,value):
    for i in range(len(arr)):
        if i == value:
            return i
    return -1

arr= [4,6,7,3,8]
val= 3

result=linearSearch(arr,val)

if result != 1:
    print("linear Search value in list: ",result )
else:
    print('Not found')