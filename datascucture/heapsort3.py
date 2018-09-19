

def heapify(alist, n, i):
    largest = i
    l = 2*largest +1
    r = 2*largest +2

    if l < n and alist[largest] < alist[l]:
        largest = l
    if r < n and alist[largest] < alist[r]:
        largest = r
    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        heapify(alist, n, largest)

def heapsort(alist):
    n = len(alist)

    # first build a tree, top is the biggest.
    for i in range(n, -1, -1): # for each node, check whether the below is smaller
        heapify(alist, n, i)  # n is just to control the max

    # print(alist)

    for i in range(n-1, 0, -1):
        alist[i],alist[0] = alist[0], alist[i]
        heapify(alist, i, 0) # from 0, get a this one, you can use n, but  in fact, all the below works. no
        # heapify(alist, i, 0)

alist = [5,6,4,3,7,1,9]
heapsort(alist)
print(alist)

