
import time
import math
import random
from algicFinal import *
from libic import *

# ----------------------------
#  Interface gráfica
# ----------------------------
window_size = 800
window = windowIC(window_size)
resultados = []

# Escolher instância TSP
#l = readTSP2ListIC("berlin52.tsp")
l = readTSP2ListIC("Simple.tsp")
#l = readTSP2ListIC("kroA100.tsp")

drawIC(l, window)
input("Enter para continuar... ")

# Parâmetros gerais de teste
iter_default = 100

# Problemas manuais
rect = [
    (1, 0, 0),
    (2, 0, 10),
    (3, 20, 10),
    (4, 20, 0)
]
circ1 = [(i + 1,
           int(50 + 20 * math.cos(2 * math.pi * i / 10)),
           int(50 + 20 * math.sin(2 * math.pi * i / 10))) for i in range(10)]
circ2_base = [(i + 1,
                int(50 + 20 * math.cos(2 * math.pi * i / 50)),
                int(50 + 20 * math.sin(2 * math.pi * i / 50))) for i in range(50)]
circ2a = circ2_base.copy()
random.shuffle(circ2a)
circ2b = circ2a.copy()

opt_rect = distCircularIC(rect)
opt_circ1 = distCircularIC(circ1)
opt_circ2 = distCircularIC(circ2_base)

# ----------------------------
#  Validação de algoritmos
# ----------------------------
def run_and_draw(name, l, alg_func, expected, iteracoes=100, runs=1, min_successes=1):
    print(f"\n🔍 Teste: {name} | Algoritmo: {alg_func.__name__} | Iterações: {iteracoes} | Runs: {runs}")
    start = time.time()
    successes = 0
    best_sol = None
    best_dist = float('inf')
    
    for _ in range(runs):
        l_run = l.copy()
        random.shuffle(l_run)  # shuffle fora do algoritmo
        ci, cf, sol = alg_func(l_run, iteracoes)
        if cf < best_dist:
            best_sol = sol
            best_dist = cf
        if abs(cf - expected) < 0.001:
            successes += 1
    
    end = time.time()
    tempo = round((end - start) * 1000, 2)  # em milissegundos
    erro = round(best_dist - expected, 3)

    # Guardar resultados
    resultados.append({
        "Algoritmo": alg_func.__name__,
        "Teste": name,
        "Sucessos": f"{successes}/{runs}",
        "Erro": erro,
        "Tempo (ms)": tempo
    })

    # Mostrar estado
    if successes >= min_successes:
        print(f"✅ Sucesso em {successes}/{runs} runs | Melhor distância: {best_dist:.3f} | Erro: {erro:.3f} | Tempo total: {tempo}ms")
    else:
        print(f"❌ Falhou ({successes}/{runs}) | Melhor distância: {best_dist:.3f} | Erro: {erro:.3f} | Tempo total: {tempo}ms")

    drawIC(best_sol, window)
    input("Enter para continuar... ")

# Algoritmos a testar
algoritmos = [Greedy, sGreedy, pGreedy, Greedy2, rGreedy, rGreedy2, optDistCircularIC]

# ----------- RECT -----------
for alg in algoritmos:
    run_and_draw("RECT", rect, alg, opt_rect, iteracoes=100)

# ----------- CIRC1 ----------
for alg in algoritmos:
    run_and_draw("CIRC1", circ1, alg, opt_circ1, iteracoes=100)

# ----------- CIRC2a (5 iters) ----------
run_and_draw("CIRC2a", circ2a, Greedy, opt_circ2, iteracoes=5)
for alg in algoritmos[1:]:
    run_and_draw("CIRC2a", circ2a, alg, opt_circ2, iteracoes=5)

# ----------- CIRC2b (400 iters, 5 runs) ----------
for alg in algoritmos:
    run_and_draw("CIRC2b", circ2b, alg, opt_circ2, iteracoes=400, runs=5, min_successes=1)

print("\n✅ Validação concluída.")

# ----------------------------
#  Imprimir tabela final
# ----------------------------
print("\n📊 Resultados Comparativos:")
print(f"{'Algoritmo':<12} {'Teste':<8} {'Sucessos':<10} {'Erro':<8} {'Tempo (ms)':<10}")
for r in resultados:
    print(f"{r['Algoritmo']:<12} {r['Teste']:<8} {r['Sucessos']:<10} {r['Erro']:<8} {r['Tempo (ms)']:<10}")


