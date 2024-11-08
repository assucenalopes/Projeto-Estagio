#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

from random import randint

def fibonacci_check(n):
    # Inicializando os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    # Verificando se o número informado é 0 ou 1, pois esses números pertencem à sequência
    if n == 0 or n == 1:
        return f"O número {n} pertence à sequência de Fibonacci."
    # Calculando a sequência de Fibonacci até que o valor de `b` seja igual ou maior que `n`
    while b < n:
        a, b = b, a + b
    # Verificando se o número informado pertence à sequência
    if b == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Gerando um número aleatório entre 0 e 100, a entrada escolhida foi um número random
number = randint(0, 100)

# Chamando a função com o número aleatório gerado
result = fibonacci_check(number)
print(f"Número sorteado: {number}")
print(result)
