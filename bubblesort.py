array=[10,4,2,7,5,8,9]

for i in range(len(array)):
    for j in range(0,len(array)-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)


