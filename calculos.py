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

    # Se a mantissa foi maior ou muito proximo a 10, ela divide a mantissa por 10 para ter 1 digito antes da virgula
    if  (mantissa >= 9.99998):
            mantissa = mantissa / 10.0
            expoente = expoente + 1
   
    return mantissa, expoente


###############################################################################################


def aproximacao(numero, n_casas_decimais, metodo):
  
    fator = 10 ** n_casas_decimais

    # --- MÉTODO 1: ARREDONDAMENTO ---
    if metodo == 1:
        # Lógica de arredondamento "metade para cima"
        numero_escalado = numero * fator
        resultado_arredondado = int(numero_escalado + math.copysign(0.5, numero_escalado))
        return resultado_arredondado / fator

    # --- MÉTODO 2: TRUNCAMENTO ---
    elif metodo == 2:
        return math.trunc(numero * fator) / fator

    # Caso o método não seja 1 ou 2
    return numero


def aproximarEsomar(x,y,n_digitos,metodo):
    return aproximacao(x+y,n_digitos,metodo)
    # aproxima cada pelo metodo escolhido e x + y


def aproximarEsubtrair(x,y,n_digitos,metodo):
    """
    Realiza uma subtração de forma inteligente:
    - Se x e y são muito próximos (risco de cancelamento subtrativo), aproxima-os primeiro.
    - Se não, subtrai primeiro para máxima precisão.
    """
    # math.isclose() verifica se os números são próximos com base em uma tolerância relativa.
    # rel_tol=1e-3 significa que eles são considerados "próximos" se a diferença
    # for menor que 0.1% do maior valor entre eles.
    if math.isclose(x, y, rel_tol=1e-3):
        print("-> Números próximos detectados! Usando método de cancelamento subtrativo.")
        # Aproxima primeiro, depois subtrai (para demonstrar o erro)
        return aproximacao(x, n_digitos, metodo) - aproximacao(y, n_digitos, metodo)
    else:
        print("-> Números distantes. Usando método de subtração normal.")
        # Subtrai primeiro, depois aproxima (para manter a precisão)
        return aproximacao(x - y, n_digitos, metodo)


def aproximarEdividir(x,y,n_digitos,metodo):
    if y == 0:
        return float('inf')
    return aproximacao(x/y,n_digitos,metodo)
    # aproxima cada pelo metodo escolhido e x / y 


def aproximarEmultiplicar(x,y,n_digitos,metodo):
    return aproximacao(x*y,n_digitos,metodo)
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

# --- EXATA ---
def propagValorExSoma(x, n_vezes):
    
    #Calcula a soma EXATA de x com ele mesmo n_vezes (x * n_vezes).

    return x * n_vezes

def propagValorExSub(x, n_vezes):
    
    #Calcula o resultado EXATO da subtração de x por ele mesmo n_vezes.
    
    if n_vezes == 0:
        return 0
    # A fórmula é x - (n-1)*x
    return x - (x * (n_vezes - 1))

def propagValorExMult(x, n_vezes):
    
    #Calcula o produto EXATO de x por ele mesmo n_vezes (x^n_vezes).
    
    return x ** n_vezes

def propagValorExDiv(x, n_vezes):
   
    #Calcula o resultado EXATO da divisão de x por ele mesmo n_vezes.
    
    if x == 0:
        if n_vezes <= 1:
            return 0
        else:
            return float('nan') # Indefinido (0/0)
    if n_vezes == 0:
        return 1
    # A fórmula é x / x^(n-1)
    return x / (x ** (n_vezes - 1))



# --- APROXIMADA ---

def propagValorApSoma(x, n_vezes, n_digitos, metodo):
    
    #Calcula a soma de x com ele mesmo n_vezes (n*x), APROXIMANDO a cada passo.
    
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
        print(f"valor aproximado {i}x -> {resultado}")
    return resultado


def propagValorApSub(x, n_vezes, n_digitos, metodo):
  
    #Calcula a subtração de x por ele mesmo n_vezes, APROXIMANDO a cada passo.
    #Ex: para n=3 -> (x - x)aprox - x
   
    if n_vezes == 0:
        return 0
    if n_vezes == 1:
        return aproximacao(x, n_digitos, metodo)

    # Começa com o próprio x
    resultado = x
    # O loop roda n_vezes - 1, pois a primeira vez já está no 'resultado'
    for i in range(n_vezes - 1):
        resultado = resultado - x
        resultado = aproximacao(resultado, n_digitos, metodo)
    return resultado


def propagValorApMult(x, n_vezes, n_digitos, metodo):
   
    #Calcula o produto de x por ele mesmo n_vezes (x^n), APROXIMANDO a cada passo.
   
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


def propagValorApDiv(x, n_vezes, n_digitos, metodo):
    
    #Calcula a divisão de x por ele mesmo n_vezes, APROXIMANDO a cada passo.
    #Ex: para n=3 -> (x / x)aprox / x
    
    if x == 0 and n_vezes > 1:
        return float('nan') # Resultado indefinido (0/0)
    if n_vezes == 0:
        return 1
    if n_vezes == 1:
        return aproximacao(x, n_digitos, metodo)

    # Começa com o próprio x
    resultado = x
    # O loop roda n_vezes - 1
    for i in range(n_vezes - 1):
        if x == 0:
            return float('inf') # Divisão por zero
        resultado = resultado / x
        resultado = aproximacao(resultado, n_digitos, metodo)
    return resultado

    

