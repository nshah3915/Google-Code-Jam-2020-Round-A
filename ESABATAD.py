import sys
testCases = int(input())
for test in range(testCases):
    low,high=map(int,input().split())
    n=int(input())
    g=int((low + high)//2)
    print(g)
    sys.stdout.flush()
    for j in range(n):
        r=input()
        if r == 'CORRECT':
            break
        elif r == 'TOO_SMALL':
            low=g
            g=int((low + high)//2)
            print(g)
            sys.stdout.flush()
        elif r == 'TOO_BIG':
            high = g
            g=int((low + high)//2)
            print(g)
            sys.stdout.flush()
        else:
            sys.exit(0)
    else:
        sys.exit(0)
            
