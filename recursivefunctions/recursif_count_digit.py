def count_digit(n):
    if n//10 == 0:
        return 1
    else:
        return 1 + count_digit(n//10)
    
while True:
    print(count_digit(int(input())))