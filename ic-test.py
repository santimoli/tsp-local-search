import math
import random
import sys
import time
from libic import*
from algicFinal import *

# ------------------
#   Execucao...
# ------------------

w = windowIC(800)

#l = readTSP2ListIC("berlin52.tsp")
#l = readTSP2ListIC("Simple.tsp")
l = readTSP2ListIC("kroA100.tsp")

drawIC(l,w)
random.shuffle(l)
input("Enter para continuar... ")
print("Optimizing...")

iter = 100
if len(sys.argv) > 1:
    iter = int(sys.argv[1])

st = time.process_time() 

#####TESTAR ALGORITMOS#######################################

#(ci,cf,lopt) = optDistCircularIC(l,iter)
(ci,cf,lopt) = Greedy(l,iter)
#(ci,cf,lopt)  = sGreedy(l,iter)
#(ci,cf,lopt)  = pGreedy(l,iter)
#(ci,cf,lopt) = rGreedy(l,iter)
#(ci,cf,lopt) = rGreedy2(l,iter)

##############################################################

et = time.process_time()
#print("DISTÂNCIA ci:",ci, "-> cf:",cf)
print("DISTÂNCIA ci:", ci, "-> cf:", str(cf).replace('.', ','))
print(f"CPU time: {(et - st) * 1000:.3f} ms".replace(".", ","))  

drawIC(lopt,w)

input("Enter para continuar... ")

