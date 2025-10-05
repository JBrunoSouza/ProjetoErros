from calculos import somar, subtrair, dividir, multiplicar,arredondar_significativos
import math
def main():
    print("--- Simulador de Propagação de Erros ---")
    print("Por favor, insira os dois números (x e y).")

    # Pede os inputs e já converte para float
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))

    print("""
Qual operação você quer realizar?
1 -> Soma
2 -> Subtração
3 -> Multiplicação
4 -> Divisão
    """)

    # Pede a opção e já converte para int
    op = int(input("Escolha uma opção (1-4): "))

    if(op==1):
        resultado = somar(x,y)
        print(f"o resultado é {somar(x,y)}")
    elif(op==2):
        resultado = subtrair(x,y)
        print(f"o resultado é {subtrair(x,y)}")
    elif(op==3):
        resultado = dividir(x,y)
        print(f"o resultado é {dividir(x,y)}")
    elif(op==4):
        resultado = multiplicar(x,y)
        print(f"o resultado é {multiplicar(x,y)}")

    print(f"resultado {resultado}")

    print("""qual tipo de aproximação?
            1 -> arredondamento
            2 -> truncamento """)
    
    opAprox = int(input("Escolha uma opção (1-2): "))

    NumSig = int(input("Quantos numeros significativos? "))

    if(opAprox == 1):
        aprox = arredondar_significativos(resultado,NumSig)
        print(aprox)
    
    

    

# Ponto de entrada do prograclma
if __name__ == "__main__":
    main()