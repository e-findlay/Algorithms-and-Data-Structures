def merge_sort(lst):
    #sort using selection sort if list is <= 4
    if len(lst) <= 4:
        for i in range(0, len(lst)-1):
            elem = lst[i]
            pos = i
            #if element to right of chosen element larger, choose the larger element
            for j in range(i+1, len(lst)):
                if lst[j] > elem:
                    elem = lst[j]
                    pos = j
            #swap largest element with the first available element
            temp = lst[pos]
            lst[pos] = lst[i]
            lst[i] = temp
        return lst
        
    #find midpoint of list
    mid = int(len(lst)/2)
    #split into left and right list
    left = lst[:mid]
    right = lst[mid:]
    #call mergesort on left list then right list
    leftsort = merge_sort(left)
    rightsort = merge_sort(right)
    return merge(leftsort, rightsort)

def merge(leftsort, rightsort):
    result = []
    while len(leftsort) > 0 or len(rightsort) > 0:
        if len(leftsort) > 0 and len(rightsort) > 0:
            #compare left-most element of both lists and append largest element to result
            if leftsort[0] > rightsort[0]:
                result.append(leftsort[0])
                leftsort.pop(0)
            else:
                result.append(rightsort[0])
                rightsort.pop(0)
        #if right list empty, appent left-most element of left list to result
        elif len(leftsort) > 0:
            result.append(leftsort[0])
            leftsort.pop(0)
         #if left list empty, appent left-most element of right list to result
        else:
            result.append(rightsort[0])
            rightsort.pop(0)
    return result
