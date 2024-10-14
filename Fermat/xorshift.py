import os
import time

class XorShift4096:
    def __init__(self, seed, bit_length):
        # Inicializa o estado com 64 posições, usando a semente fornecida
        self.state = [0] * 64
        self.state[0] = seed
        self.bit_length = bit_length  # Armazena o comprimento dos bits
        for i in range(1, 64):
            # Gera o estado inicial usando a semente
            self.state[i] = self.state[i - 1] ^ (self.state[i - 1] >> 30) + i

    def next(self):
        # Gera o próximo número pseudoaleatório usando o algoritmo XorShift
        t = self.state[0]
        s = self.state[63]
        self.state[0] = s
        t ^= t << 23  # Operação de deslocamento e XOR
        t ^= t >> 17  # Operação de deslocamento e XOR
        t ^= s ^ (s >> 26)  # Operação de deslocamento e XOR com o estado anterior
        self.state[63] = t  # Atualiza o estado
        result = t + s  # Calcula o resultado final
        # Aplicar máscara para limitar ao número de bits especificado
        mask = (1 << self.bit_length) -1 
        return result & mask

class SeedGenerator:
    @staticmethod
    def generate_seed(bit_length):
        # Gera uma semente aleatória com o comprimento de bits especificado
        if bit_length < 40 or bit_length > 4096:
            # Eu acho que isso não é mais necessário (pois os valores agora estão na lista, porém por via das dúvidas, para não ter que refazer tudo, irei deixar esse ValueError)
            raise ValueError("O comprimento do bit deve estar entre 40 e 4096")
        return int.from_bytes(os.urandom(bit_length // 8), 'big')


lista = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
lista_todos = []
for item in lista:
    bit_length = item
    # Gera a semente com o comprimento de bits especificado
    seed = SeedGenerator.generate_seed(bit_length)
    # Inicializa o gerador XorShift com a semente gerada e o comprimento de bits especificado
    xorshift = XorShift4096(seed, bit_length)

    # Número de iterações para gerar múltiplos números aleatórios
    iterations = 10000

    # Iniciar a contagem do tempo
    start_time = time.time()
    lista_gerada = []
    # Gerar múltiplos números aleatórios e armazenar em uma lista temporária (é gerada essa lista temporária para cada "linha" da matriz (linhas equivalem ao número de bits 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096), cada linha terá iterations colunas)
    for _ in range(iterations):
        random_number = xorshift.next()
        lista_gerada.append(random_number)
    end_time = time.time()
    #adiciona a lista total o resultado da lista gerada
    lista_todos.append(lista_gerada)

# Calcular o tempo total decorrido em milissegundos
    total_elapsed_time_ms = (end_time - start_time) * 1000

    # Exibir os resultados
    print(f"Numero aleatorio: {random_number}")
    print(f"Tempo total para gerar o numero: {total_elapsed_time_ms:.4f} milissegundos")
    print(f"Numero de bits: {random_number.bit_length()}")
    #lista gerada causa um resultado um pouco explosivo no resultado, caso queira ver a lista gerada, descomente a linha abaixo
    #print(f"Lista gerada: {lista_gerada}")