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

# Iniciar a contagem do tempo
#start_time = time.time()

# Gerar números até encontrar a quantidade desejada de primos
#xorshift.xorshift = xorshift.XorShift4096(xorshift.SeedGenerator.generate_seed(xorshift.lista[0]), xorshift.lista[0])
while len(prime_numbers) < desired_primes:
    for j in range(len(xorshift.lista)):
        start_time = time.time()
        for item in range(len(xorshift.lista_todos[0])):
            random_number = xorshift.lista_todos[j][item]
            attempts += 1
            if miller_rabin(random_number):
                prime_numbers.append(random_number)
                print(f"Numero primo: {random_number}")
                break
        end_time = time.time()
        total_elapsed_time_ms = (end_time - start_time)
        print(f"Tempo total para gerar o numero de {xorshift.lista[j]} bits: {total_elapsed_time_ms:.4f} segundos")
    #random_number = xorshift.xorshift.next()
    #attempts += 1
    #if miller_rabin(random_number):
        #prime_numbers.append(random_number)

# Finalizar a contagem do tempo
#end_time = time.time()

# Calcular o tempo total decorrido em milissegundos
#total_elapsed_time_ms = (end_time - start_time) * 1000

# Exibir a tabela de números primos
print("Tabela de Números Primos:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}: {prime}")

# Exibir o tempo total decorrido e o número de tentativas
#print(f"Tempo total para gerar {desired_primes} números primos: {total_elapsed_time_ms:.4f} milissegundos")
print(f"Número de tentativas para gerar {desired_primes} números primos: {attempts}")