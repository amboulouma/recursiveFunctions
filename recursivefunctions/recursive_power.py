from math import floor

def power(a, n):
    if n == 0:
        return 1
    else:
        if n%2:
            return a*(power(a,(floor(n/2)))**2)
        else:
            return power(a,(floor(n/2)))**2
        
while True:
    a, n = map(int, input().split())
    print(power(a, n))