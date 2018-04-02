    
def division(a, b):
    if a < b:
        return 0
    else:
        return 1 + division(a-b, b)
    
while True:
    try:
        a, b = map(int, input().split())
        if b == 0:
            raise Exception
        print(division(a, b))
    except Exception:
        print('This following operation cannot be performed because b = 0')