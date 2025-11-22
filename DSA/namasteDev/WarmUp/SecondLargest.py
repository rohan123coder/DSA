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
