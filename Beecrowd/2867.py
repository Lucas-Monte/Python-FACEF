c = int(input())


for i in range (0, c, 1):
    n, m = (input().split())
    resp = int(n) ** int(m)
    print(len(str(resp)))
