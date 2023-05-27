A = 0
B = 1
C = 1
lista_Fibonacci = [A, B, C]

num = int(input("Digite um número para verificar se o mesmo faz parte da sequencia Fibonacci: "))
for i in range(num):
    D = B + C
    B, C = C, D
    lista_Fibonacci.append(D)

print(lista_Fibonacci)

print(f"O numero {num} pertence a sequencia Fibonacci.") if num in lista_Fibonacci \
    else f"O número {num} não pertence a sequencia Fibonacci"
