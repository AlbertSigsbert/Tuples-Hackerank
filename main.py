n = int(input())


int_list = map(int, input().split()[:n])

t = tuple(int_list)

print(hash(t))
