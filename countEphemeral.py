def ephemeral(i):
    if i in eph_dict:
        #add all elements in the current sequence to dictionary with same value as element already in dictionary
        if eph_dict[i] == "Y":
            for j in temp_set:
                eph_dict[j] = "Y"
            return True
        else:
            for j in temp_set:
                eph_dict[j] = "N"
            return False
            
    if i in temp_set:
        #element is repeated so all elements in current seuqence are added to dictionary with 'N' value
        for j in temp_set:
            eph_dict[j] = "N"
        return False
    else:
        #add to temporary set for current sequence
        temp_set.add(i)
        #calculate next term in sequence
        i = sum([powers[int(k)] for k in str(i)])
        return ephemeral(i)
    


def count_ephemeral(n1, n2, k):
    #create list of powers of single digit numbers
    global powers
    powers = {0:0, 1:1, 2:2**k, 3:3**k, 4:4**k, 5:5**k, 6:6**k, 7:7**k, 8:8**k, 9:9**k}
    #create global temp set to store numbers in sequence
    global temp_set
    temp_set = set()
    #create global dictionary of tested numbers
    global eph_dict
    eph_dict = {1:"Y"}
    count = 0
    #check if each number is ephemeral
    for i in range(n1, n2):
        #increment count if number is ephemeral
        if ephemeral(i) == True:
            count += 1
        #reset set of current sequence terms
        temp_set = set()
    return count


    
        
   
