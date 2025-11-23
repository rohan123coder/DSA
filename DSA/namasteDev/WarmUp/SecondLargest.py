# Corner cases:
#  1. If the array has less than 2 elements, return None
#  2. If all elements are the same, return None
#  3. If the array contains negative numbers, handle them correctly
#  4. If the array contains floating point numbers, handle them correctly
#  5. If the array contains duplicate largest elements, return the next distinct largest element

def second_largest(arr):
    if len(arr)<2:
        return None
    firstLargest=float('-inf')
    secondLargest=float('-inf')
    for num in arr:
        if firstLargest<=num:
            secondLargest=firstLargest
            firstLargest=num
        elif secondLargest<num:
            secondLargest=num
    return secondLargest

    
    
if __name__=='__main__':
    arr=[23,5,888,533,0.0,-1,-45,8,23.5]
    print(second_largest(arr))
