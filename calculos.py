import math

def somar(x,y):
    return x + y

def subtrair(x,y):
    return x - y

def dividir(x,y):
    return x/y

def multiplicar(x,y):
    return x*y

def arredondar_significativos(numero, n_digitos):
    
    if numero == 0:
        return 0
    
    # Usa matemática para encontrar a "ordem de grandeza" do número
    potencia = math.floor(math.log10(abs(numero))) + 1
    
    # Calcula o fator para arredondamento
    fator = 10 ** (n_digitos - potencia)
    
    # Arredonda o número escalado e depois desfaz a escala
    return round(numero * fator) / fator

def truncar_significativos(numero, n_digitos):
   
    if numero == 0:
        return 0
    
    # A lógica para encontrar a potência e o fator é a mesma do arredondamento
    potencia = math.floor(math.log10(abs(numero))) + 1
    
    fator = 10 ** (n_digitos - potencia)
    
    # A MUDANÇA ESTÁ AQUI: usamos math.trunc() em vez de round()
    # math.trunc() "corta" a parte decimal, efetivamente truncando o número.
    return math.trunc(numero * fator) / fator

