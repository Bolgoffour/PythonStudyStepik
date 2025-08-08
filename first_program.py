x = int(input())
sequence = (x, 2 * x , 3 * x, 4 * x, 5 * x)
print(*sequence, sep='---')
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')