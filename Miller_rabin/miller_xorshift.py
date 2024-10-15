import xorshift
import time

def miller_rabin(n, k=5):
    """Realiza o teste de primalidade de Miller-Rabin em n com k iterações."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Escreve n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def is_composite(a):
        """Verifica se a é um testemunho de que n é composto."""
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    # Realiza k testes
    for _ in range(k):
        a = xorshift.xorshift.next() % (n - 4) + 2
        if is_composite(a):
            return False

    return True

# Lista para armazenar números primos
prime_numbers = []

# Número de primos desejados
desired_primes = 1

# Contador de tentativas
attempts = 0

# Gerar números até encontrar a quantidade desejada de primos
while len(prime_numbers) < desired_primes: # Gerar números até encontrar a quantidade desejada de primos
    for j in range(len(xorshift.lista)): #percorre a lista de bits (40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096), que são as linhas da matriz de números gerados
        start_time = time.time()
        for item in range(len(xorshift.lista_todos[0])): #aqui é feita a iteração com base no tamanho de cada linha (em colunas), que depende do valor de iterações feitas no xorshift.py
            random_number = xorshift.lista_todos[j][item] #seleciona um numero com base nos valores de j e item (linha e coluna) da matriz lista_todos (que é a matriz com todos os números, de todos os bit sizes) para atribuir a random_number
            attempts += 1 #soma 1 ao contador de tentativas
            if miller_rabin(random_number): # realiza o teste de primalidade de Miller-Rabin com o número adquirido no passo anterior
                prime_numbers.append(random_number) # se o número for primo, adiciona o número a lista de números primos, printa o número e quebra o loop
                print(f"Numero primo: {random_number}")
                break # Sai do loop interno se encontrar um primo
        end_time = time.time()
        total_elapsed_time_ms = (end_time - start_time)
        print(f"Tempo total para gerar o numero de {xorshift.lista[j]} bits: {total_elapsed_time_ms:.4f} segundos")

# Exibir a tabela de números primos
'''print("Tabela de Números Primos:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}: {prime}")'''

# Exibir o tempo total decorrido e o número de tentativas
#print(f"Tempo total para gerar {desired_primes} números primos: {total_elapsed_time_ms:.4f} milissegundos")
print(f"Número de tentativas para gerar {desired_primes} números primos: {attempts}")
