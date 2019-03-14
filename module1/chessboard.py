n = 8
a = [[0] * n for i in range(n)]
print(a)
for i in range(n):
    for j in range(n):
        
        a[i][j] = [' ']
for row in a:
    print(' '.join([str(elem) for elem in row]))

'''
n = 8
a = [[0] * n for i in range(n)]
for i in range(n):
    if i == 1:
        for j in a:
        j = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
'''
