import xorshift
import time
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

# Lista para armazenar números primos
prime_numbers = []

# Número de primos desejados
desired_primes = 1

# Contador de tentativas
attempts = 0

# Gerar números até encontrar a quantidade desejada de primos
while len(prime_numbers) < desired_primes:
    for j in range(len(xorshift.lista)):
        start_time = time.time()
        for item in range(len(xorshift.lista_todos[0])):
            random_number = xorshift.lista_todos[j][item]
            attempts += 1
            if fermat_primality_test(random_number):
                prime_numbers.append(random_number)
                print(f"Numero primo: {random_number}")
                break
        end_time = time.time()
        total_elapsed_time = (end_time - start_time)
        if total_elapsed_time < 1:
            total_elapsed_time_ms = total_elapsed_time * 1000
            print(f"Tempo total para gerar o numero de {xorshift.lista[j]} bits: {total_elapsed_time_ms:.4f} milissegundos")
        else:
            print(f"Tempo total para gerar o numero de {xorshift.lista[j]} bits: {total_elapsed_time:.4f} segundos")

# Exibir a tabela de números primos
print("Tabela de Números Primos:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}: {prime}")

print(f"Número de tentativas para gerar {desired_primes} números primos: {attempts}")