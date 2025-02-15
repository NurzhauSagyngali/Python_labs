def even_nums(N):
    for x in range(0, N + 1, 2):
        yield x
        
N = int(input())
print(",".join(map(str,(even_nums(N)))))
