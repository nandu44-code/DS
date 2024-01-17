
arr=[1,2,3,4,5,6,7,8,9,10]
element=int(input('enter an element to be found in this array'))
def binarySearch(array,element):
    left=0
    right=len(array)-1
    while left<=right:
        middleElement=(left+right)//2

        if element <middleElement:
            right=middleElement-1
        elif element>middleElement:
            left=middleElement+1
        else:
            return middleElement

    print('target element is not found')

result=binarySearch(arr,element)
print("target element found at position",result)