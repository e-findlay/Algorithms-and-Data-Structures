def hash_quadratic(d):
    #create table
    table = ["-"]*19
    count = 0
    Next = False
    for k in d:
        #if k already in table, skip to next input
        if k in table:
            continue
        #hash function
        i = (6*k + 3) % 19
        j = 0
        #find empty space in hash table
        while table[i] != "-":
            j+= 1
            i = (i + j**2 - (j-1)**2) % 19
            #if no space fond from quadratic hash, break loop
            if j > 19:
                Next = True
                break
        #continue to next number in input if no space found in hash table
        if Next == True:
            Next = False
            continue
        #place element in table
        table[i] = k
        count += 1
        if count == 19:
            return table
    return table

def hash_double(d):
    #create table
    table = ["-"]*19
    count = 0
    Next = False
    for k in d:
        #if k already in table, skip to next input
        if k in table:
            continue
        #hash function
        i = (6*k + 3) % 19
        #secondary hash function
        h = 11 - (k % 11)
        j = 0
        #look for empty space in hash table
        while table[i] != "-":
            j += 1
            i = (i + j*h - (j-1)*h) % 19
            #if no space found from secondary hashing, break loop
            if j == 19:
                Next = True
                break
        #if no space found, continue to next element in sequence
        if Next:
            Next = False
            continue
        #place element in hash table
        table[i] = k
        count += 1
        #if table full, return table
        if count == 19:
            return table
    return table


