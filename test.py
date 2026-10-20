import csv
import time
import random
from algicFinal import optDistCircularIC, Greedy, sGreedy, pGreedy, rGreedy, rGreedy2

def carregar_instancia_tsp(nome_arquivo):
    """Carrega uma instância TSP a partir de um arquivo .tsp"""
    cidades = []
    ler_coordenadas = False
    
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            if linha.strip() == "NODE_COORD_SECTION":
                ler_coordenadas = True
                continue
            if linha.strip() == "EOF":
                break
            if ler_coordenadas:
                partes = linha.strip().split()
                if len(partes) == 3:
                    id_cidade = int(partes[0])
                    x = float(partes[1])
                    y = float(partes[2])
                    cidades.append((id_cidade, x, y))
    
    return cidades

def executar_algoritmo(algoritmo, instancia, iteracoes):
    """Executa um algoritmo e retorna métricas de performance"""
    inicio = time.time()
    
    if algoritmo == 'optDistCircularIC':
        dist_inicial, dist_final, solucao = optDistCircularIC(instancia, iteracoes)
    elif algoritmo == 'Greedy':
        dist_inicial, dist_final, solucao = Greedy(instancia, iteracoes)
    elif algoritmo == 'sGreedy':
        dist_inicial, dist_final, solucao = sGreedy(instancia, iteracoes)
    elif algoritmo == 'pGreedy':
        dist_inicial, dist_final, solucao = pGreedy(instancia, iteracoes)
    elif algoritmo == 'rGreedy':
        dist_inicial, dist_final, solucao = rGreedy(instancia, iteracoes)
    elif algoritmo == 'rGreedy2':
        dist_inicial, dist_final, solucao = rGreedy2(instancia, iteracoes)
    else:
        raise ValueError(f"Algoritmo desconhecido: {algoritmo}")
    
    tempo_execucao = (time.time() - inicio) * 1000  # ms
    return dist_final, tempo_execucao

def executar_experimentos_rGreedy2_berlin52(instancia_nome, iteracoes_list, num_execucoes, nome_arquivo):
    """Executa experimentos só com rGreedy2 na instância berlin52.tsp"""
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Instância', 'Algoritmo', 'Iterações', 'Execução', 'Custo', 'Tempo(ms)'])

        try:
            instancia = carregar_instancia_tsp(instancia_nome)
            print(f"\nCarregada instância: {instancia_nome}")
        except FileNotFoundError:
            print(f"\nArquivo {instancia_nome} não encontrado.")
            return

        algoritmo = 'rGreedy2'
        print(f"Executando {algoritmo} para {instancia_nome}...")

        for iteracoes in iteracoes_list:
            for execucao in range(1, num_execucoes + 1):
                print(f"  Execução {execucao}/{num_execucoes} para N={iteracoes}")

                # Aqui sem shuffle, pois quer testar direto
                custo, tempo = executar_algoritmo(algoritmo, instancia, iteracoes)
                writer.writerow([instancia_nome.split('.')[0], algoritmo, iteracoes, execucao, f"{custo:.2f}", f"{tempo:.2f}"])
                csvfile.flush()

# Configurações para teste com berlin52.tsp e rGreedy2
instancia_nome = 'berlin52.tsp'
iteracoes_list = [1000000]
num_execucoes = 5
nome_arquivo = 'resultados_rGreedy2_berlin52.csv'

executar_experimentos_rGreedy2_berlin52(
    instancia_nome=instancia_nome,
    iteracoes_list=iteracoes_list,
    num_execucoes=num_execucoes,
    nome_arquivo=nome_arquivo
)

print("\nExecuções concluídas! Resultados salvos em 'resultados_rGreedy2_berlin52.csv'")
