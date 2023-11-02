def fibonacci(n):
    a, b = 0, 1
    for num in range(n):
        a, b = b, a + b
    return a

# Imprimir los primeros 10 números de Fibonacci
for i in range(10):
    print(fibonacci(i))
