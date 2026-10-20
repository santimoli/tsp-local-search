import math
import random
import queue

####################################EXERCICIOS FICHA 3 ###################################
##########################################################################################

def Random_iCidade(id):
    return (id,random.randint(50,100),random.randint(50,100))

def RandNum():
    return random.randint(0,100)

#exercicio 1

l=(Random_iCidade(RandNum()))

#exercicio2

def distIC(iCidade1,iCidade2):
    return math.sqrt((iCidade2[1] - iCidade1[1])**2 + ( iCidade2[2] - iCidade1[2] )**2)

#exercicio 3 

def Nlistas(n):
    l=[]
    for i in range(1,n+1):
        l.append(Random_iCidade(i))
    return l
    
#exercicio 4

def distCircularIC(l): 
    d=0
    for i in range(len(l)-1):
        d += distIC(l[i],l[(i+1)])

    d += distIC(l[-1], l[0])
    return d

#exercicio 5

def trocaIC(lista, pos1, pos2):
    NovaLista = lista.copy()
    
    NovaLista[pos1], NovaLista[pos2] = NovaLista[pos2], NovaLista[pos1]
    
    return NovaLista

#exercicio 6

def trocaSeMelhorIC(lista):

    #pos1 = random.randint(0, len(l) - 1)
    #pos2 = random.randint(0, len(l) - 1)
    pos1, pos2 = random.sample(range(len(lista)), 2) 
    #pos1, pos2 = random.sample(range(len(lista)-1), 2) 
    NovaLista = trocaIC(lista, pos1, pos2)
    
    if distCircularIC(NovaLista) <= distCircularIC(lista):
        return NovaLista
    return lista  

#exercicio 7

def melhoraDistCircularIC(lista, n):
    for _ in range(n):
        lista = trocaSeMelhorIC(lista)
    return lista

############################################FUNÇÕES AUXILIARES################################

#VARIAVEIS GLOBAIS##########

k = 10
epsilon=0.001
r = 10

#############################################FUNÇÕES SUCESSORES################################

def Successors(estado):
    sucessores = []
    n = len(estado)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            vizinho = trocaIC(estado, i, j)
            custo = distCircularIC(vizinho)
            sucessores.append((vizinho, custo))
            
    return sucessores

def GetBestSuccesor(sucessores):
    Best = min(sucessores, key=distCircularIC)
    return Best

#####################################FUNÇÃO SUCESSOR INVERSÃO(AVANÇADO)#############################

def Sucessores2(estado):
    sucessores = []
    n = len(estado)
    for i in range(n - 1):
        for j in range(i + 1, n):
            vizinho = estado[:]
            vizinho[i:j+1] = reversed(vizinho[i:j+1])
            sucessores.append(vizinho)
    return sucessores

######################################ALGORITMOS GREEDY#######################################
##############################################################################################

def optDistCircularIC(l, iter):

    CurrentState = l.copy()
    lopt = melhoraDistCircularIC(CurrentState, iter)
    FinalDist = distCircularIC(lopt)

    return distCircularIC(l), FinalDist, lopt


#########################################_rGREEDY_###########################################

def Greedy(l, iter):
   
    state = l[:]
    ci = distCircularIC(state)
    
    Improvements = []
    count = 0
    
    while count < iter:

        count += 1
        CurrentDist = distCircularIC(state)
        succ = Successors(state)
        
        BestSucc, BestSuccDist = min(succ, key=lambda x: x[1]) # Escolhe o melhor sucessor (estado, custo)
        
        if BestSuccDist >= CurrentDist:
            break
        
        Improve = CurrentDist - BestSuccDist
        state = BestSucc
        Improvements.append(Improve)
        if len(Improvements) > k:
            Improvements.pop(0)
        
        if len(Improvements) == k and sum(Improvements) < epsilon:  # Se melhoria acumulada nas últimas k iterações < epsilon, para
            break
    
    cf = distCircularIC(state)
    return ci, cf, state


def rGreedy(l, iter):
   
    state = l[:]
    ci = distCircularIC(state)
    BestState = state[:]
    cf = ci
    ImproveRestarts = []
    
    for restart in range(r):
        if restart == 0:
            CurrentStates = state[:]
        else:
            CurrentStates = state[:]
            random.shuffle(CurrentStates)
        
        _, CurrentDist, CurrentState = Greedy(CurrentStates, iter)
        
        if CurrentDist < cf:
            Improve = cf - CurrentDist
            BestState = CurrentState[:]
            cf = CurrentDist
            ImproveRestarts.append(Improve)

            if len(ImproveRestarts) > k:
                ImproveRestarts.pop(0)
            
            # Paragem se melhoria acumulada é muito pequena
            if len(ImproveRestarts) == k and sum(ImproveRestarts) < epsilon:
                break
        else:
            ImproveRestarts.append(0)
            if len(ImproveRestarts) > k:
                ImproveRestarts.pop(0)
    
    return ci, cf, BestState

#########################################_sGREEDY_###########################################

def sGreedy(l, iter,b=3):
   
    state = l[:]
    ci = distCircularIC(state)
    
    Improvements = []
    count = 0

    while count < iter:
        
        count += 1
        CurrentDist = distCircularIC(state)
        succ = Successors(state)
        succ.sort(key=lambda x: x[1])
        BestSucc = succ[:b]
        ChooseSucc, ChooseDist = random.choice(BestSucc)
        
        if ChooseDist >= CurrentDist:
            break
        
        Improve = CurrentDist - ChooseDist
        state = ChooseSucc
        Improvements.append(Improve)

        if len(Improvements) > k:
            Improvements.pop(0)
        
        if len(Improvements) == k and sum(Improvements) < epsilon:
            break

    cf = distCircularIC(state)
    return ci, cf, state
   

#####################################_pGREEDY_################################################

def pGreedy(l, iter):

    state = l[:]
    ci = distCircularIC(state)
    Improvements = []

    for _ in range(iter):

        CurrentDist = distCircularIC(state)
        isImprove = False
        n = len(state)
        pos = random.randint(0, n - 1)

        for j in range(n):

            if j == pos:
                continue

            
            succ = trocaIC(state, pos, j)
            NewDist = distCircularIC(succ)

            if NewDist < CurrentDist:
                Improve = CurrentDist - NewDist
                state = succ
                Improvements.append(Improve)

                if len(Improvements) > k:
                    Improvements.pop(0)

                isImprove = True
                break  # primeira melhoria encontrada

        if not isImprove:
            break

        if len(Improvements) == k and sum(Improvements) < epsilon:
            break

    cf = distCircularIC(state)
    return ci, cf, state


######################################(AVANÇADO)######################################################


def Greedy2(l, iter):
    
    state = l[:]
    ci = distCircularIC(state)

    Improvements = []
    count = 0

    while count < iter:
        
        count += 1
        CurrentDist = distCircularIC(state)
        Succ = Sucessores2(state)
        BestSucc = GetBestSuccesor(Succ)
        BestDist = distCircularIC(BestSucc)

        # Verifica se houve melhoria
        if BestDist >= CurrentDist:
            break

        Improve = CurrentDist - BestDist
        state = BestSucc
        Improvements.append(Improve)

        if len(Improvements) > k:
            Improvements.pop(0)

        if len(Improvements) == k and sum(Improvements) < epsilon:
            break

    cf = distCircularIC(state)
    return ci, cf, state

##########################################################################################################

def rGreedy2(l, iter):
    
    state = l[:]
    ci = distCircularIC(state)

    BestState = state[:]
    cf = ci

    ImproveRestarts = []

    for restart in range(r):
        if restart == 0:
            CurrentState = state[:]
        else:
            CurrentState = state[:]
            random.shuffle(CurrentState)

        _, CurrentDist, CurrentBestState = Greedy2(CurrentState, iter)

        if CurrentDist < cf:
            Improve = cf - CurrentDist
            BestState = CurrentBestState[:]
            cf = CurrentDist

            ImproveRestarts.append(Improve)
            if len(ImproveRestarts) > k:
                ImproveRestarts.pop(0)

            if len(ImproveRestarts) == k and sum(ImproveRestarts) < epsilon:
                break
        else:
            ImproveRestarts.append(0)
            if len(ImproveRestarts) > k:
                ImproveRestarts.pop(0)

    return ci, cf, BestState




######################################################################################################
