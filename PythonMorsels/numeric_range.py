''' Function returns the difference between the highest
    lowest values in a list of numbers'''
def numeric_range(numArr):
    if type(numArr) == list:
        if len(numArr) <= 1:
            print(0)
            return 0

        numArr = sorted(numArr)
        out = numArr[len(numArr)-1] - numArr[0]
    else:
        newArr = []
        print('numArr: {0}'.format(numArr))
        for i in numArr:
            print('i: {0}'.format(i))
            if type(i) != int:
                for j in i:
                    nextArr.append(j)
            else:
                newArr.append(i)
        newArr = sorted(newArr)
        
        out = newArr[len(numArr)-1] - newArr[0]
        print('tup')
    print(out)
    return(out)

numeric_range([10,8,7,5,3,6,2])
numeric_range([1,2,3])
numeric_range([4])
numeric_range([])



#TODO: Modify function to accept iterables as well as lists.
#      Keep in mind larg numbers.
