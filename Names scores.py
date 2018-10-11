def initialisation_fichier(dossier):
    f=open (dossier,'r')
    for a in f:
        sortie= a
    f.close()
    return sortie


def solve(dossier):
    compte=0 
    chaine=initialisation_fichier(dossier)
    liste = chaine.split(',') #découpe le texte dans une liste
    liste.sort()
    for i in range (len(liste)):
        res=0
        L=liste[i]
        indice_reference=ord('A') #numéro du 1er indice
        for j in range (1,len(L)-1): #il y a des guillements de trop
            res+=ord(L[j])-indice_reference+1
        compte+= res*(i+1)
    return(compte)
        

print(solve('p022_names.txt'))




