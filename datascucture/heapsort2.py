
def heapify(alist, n, i):
    largest = i
    l = 2*i +1
    r = 2*i +2

    # infact, it works. for i and largest.
    # if l <n and alist[i] < alist[l]:
    if l < n and alist[largest] < alist[l]:
        largest = l
    if r <n and alist[largest] < alist[r]:
        largest = r
    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        heapify(alist, n, largest)

def heapsort(alist):
    n=len(alist)

    #build one tree
    # why 6 -> 0 , sort need all.
    for i in range(n, -1, -1):
        heapify(alist, n, i)

    # for i in range(n-1, 0, -1):
    # why 6 -> 1, because 0 is the lasrget, not need.
    for i in range(n - 1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]
        heapify(alist, i, 0)

alist=[3,5,4,6,1,2,9]
heapsort(alist)
print(alist)
