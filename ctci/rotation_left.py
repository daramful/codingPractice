
def array_left_rotation(a, n, k):
    b = []
    for i in range(0, n):
        b.append(a[(k+i)%n])
    return b
        

a = [1, 2, 3, 4, 5]
array_left_rotation(a, 5, 4)
print(array_left_rotation(a, 5, 4))
