import time
import linear_gen
import secrets

# Função para realizar o teste de primalidade de Fermat
def fermat_primality_test(n, k=5):  # número de testes
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Realiza o teste de Fermat k vezes
    for _ in range(k):
        # Seleciona um número aleatório a no intervalo [2, n-2]
        a = secrets.randbelow(n - 3) + 2
        # Se a^(n-1) % n != 1, então n não é primo
        if pow(a, n - 1, n) != 1:
            return False
    # Se todos os testes passaram, n é provavelmente primo
    return True

# Lista para armazenar números primos encontrados
prime_numbers = []

# Número de primos desejados
desired_primes = 1

# Contador de tentativas
attempts = 0

# Lista de valores de bits para gerar números
bit_lengths = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

# Inicializar o gerador de números aleatórios Linear Congruential Generator
lcg = linear_gen.LinearCongruentialGenerator()

# Gerar números até encontrar a quantidade desejada de primos
while len(prime_numbers) < desired_primes:
    #percorre a lista de bits (40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096), que são as linhas da matriz de números gerados
    for j in range(len(linear_gen.bit_lengths)):
        start_time = time.time()
        #aqui é feita a iteração com base no tamanho de cada linha (em colunas), que depende do valor de iterações feitas no linear_gen.py
        for item in range(len(linear_gen.numbers_matrix[0])):
            #seleciona um numero com base nos valores de j e item (linha e coluna) da matriz numbers_matrix (que é a matriz com todos os números, de todos os bit sizes) para atribuir a random_number
            random_number = linear_gen.numbers_matrix[j][item]
            #soma 1 ao contador de tentativas
            attempts += 1
            #realiza o teste de primalidade de fermat com o número adquirido no passo anterior
            if fermat_primality_test(random_number):
                #se o número for primo, adiciona o número a lista de números primos, printa o número e quebra o loop
                prime_numbers.append(random_number)
                print(f"Numero primo: {random_number}")
                break
        end_time = time.time()
        total_elapsed_time = (end_time - start_time)
        #exibe o tempo total decorrido, convertendo para milissegundos se for menor que 1 segundo
        if total_elapsed_time < 1:
            total_elapsed_time_ms = total_elapsed_time * 1000
            print(f"Tempo total para gerar o numero de {linear_gen.bit_lengths[j]} bits: {total_elapsed_time_ms:.4f} milissegundos")
        else:
            print(f"Tempo total para gerar o numero de {linear_gen.bit_lengths[j]} bits: {total_elapsed_time:.4f} segundos")

# Exibir a tabela de números primos encontrados
print("Tabela de Números Primos:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}: {prime}")

# Exibir o número de tentativas realizadas
print(f"Número de tentativas para gerar {desired_primes} números primos: {attempts}")