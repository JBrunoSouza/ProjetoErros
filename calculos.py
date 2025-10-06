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

def aproximacao(numero,n_digitos,metodo):
    n_digitos = n_digitos + 1
    #metodo 1: arrendondamento
    if (metodo == 1):
        if numero == 0:
            return 0
        else:
            # Usa matemática para encontrar a "ordem de grandeza" do número
            # math.log10 consegue o expoente ao colocar o numero na base 10
            # math.floor pega a parte inteira do expoente
            # Soma mais 1 para...................................................................................................
            potencia = math.floor(math.log10(abs(numero))) + 1
            
            
            # Calcula o fator para arredondamento
            fator = 10 ** (n_digitos - potencia)
            
            # Arredonda o número escalado e depois desfaz a escala
            return round(numero * fator) / fator
    

    #metodo 2: truncamento
    elif(metodo == 2):
        if numero == 0:
            return 0
        else:
            # A lógica para encontrar a potência e o fator é a mesma do arredondamento
            potencia = math.floor(math.log10(abs(numero))) + 1

            fator = 10 ** (n_digitos - potencia)
            
            # A MUDANÇA ESTÁ AQUI: usamos math.trunc() em vez de round()
            # math.trunc() "corta" a parte decimal, efetivamente truncando o número.
            return math.trunc(numero * fator) / fator
        
###############################################################################################

## funções aritimeticas basicas com metodos aproximação

def somarEaproximar(x,y,n_digitos,metodo):
    return aproximacao(x + y,n_digitos,metodo)
    # x + y e aproxima pelo metodo escolhido

def subtrairEaproximar(x,y,n_digitos,metodo):
    return aproximacao(x - y,n_digitos,metodo)
    # x - y e aproxima pelo metodo escolhido



def dividirEaproximar(x,y,n_digitos,metodo):
    if y == 0: return float('inf')
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
    if aprox == 0: return float('inf')
    return abs((exato - aprox)/aprox)


def propErroAprox(x,y,n_vezes,n_digitos,metodo,operacao):
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
    
# --- Exemplo de Teste (baseado no projeto) ---
# Problema: Some 0.56786 dez vezes com 4 dígitos por truncamento.
x_teste = 0.76545
y_teste = 0.76541
n_somas = 1
digitos = 4
metodo_trunc = 1
operacao = 2

print(f"valor aproximado arredondado {aproximacao(x_teste,digitos,1)}")
print(f"valor aproximado truncado {aproximacao(x_teste,digitos,2)}")

#valor_exato = PropErroExato(x_teste,n_somas,operacao)
#valor_aproximado = propErroAprox(x_teste,y_teste,n_somas, digitos, metodo_trunc,operacao)

valor_exato = x_teste-y_teste
valor_aproximado = CancelamentoSub(x_teste,y_teste,digitos,metodo_trunc)

#print("---------------------------------------------------------------------------")
#print(f"Valor Exato: {valor_exato}")
#print(f"Valor Aproximado (com propagação de erro): {valor_aproximado}")
#print(f"Erro Absoluto: {erroAbsoluto(valor_exato, valor_aproximado):.6f}")
#print(f"Erro Relativo: {erroRelativo(valor_exato, valor_aproximado)*100:.4f}%")

mantissa,expoente = para_notacao_cientifica(valor_exato,False)
print(f"Notação Científica Padrão: {mantissa:.1f} x 10^{expoente}")








