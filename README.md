# Simulador de Propagação de Erros Númericos

## Sobre o Projeto: 

Este projeto é um **Simulador de Propragação de Erros Númericos** desenvolvido para a disciplina de Cálculo Númerico da Universidade Federal do Vale so São Francisco (UNIVASF).

O objetivo principal é aplicar os conceitos teóricos de erros de arredondamento e truncamento em operações aritméticas, demonstrando como a precisão finita de um sistema computacional afeta o resultado de cálculos sequenciais. A aplicação foi projetada para funcionar como uma calculadora de precisão limitada, permitindo ao usuário analisar os efeitos da propagação de erros.


## Funcionalidades Implementadas 

O simulador foi desenvolvido para atender às seguintes especificações:

-  **Entrada de Dados:** Permite ao usuário inserir dois números em ponto flutuante (`x` e `y`), a operação a ser realizada e o número de dígitos significativos para o cálculo.
 
-  **Operações Aritméticas:** Suporta as quatro operações básicas: soma, subtração, multiplicação e divisão.

-  **Controle de Precisão:** O usuário pode escolher entre dois métodos para ajustar a precisão do resultado:
        - **Arredondamento:** Ajusta o resultado para o número de dígitos significativos especificado, seguindo a regra de arredondamento padrão.
        - **Truncamento:** "Corta" o resultado no número de dígitos significativos especificado, descartando os demais.
   
-  **Análise de Erros:** Para cada operação, o programa calcula e exibe:
        - O **valor exato** (calculado com a precisão máxima da linguagem).
        - O **valor aproximado** (obtido após aplicar o método de ajuste).
        - O **Erro Absoluto** ($E_a = |Valor_{Exato} - Valor_{Aproximado}|$).
        - O **Erro Relativo** ($E_r = \frac{|Valor_{Exato} - Valor_{Aproximado}|}{|Valor_{Exato}|}$).


## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal utilizada para toda a lógica do simulador.
- **PyQt6:** Biblioteca utilizada para a construção da interface gráfica do usuário (GUI), proporcionando uma experiência de uso mais interativa e amigável.


## Estrutura do Código

O código-fonte está organizado nos seguintes arquivos:

- `calculos.py`: Contém as funções matemáticas essenciais, como as operações aritméticas básicas e as lógicas para arredondamento e truncamento de dígitos significativos.

- `programa.py`: Implementa a lógica principal da aplicação, incluindo uma interface inicial via linha de comando para testes.

- `main.py`: Será o ponto de entrada para a interface gráfica desenvolvida com PyQt6.
    
- `.gitignore`: Configurado para ignorar arquivos e pastas gerados automaticamente (ex: `__pycache__/`).
    
- `LICENSE`: Arquivo de licença do projeto.
    
- `README.md`: Este arquivo.


## Como Executar o Projeto

Para executar o simulador em seu ambiente local, siga os passos abaixo:

1. **Clone o repositório:** 
```
    git clone https://github.com/JBrunoSouza/ProjetoErros
    cd ProjetoErros
```

2. **Crie e ative um ambiente virtual (recomendado):**
```
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No Linux ou macOS
    source venv/bin/activate
```

3. **Instale as dependências:**
```
    pip install PyQt6
```

4. **Execute a aplicação:**
```
    python main.py 
```

    
 ## Equipe 

 - Anna Angélica Costa de Souza 
 - José Bruno de Souza Alves 
 - Júlia Novais Pereira



