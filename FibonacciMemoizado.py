def fibonacci(n , memo = {}):
    if n < 3:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
n = 7
resultado = fibonacci(n)
print(f'A posição {n} de fibonacci é: {resultado}')
