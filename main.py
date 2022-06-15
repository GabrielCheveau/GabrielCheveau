

def somar(num_a, num_b):
    return num_a + num_b


def subtrair(num_a, num_b):
    return num_a - num_b


def multiplicar(num_a, num_b):
    return num_a * num_b


def dividir(num_a, num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError:
        return 'Não dividir por zero'


if __name__ == '__main__':

    # Chamar a definição somar e mostrar o resultado
    Resultado = somar(21, 29)
    print(f'Um mais o outro é: {Resultado}')

    # Chamar a definição subtrair e mostrar o resultado
    Resultado = subtrair(90, 40)
    print(f'Um menos o outro é: {Resultado}')

    # Chamar a definição multiplicar e mostrar o resultado
    Resultado = multiplicar(5, 10)
    print(f'Um vezes o outro é: {Resultado}')

    # Chamar a definição dividir e mostrar o resultado
    Resultado = dividir(100, 2)
    print(f'Um dividido pelo outro é: {Resultado}')


def test_somar():

    # 1 - Configura
    num_a = 21
    num_b = 29
    resultado_esperado = 50

    # 2 - Executa
    resultado_obtido = somar(num_a, num_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_subtrair():
    # 1 - Prepara / Configura
    # 1.1 - Dados de Entrada / Valores do Teste
    num_a = 90
    num_b = 40

    #1.2 - Resultados Esperados
    resultado_esperado = 50


def test_multiplicar():
    num_a = 5
    num_b = 10
    resultado_esperado = 50


def test_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    num_a = 100
    num_b = 2

    # 1.2 - Resultados Esperados
    resultado_esperado = 50

    # 2 - Executa
    resultado_obtido = dividir(num_a, num_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def test_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    num_a = 100
    num_b = 0

    # 1.2 - Resultados Esperados
    resultado_esperado = 'Não dividir por zero'

    # 2 - Executa
    resultado_obtido = dividir(num_a, num_b)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado

# TDD - Test Driven Development






