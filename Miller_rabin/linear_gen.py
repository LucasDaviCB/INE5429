import secrets
import time

class LinearCongruentialGenerator:
    def __init__(self, seed=None, a=1664525, c=1013904223, m=2**32):
        if seed is None:
            # Gerar uma seed aleatória entre 40 e 4096 bits
            bit_length = secrets.choice(range(40, 4097))
            seed = secrets.randbits(bit_length)
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

# Lista de valores de bits
bit_lengths = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

# Matriz para armazenar os números gerados
numbers_matrix = []

# Gerar números para cada valor de bits e medir o tempo de execução
for bits in bit_lengths:
    lcg = LinearCongruentialGenerator(m=2**bits)
    iterations = 10000
    # Iniciar a contagem do tempo
    start_time = time.time()
    lista_gerada = []
    # Gerar múltiplos números aleatórios
    for _ in range(iterations):
        random_number = lcg.next() & ((1 << bits) - 1)  # Aplicar máscara de bits
        # Garantir que o número tenha exatamente 'bits' bits
        if random_number.bit_length() < bits:
            random_number |= (1 << (bits - 1))
        lista_gerada.append(random_number)
    # Finalizar a contagem do tempo
    end_time = time.time()
    total_elapsed_time_ms = (end_time - start_time) * 1000
    numbers_matrix.append(lista_gerada)

    print(f"Tempo total para gerar {iterations} numeros com {bits} bits: {total_elapsed_time_ms:.4f} milissegundos")
    print()
    #comentando lista gerada pois é muito grande e polue o output, descomente o trecho abaixo se quiser ver a lista gerada
    #print(f"lista gerada: {lista_gerada}")

#print(f"Matriz de numeros gerados: {numbers_matrix}")