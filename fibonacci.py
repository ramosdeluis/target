def calcula_fibo(tamanho: int) -> list:
    result = [0, 1]

    for _ in range(tamanho):
        result.append(result[-1] + result[-2])

    return result


def valida_fibo(numero_usuario: int) -> list[bool, int]:
    """
    Recebe um número e verifica se ele faz ou não parte da sequência de Fibonacci.

    Retorna uma lista (Primeiro elemento sendo True ou False e o segundo sendo a posição, com -1 caso falso.)
    """

    RANGE_FIBO = 200

    IS_ON = True

    while IS_ON:

        fib_list = calcula_fibo(RANGE_FIBO)

        for index, numero_seq in enumerate(fib_list):
            if numero_seq == numero_usuario:
                result = [True, index]
                IS_ON = False

        RANGE_FIBO += 200

        if RANGE_FIBO > 11000:  # Limitação de tamanho da sequência que será gerada para procura
            result = [False, -1]
            IS_ON = False

    return result


if __name__ == '__main__':

    NUMERO = 0

    resultado = valida_fibo(NUMERO)
    if resultado[0]:
        print(
            f"Sim! O número {NUMERO} faz parte da sequência, sua posição é a de {resultado[1] + 1}º.")
    else:
        print(f"Desculpe... O Número {NUMERO} não faz parte da sequência.")
