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

while len(prime_numbers) < desired_primes: # Gerar números até encontrar a quantidade desejada de primos
    for j in range(len(xorshift.lista)): #percorre a lista de bits (40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096), que são as linhas da matriz de números gerados
        start_time = time.time()
        for item in range(len(xorshift.lista_todos[0])): #aqui é feita a iteração com base no tamanho de cada linha (em colunas), que depende do valor de iterações feitas no xorshift.py
            random_number = xorshift.lista_todos[j][item]  #seleciona um numero com base nos valores de j e item (linha e coluna) da matriz lista_todos (que é a matriz com todos os números, de todos os bit sizes) para atribuir a random_number
            attempts += 1 #soma 1 ao contador de tentativas
            if fermat_primality_test(random_number):  # realiza o teste de primalidade de fermat com o número adquirido no passo anterior
                prime_numbers.append(random_number)  # se o número for primo, adiciona o número a lista de números primos, printa o número e quebra o loop
                print(f"Numero primo: {random_number}")
                break  # Sai do loop interno se encontrar um primo
        end_time = time.time()
        total_elapsed_time = (end_time - start_time)  # Calcula o tempo total decorrido
        if total_elapsed_time < 1:
            total_elapsed_time_ms = total_elapsed_time * 1000  # Converte para milissegundos caso o valor seja menor que 1 segundo
            print(f"Tempo total para gerar o numero de {xorshift.lista[j]} bits: {total_elapsed_time_ms:.4f} milissegundos")
        else:
            print(f"Tempo total para gerar o numero de {xorshift.lista[j]} bits: {total_elapsed_time:.4f} segundos")

# Exibir a tabela de números primos
print("Tabela de Números Primos:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}: {prime}")

print(f"Número de tentativas para gerar {desired_primes} números primos: {attempts}")
