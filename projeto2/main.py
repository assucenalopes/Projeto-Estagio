import random
import string


def counter_a(texto):
    # Convertendo toda a string para maiúsculas, para não ter diferença entre "a" e "A"
    texto = texto.upper()

    # Contando a quantidade de ocorrências de 'A'
    counter = texto.count('A')

    # Verificando se a letra 'A' está presente e exibindo o resultado
    if counter > 0:
        return f"A letra 'a' aparece {counter} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."


# Gerando uma string aleatória de tamanho random entre 1 e 20
size_string = random.randint(1,20)
string_random = ''.join(random.choice(string.ascii_letters + string.digits + " ") for _ in range(size_string))

# Chamando a função com a string aleatória gerada
result = counter_a(string_random)
print(f"String aleatória gerada: {string_random}")
print(result)
