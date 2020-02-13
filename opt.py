M=[[1,1,1,1],[0,1,1,0],[0,1,9,1],[1,1,1,1]]
M[0][0]='P'

def printM(M):
    x='| '
    y='+'
    for i in range(len(M)):
        y+=' - +'
    print(y)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==1:
                x+='  | '
            elif M[i][j]==0:
                x+='x | '
            elif M[i][j]==9:
                x+='o | '
            else:
                x+='p | '
        print(x)
        print(y)
        x='| '
        
def lista(p):
    if p==1:
        return ["c","d","b","e"]
    else:
        return [y+x for y in lista(1) for x in lista(p-1)]

def posobj(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==9:
                pos=[i,j]
                return(pos)

def posjog(lista,M):
    pos=[0,0]
    for i in lista:
        if i=='c':
            if pos[0]!=0:
                if M[pos[0]-1][pos[1]]!=0:
                    pos[0]-=1
        elif i=='d':
            if pos[1]!=len(M[0])-1:
                if M[pos[0]][pos[1]+1]!=0:
                    pos[1]+=1
        elif i=='b':
            if pos[0]!=len(M)-1:
                if M[pos[0]+1][pos[1]]!=0:
                    pos[0]+=1
        else:
            if pos[1]!=0:
                if M[pos[0]][pos[1]-1]!=0:
                    pos[1]-=1
    return(pos)

def main(M):
    a=1
    obj=posobj(M)
    match=False
    printM(M)
    print('p = posição, x = bloqueio, o = objetivo')
    print()
    print('c = cima, d = direita, b = baixo, e = esquerda')
    print()
    while not match and a<len(M)*(len(M[0])):
        movs=lista(a)
        for i in movs:
            if posjog(i,M)==obj:
                match=True
                print('Um possível caminho ótimo é:',i)
        a+=1
    if not match:
        print('Não foi possível encontrar um caminho')

main(M)
