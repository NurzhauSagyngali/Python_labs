def squares_nums(N):
    for x in range(N + 1):
        yield x ** 2
        
N = int(input())
for num in squares_nums(N):
    print(num)

