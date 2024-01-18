

list=[8,3,12,2,7,4,5,1]
len=len(list)
for i in range(1,len):
    key=list[i]
    j=i-1
    while j>=0 and list[j]>key:
        list[j+1]=list[j]
        j=j-1
        list[j+1]=key
print(list)
# # insertion sort
