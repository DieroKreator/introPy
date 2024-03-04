# 1 - imports / bibliotecas

# 2 - Classes

# 3 - Métodos e Funcoes
# def = definition = definicao
def print_hi(name):

    print(f'Oi, {name}') # a partir do Python 3

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

# estrutura de identificacao / execucao do script
if __name__ == '__main__':
    print_hi('Diego')

    # chamar a funcao de calculo da area do retángulo
    resultado = calcular_area_do_retangulo(3, 4)
    print(f'A area do retângulo é de {resultado} m2')
