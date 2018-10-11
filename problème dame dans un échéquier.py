from scipy import *


def case_libre(n,L,M):
    #Prend en argument un tableau M correspondant à l'échéquier 
    #et une liste L correspondant au placement de la nouvelle dame
    #il ressort un nouveau tableau où il est inscrit les cases
    #où il est impossible de placer une nouvelle dame
    S=array(zeros((n, n)))
    for i in range (n):
        for j in range (n):
            S[i][j]=M[i][j]
           
    for j in range(len(M)):
        S [L[0]][j]=1
        S [ j ][ L [1] ]=1
    a=L[0]+1
    b=L[1]+1
    while a<n and b<n:
        S[a][b]=1
        a+=1
        b+=1
    a=L[0]+1
    b=L[1]-1
    while a<n and b>-1:
        S[a][b]=1
        a+=1
        b-=1 
    a=L[0]-1
    b=L[1]-1
    while a>-1 and b>-1:
        S[a][b]=1
        a-=1
        b-=1
    a=L[0]-1
    b=L[1]+1
    while a>-1 and b<n:
        S[a][b]=1
        a-=1
        b+=1   
    
    return(array(S))

def verif(M):
    #vérifie si il reste des cases libre au placement d'une dame
    z=False
    for i in range (len(M)):
        for j in range (len(M[i])):
            if M[i][j]== 0:
                z=True
    return(z)

def indice(M):
    #ressort l'indice d'une case libre au placement d'une dame
    a=[-1,-1]
    i=-1
    while a==[-1,-1]:
        i+=1
        if 0 in M[i]:
            K=list(M[i])
            a=[i,K.index(0)]
    return (a)

#M=array([[1,2,2],[1,4,0]])
#print(indice(M))




def iteration(d,n,L,N,compte):
    #recherche les toutes les combinaisons possibles et
    #ajoute plus 1 au compteur dès qu'il en trouve une
    #fonction dont le fonctionnement est difficile à décrire mais je peux l'expliquer 
    #à l'oral son mécanisme grâce à des dessins
    if d!=0 and verif(N[-1]):
        L.append(indice(N[-1]))
        N.append(case_libre(n,L[-1],N[-1]))
        d-=1
        return(iteration(d,n,L,N,compte))
    
    if d==0:
        compte+=1
        a=L[-1]
        del L[-1]
        del N[-1]
        N[-1][a[0]][a[1]]=1
        d+=1
        return(iteration(d,n,L,N,compte))
    
    if d!=0 and not(verif(N[-1])):
        if len(N)==1:
            return(compte)        
        else:
            a=L[-1]
            del L[-1]
            del N[-1]
            N[-1][a[0]][a[1]]=1
            d+=1
            return(iteration(d,n,L,N,compte))
        
        
def solve(d,n):
    compte=0
    L=[]
    N=[]
    M=array(zeros((n, n)))
    N.append(M)
    return(iteration(d,n,L,N,compte))        
print(solve(4,4))          
        
