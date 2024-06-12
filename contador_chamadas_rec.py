contador_de_chamadas = 0

def fibo_rec(n):
    global contador_de_chamadas
    contador_de_chamadas += 1
    
    if n <= 1:
        return n
    
    return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_rec_memo(n, memo=None):
    global contador_de_chamadas
    contador_de_chamadas += 1
    
    if memo is None:
        memo = {}
    
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fibo_rec_memo(n-1, memo) + fibo_rec_memo(n-2, memo)
    
    return memo[n]


num = int(input("Digite um número para calcular o Fibonacci: "))


contador_de_chamadas = 0
resultado_fibo_rec = fibo_rec(num)
chamadas_fibo_rec = contador_de_chamadas
print(f"\nResultado de fibo_rec({num}): {resultado_fibo_rec}")
print(f"Chamadas recursivas sem memoização: {chamadas_fibo_rec}")

print("------------------------------")


contador_de_chamadas = 0
resultado_fibo_rec_memo = fibo_rec_memo(num)
chamadas_fibo_rec_memo = contador_de_chamadas
print(f"\nResultado de fibo_rec_memo({num}): {resultado_fibo_rec_memo}")
print(f"Chamadas recursivas com memoização: {chamadas_fibo_rec_memo}")


diferenca_chamadas = chamadas_fibo_rec - chamadas_fibo_rec_memo
print(f"\nDiferença de chamadas recursivas: {diferenca_chamadas}")