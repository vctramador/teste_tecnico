def is_fibonacci(n):
    # Inicializando os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Testando o programa
num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
