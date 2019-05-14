# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(lst):
    '''Way 1 - This method cannot handle the case when lst is a list of list
    dic = {}
    if lst == []:
        return None
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count += 1
            dic[i] = count
    result_c = dic[lst[0]]
    result = lst[0]
    #print dic
    for e in dic:
        #print e
        #print dic[e]
        if dic[e] > result_c:
            result_c = dic[e]
            result = e
    return result
    '''
    #Way 2
    best = None
    best_count = 0
    current = None
    current_count = 0
    for e in lst:
        if e != current:
            current = e
            current_count = 1
        else:
            current_count += 1
        if current_count > best_count:
            best = current
            best_count = current_count
    return best
            
            
            


#For example,
print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

