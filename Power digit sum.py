def solve(n):
    a=str(2**n)
    sum= 0
    for i in range (len(a)):
        sum+= int(a[i])
    return(sum)

print(solve(1000))
    