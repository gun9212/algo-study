import sys
input = sys.stdin.readline

N = int(input())

for i in range (N):
    etc = i    
    num= [0] * 8
    for j in range (7, 0, -1):
        num[j] = int(etc // (10**j))
        etc = int(etc % (10**j))

    sum = i
    for k in range (1, 8):
        sum += num[k]
    sum += etc
    if (N == sum):
        print(i)
        break
else:
    print(0)