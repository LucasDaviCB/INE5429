import time
import linear_gen
import secrets

# Função para realizar o teste de primalidade de Miller-Rabin
def miller_rabin(n, k=5):  # número de testes
    # Verifica se o número é menor ou igual a 1
    if n <= 1:
        return False
    # Verifica se o número é 2 ou 3, que são primos
    if n <= 3:
        return True
    # Verifica se o número é par
    if n % 2 == 0:
        return False

    # Escreve n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Realiza o teste de Miller-Rabin k vezes
    for _ in range(k):
        # Seleciona um número aleatório a no intervalo [2, n-2]
        a = secrets.randbelow(n - 3) + 2
        # Calcula x = a^d % n
        x = pow(a, d, n)
        # Se x é 1 ou n-1, continua para o próximo teste
        if x == 1 or x == n - 1:
            continue
        # Realiza r-1 iterações
        for _ in range(r - 1):
            # Calcula x = x^2 % n
            x = pow(x, 2, n)
            # Se x é n-1, quebra o loop interno
            if x == n - 1:
                break
        else:
            # Se nenhum dos testes passou, n não é primo
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

# Enquanto o número de primos encontrados for menor que o desejado, continue percorrendo os numeros gerados
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
            #realiza o teste de primalidade de miller_rabin com o número adquirido no passo anterior
            if miller_rabin(random_number):
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

#desnecessário, pois os números primos já são impressos quando são encontrados
'''# Exibir a tabela de números primos encontrados
print("Tabela de Números Primos:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}: {prime}")'''

# Exibir o número de tentativas realizadas
print(f"Numero de tentativas para gerar {desired_primes} numeros primos para todos os bit_sizes somados: {attempts}")