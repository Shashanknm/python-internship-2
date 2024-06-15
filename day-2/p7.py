def p(n,m):
    if m==0:
        return 1
    else:
        return n*p(n,m-1)
print(p(2,3))

