def all(n):
    for x in range(n, -1, -1): #range(start stop step)
        yield x
    
n = int(input())
for num in all(n):
    print(num)