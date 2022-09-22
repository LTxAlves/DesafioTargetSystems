RESPOSTA_POSITIVA = "O valor faz parte da sequência de Fibonacci!"
RESPOSTA_NEGATIVA = "O valor não faz parte da sequência de Fibonacci!"

if __name__ == "__main__":
    valor = input("Digite o valor a verificar: ")

    try:
        valor = int(valor)
    except:
        print("O valor digitado deve ser um número inteiro.")
        exit()

    if (valor < 0):
        print(RESPOSTA_NEGATIVA)
        exit()

    fib = [0, 1, 1]
    
    if (valor in fib):
        print(RESPOSTA_POSITIVA)
        exit()

    while (fib[-1] < valor):
        novo = fib[-2] + fib[-1]
        fib = fib[-2:] + [novo]
    
    if (valor in fib):
        print(RESPOSTA_POSITIVA)
        exit()
    
    print(RESPOSTA_NEGATIVA)
    