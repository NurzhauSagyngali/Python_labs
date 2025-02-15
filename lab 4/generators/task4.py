def squares(a,b):
    for x in range(a, b + 1):
        yield x ** 2
        
a,b = map(int, (input().split()))

for num in squares(a,b):
    print(num)