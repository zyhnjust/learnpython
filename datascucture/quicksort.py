
def quicksort(alist):
    quicksorthelper(alist, 0, len(alist)-1)

def quicksorthelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quicksorthelper(alist, first, splitpoint-1)
        quicksorthelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivot = alist[first]

    leftmark = first+1
    rightmark = last

    done= False
    while not done:
        while leftmark <= rightmark and pivot >= alist[leftmark]:
            leftmark= leftmark+1
        while leftmark <= rightmark and pivot <= alist[rightmark]:
            rightmark = rightmark-1

        if leftmark > rightmark:
            done = True
        else:
            tmp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = tmp
    tmp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = tmp
    return rightmark

alist=[6,2,3,7,89,1,90]
quicksort(alist)
print(alist)


