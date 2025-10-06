import math
def para_notacao_cientifica(numero, formato_projeto=False):
    # Trata o caso especial do zero
    if numero == 0:
        return 0.0, 0

    # Calcula o expoente usando logaritmo na base 10
    # math.floor arredonda para baixo, nos dando a potência de 10 correta
    expoente = math.floor(math.log10(abs(numero)))

    # Se for o formato do projeto (0.dddd...), o expoente é uma unidade maior
    if formato_projeto:
        expoente += 1

    # Calcula a mantissa dividindo o número pela potência de 10
    mantissa = numero / (10**expoente)
    
    #usar print assim:
    #mantissa,expoente = para_notacao_cientifica(valor_exato,False)
    #print(f"Notação Científica Padrão: {mantissa:.1f} x 10^{expoente}") 
    return mantissa, expoente
###############################################################################################

def aproximacao(numero, n_digitos, metodo):
    """
    Aproxima um número para um número específico de DÍGITOS SIGNIFICATIVOS.

    Args:
        numero (float): O número a ser aproximado.
        n_digitos (int): O número de dígitos significativos a ser mantido.
        metodo (int): 1 para arredondamento clássico, 2 para truncamento.
    """

    # --- MÉTODO 1: ARREDONDAMENTO CLÁSSICO POR DÍGITOS SIGNIFICATIVOS ---
    if metodo == 1:
        if numero == 0:
            return 0
        
        # Lógica para encontrar o fator de escala para N dígitos significativos
        potencia = math.floor(math.log10(abs(numero))) + 1
        fator = 10 ** (n_digitos - potencia)
        
        numero_escalado = numero * fator
        
        # Lógica de arredondamento "metade para cima"
        resultado_arredondado = int(numero_escalado + math.copysign(0.5, numero_escalado))
        
        return resultado_arredondado / fator

    # --- MÉTODO 2: TRUNCAMENTO POR DÍGITOS SIGNIFICATIVOS ---
    elif metodo == 2:
        if numero == 0:
            return 0

        # Lógica para encontrar o fator de escala para N dígitos significativos
        potencia = math.floor(math.log10(abs(numero))) + 1
        fator = 10 ** (n_digitos - potencia)
        
        return math.trunc(numero * fator) / fator

    # Caso o método não seja 1 ou 2
    return numero

def somarEaproximar(x,y,n_digitos,metodo):
    return aproximacao(x + y,n_digitos,metodo)
    # x + y e aproxima pelo metodo escolhido

def subtrairEaproximar(x,y,n_digitos,metodo):
    return aproximacao(x - y,n_digitos,metodo)
    # x - y e aproxima pelo metodo escolhido



def dividirEaproximar(x,y,n_digitos,metodo):
    if y == 0:
        return float('inf')
    return aproximacao(x / y,n_digitos,metodo)
    # x / y e aproxima pelo metodo escolhido


def multiplicarEaproximar(x,y,n_digitos,metodo):
    return aproximacao(x * y,n_digitos,metodo)
    # x * y e aproxima pelo metodo escolhido

###############################################################################################

#Calculo de erros

def erroAbsoluto(exato,aprox):
    return abs(exato - aprox)


def erroRelativo(exato,aprox):
    if aprox == 0: 
        return float('inf')
    return abs((exato - aprox)/aprox)


def propErroAprox(x,n_vezes,n_digitos,metodo,operacao):
    #metodos: 1-> arredondamento
    #         2-> truncamento

    #operacao: 1-> soma
    #          3-> multiplicação
    #          4-> divisão

    resultado = x
    

    for i in range (n_vezes-1):
        if(operacao == 1):
            resultado = resultado + x

        elif(operacao == 3):
            resultado = resultado * x

        elif(operacao == 4):
            if x == 0:
                return float('inf') 
            resultado = resultado / x

        resultado = aproximacao(resultado,n_digitos,metodo)
        print(f"resultado {resultado}")
    
    return resultado

def PropErroExato(x,n_vezes,operacao):
    #operacao: 1-> soma
    #          3-> multiplicação
    #          4-> divisão
    #obs: a subtração é no cancelamentoSUB

    resultado = x

    for i in range (n_vezes-1):
        if(operacao == 1):
            resultado = resultado + x
        
        elif(operacao == 3):
            resultado = resultado * x

        elif(operacao == 4):
            if x == 0:
                return float('inf') 
            resultado = resultado / x

    
    return resultado

def CancelamentoSub(x,y,n_digitos,metodo):
    #valoraproximado
    resultado = aproximacao(x,n_digitos,metodo) - aproximacao(y,n_digitos,metodo)
    return resultado
    #para saber o valor exato basta diminuir normal (x-y)
    

x_teste = 0.56786
y_teste = 0
vezes = 10
ndigitos = 4
metodo = 1
op = 1


""" 
TESTE CANCELAMENTO SUB
print(f"aproximado arredondado: {aproximacao(x_teste,ndigitos,metodo)}")
print("-"*20)
valorexato = x_teste - y_teste
valoraproximado = CancelamentoSub(x_teste,y_teste,ndigitos,metodo)
erroabsoluto = erroAbsoluto(valorexato,valoraproximado)
errorelativo = erroRelativo(valorexato,valoraproximado)
"""


""""
valorexato = PropErroExato(x_teste,vezes,op)
valoraproximado = propErroAprox(x_teste,vezes,ndigitos,metodo,op)

erroabsoluto = erroAbsoluto(valorexato,valoraproximado)
errorelativo = erroRelativo(valorexato,valoraproximado)

print(f"valor exato {valorexato}")
print(f"valor aproximado{valoraproximado}")
print(f"comparação de erros EA:{erroabsoluto}")
print(f"comparação de erros ER:{errorelativo}") 
mantissa,expoente = para_notacao_cientifica(x_teste,False)
print(f"Notação Científica Padrão: {mantissa:.1f} x 10^{expoente}") 
"""