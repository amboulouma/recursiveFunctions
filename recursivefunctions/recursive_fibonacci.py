def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return finabocci(n-1) + finabocci(n-2)
    
while True:
    print(fibonacci(int(input())))