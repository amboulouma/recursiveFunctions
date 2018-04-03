def natural_numbers(n):
    if n == 0:
        return 0
    else:
        print("{} ".format(n), end="")
        return natural_numbers(n - 1)
    
while True:
    n = int(input())
    natural_numbers(n)