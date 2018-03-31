def number_needed(a, b):
    list_a = [x for x in list_a if x in list_b]

    #listed = [list_a_copy.pop(i) for i,j in enumerate(list_a) if j in list_b]
    #print(listed)
    count = 0
    for i in (list_a):
        for j in (list_b):
            if i == j:
                list_a.replace(i, "None")
                list_b.replace(j, "None")
                print("a", list_a)
                print("b", list_b)
                count+=1
    return count

    '''
    print("lista", list_a)
    count = len(listed)
    print(listed)
    print("count", count)
    notchange = len(list_a) + len(list_b) - count*2
    return notchange
'''
    return 0


a = "mynameissam"
b = "nameissam"
print(number_needed(a,b))