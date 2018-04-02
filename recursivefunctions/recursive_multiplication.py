def multiplication(a, b):
    if a == 0 or b == 0:
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    else:
        return a + multiplication(a, b - 1)
    
while True:
    a, b = map(int, input().split())
    print(multiplication(a, b))