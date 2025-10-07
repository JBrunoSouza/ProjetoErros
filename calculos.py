import math
def para_notacao_cientifica(numero):
    # Trata o caso especial do zero
    if numero == 0:
        return 0.0, 0

    # Calcula o expoente usando logaritmo na base 10
    # math.floor arredonda para baixo, nos dando a potência de 10 correta
    expoente = math.floor(math.log10(abs(numero)))


    

    # Calcula a mantissa dividindo o número pela potência de 10
    mantissa = numero / (10**expoente)
    if  (mantissa >= 9.99998):
            mantissa = mantissa / 10.0
            expoente = expoente + 1
    
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
        metodo (int): 1 para arredondamento , 2 para truncamento.
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


def aproximarEsomar(x,y,n_digitos,metodo):
    return aproximacao(x,n_digitos,metodo) + aproximacao(y,n_digitos,metodo)
    # aproxima cada pelo metodo escolhido e x + y


def aproximarEsubtrair(x,y,n_digitos,metodo):
    return aproximacao(x,n_digitos,metodo) - aproximacao(y,n_digitos,metodo)
    # aproxima cada pelo metodo escolhido e x - y 
    # cancelamento subtrativo


def aproximarEdividir(x,y,n_digitos,metodo):
    if y == 0:
        return float('inf')
    return aproximacao(x,n_digitos,metodo) / aproximacao(y,n_digitos,metodo)
    # aproxima cada pelo metodo escolhido e x / y 


def aproximarEmultiplicar(x,y,n_digitos,metodo):
    return aproximacao(x,n_digitos,metodo) * aproximacao(y,n_digitos,metodo)
    # aproxima cada pelo metodo escolhido e x * y 

###############################################################################################

#Calculo de erros

def erroAbsoluto(exato,aprox):
    return abs(exato - aprox)


def erroRelativo(exato,aprox):
    if aprox == 0: 
        return float('inf')
    return abs((exato - aprox)/aprox)

###############################################################################################

def propErroAproxMult(x, n_vezes, n_digitos, metodo):
    """
    Calcula o produto de x por ele mesmo n_vezes (x^n), APROXIMANDO a cada passo.
    """
    if n_vezes == 0:
        return 1
    if n_vezes == 1:
        return aproximacao(x, n_digitos, metodo)

    # Começa com o próprio x
    resultado = x
    # O loop roda n_vezes - 1, pois a primeira vez já está no 'resultado'
    for i in range(n_vezes - 1):
        resultado = resultado * x
        resultado = aproximacao(resultado, n_digitos, metodo)
    return resultado

def propErroAproxSoma(x, n_vezes, n_digitos, metodo):
    """
    Calcula a soma de x com ele mesmo n_vezes (n*x), APROXIMANDO a cada passo.
    """
    if n_vezes == 0:
        return 0
    if n_vezes == 1:
        return aproximacao(x, n_digitos, metodo)

    # Começa com o próprio x
    resultado = x
    # O loop roda n_vezes - 1, pois a primeira vez já está no 'resultado'
    for i in range(n_vezes - 1):
        resultado = resultado + x
        resultado = aproximacao(resultado, n_digitos, metodo)
    return resultado

def propErroExatoMult(x, n_vezes):
    """
    Calcula o produto EXATO de x por ele mesmo n_vezes (x^n_vezes).
    """
    return x ** n_vezes

def propErroExatoSoma(x, n_vezes):
    """
    Calcula a soma EXATA de x com ele mesmo n_vezes (x * n_vezes).
    """
    return x * n_vezes

    
"""
x_teste = 0.76545
y_teste = 0.76541
vezes = 0
ndigitos = 4
metodo = 1


"""
"""
print(f"aproximado arredondado: {aproximacao(x_teste,ndigitos,metodo)}")
print("-"*20)
""""""
valorexato = x_teste - y_teste
valoraproximado = aproximarEsubtrair(x_teste,y_teste,ndigitos,metodo)
erroabsoluto = erroAbsoluto(valorexato,valoraproximado)
errorelativo = erroRelativo(valorexato,valoraproximado)

"""
"""
valorexato = PropErroExato(x_teste,vezes,op)
valoraproximado = propErroAprox(x_teste,vezes,ndigitos,metodo,op)

erroabsoluto = erroAbsoluto(valorexato,valoraproximado)
errorelativo = erroRelativo(valorexato,valoraproximado)
"""

"""
print(f"valor exato: {valorexato}")
print(f"valor aproximado: {valoraproximado}")
print(f"comparação de erros EA: {erroabsoluto}")
print(f"comparação de erros ER: {errorelativo}") 
print("+"*20)
mantissa,expoente = para_notacao_cientifica(valorexato)
print(f"Notação Científica Padrão valor aprox: {mantissa:.1f} x 10^{expoente}") 
mantissa,expoente = para_notacao_cientifica(x_teste)
print(f"Notação Científica Padrão valor aprox: {mantissa:.1f} x 10^{expoente}") 
"""