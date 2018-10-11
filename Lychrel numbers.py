    
def operation(n):
    res=0
    a=str(n)
    b=""
    for i in range (1,len(a)+1):
        b+=a[-i]
    return(int(a)+int(b))



def test_palindrome(n):
    a=str(n)
    test=True
    i=0
    while i<len(a)//2 and test:
        if a[i]!=a[-i-1]:
            test=False
        i=i+1
    return(test)


def solve(n):
    sortie=0 #compteur
    for i in range (n): 
        j=1
        a=operation(i)
        while not(test_palindrome(a)) and j<50:
            j+=1
            a=operation(a)
        if j==50:
            sortie+=1
    return(sortie)
            
            
print(solve(10000))
  
