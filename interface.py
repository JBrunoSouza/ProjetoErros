import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFrame, QGroupBox, QMessageBox,
    QButtonGroup
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import calculos

class SimuladorErro(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador de Propagação de Erros")
        self.setFixedSize(1050, 620)
        self.setStyleSheet("background-color: #f4fbef; color: black;")

        header = QLabel("Simulador de Propagação de Erros")
        header.setStyleSheet("""
            background-color: #4caf50; color: white; padding: 10px 15px; font-weight: bold;
        """)
        header.setFont(QFont("Arial", 16))
        header.setAlignment(Qt.AlignmentFlag.AlignLeft)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(15)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        left_layout.setSpacing(12)

        def label(text):
            lbl = QLabel(text)
            lbl.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            lbl.setStyleSheet("color: black;")
            return lbl
            
        def make_radio(text):
            rb = QRadioButton(text)
            rb.setFont(QFont("Arial", 10))
            rb.setStyleSheet("""
                QRadioButton { border: 1px solid #4caf50; border-radius: 8px; padding: 6px 15px 6px 10px; color: black; background-color: white; spacing: 8px; }
                QRadioButton:checked { background-color: #c8e6c9; border: 2px solid #4caf50; }
                QRadioButton::indicator { width: 14px; height: 14px; }
            """)
            return rb

        modo_group = QGroupBox("Modo de Cálculo")
        modo_group.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        modo_layout = QHBoxLayout()
        
        self.op_padrao_rb = make_radio("Operação Padrão")
        self.op_padrao_rb.setChecked(True)
        self.prop_rb = make_radio("Propagação")
        
        self.op_padrao_rb.toggled.connect(self.atualizar_modo_calculo)

        modo_layout.addWidget(self.op_padrao_rb)
        modo_layout.addWidget(self.prop_rb)
        modo_group.setLayout(modo_layout)
        left_layout.addWidget(modo_group)
        
        self.modo_button_group = QButtonGroup(self)
        self.modo_button_group.addButton(self.op_padrao_rb)
        self.modo_button_group.addButton(self.prop_rb)

        left_layout.addWidget(label("Valor de X:"))
        self.x_input = QLineEdit()
        self.x_input.setPlaceholderText("Ex: 0.76545")
        self.x_input.setFixedHeight(35)
        self.x_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #4caf50; border-radius: 6px; padding-left: 8px; }")
        left_layout.addWidget(self.x_input)

        self.y_label = label("Valor de Y:")
        left_layout.addWidget(self.y_label)
        self.y_input = QLineEdit()
        self.y_input.setPlaceholderText("Ex: 0.76541 ou 1000")
        self.y_input.setFixedHeight(35)
        self.y_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #4caf50; border-radius: 6px; padding-left: 8px; }")
        left_layout.addWidget(self.y_input)

       
        left_layout.addWidget(label("Nº de Casas Decimais:"))
        self.casas_input = QLineEdit() # Variável renomeada
        self.casas_input.setPlaceholderText("Ex: 4")
        self.casas_input.setFixedHeight(35)
        self.casas_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #4caf50; border-radius: 6px; padding-left: 8px; }")
        left_layout.addWidget(self.casas_input)
        
        left_layout.addWidget(label("Operação:"))
        op_layout = QGridLayout()
        op_layout.setSpacing(10)
        self.soma_rb, self.mult_rb = make_radio("Soma"), make_radio("Multiplicação")
        self.sub_rb, self.div_rb = make_radio("Subtração"), make_radio("Divisão")
        self.soma_rb.setChecked(True) 
        op_layout.addWidget(self.soma_rb, 0, 0); op_layout.addWidget(self.mult_rb, 0, 1)
        op_layout.addWidget(self.sub_rb, 1, 0); op_layout.addWidget(self.div_rb, 1, 1)
        left_layout.addLayout(op_layout)
        
        self.op_button_group = QButtonGroup(self)
        for btn in [self.soma_rb, self.mult_rb, self.sub_rb, self.div_rb]:
            self.op_button_group.addButton(btn)

        left_layout.addWidget(label("Tipo de Aproximação:"))
        approx_layout = QHBoxLayout()
        approx_layout.setSpacing(15)
        self.arr_rb, self.trunc_rb = make_radio("Arredondamento"), make_radio("Truncamento")
        self.arr_rb.setChecked(True)
        approx_layout.addWidget(self.arr_rb); approx_layout.addWidget(self.trunc_rb)
        left_layout.addLayout(approx_layout)
        
        self.approx_button_group = QButtonGroup(self)
        self.approx_button_group.addButton(self.trunc_rb); self.approx_button_group.addButton(self.arr_rb)

        calc_btn = QPushButton("CALCULAR")
        calc_btn.setFixedHeight(40)
        calc_btn.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        calc_btn.setStyleSheet("""
            QPushButton { background-color: #4caf50; color: white; border-radius: 8px; padding: 8px; }
            QPushButton:hover { background-color: #45a049; }
        """)
        calc_btn.clicked.connect(self.realizar_calculo)
        left_layout.addWidget(calc_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        divider = QFrame(); divider.setFrameShape(QFrame.Shape.VLine); divider.setStyleSheet("color: #a0a0a0;")
        
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        right_layout.setSpacing(15)
        results_title = QLabel("Resultados")
        results_title.setFont(QFont("Arial", 18, QFont.Weight.Bold)); results_title.setStyleSheet("color: black;")
        right_layout.addWidget(results_title); right_layout.addSpacing(5)
        
        self.valor_exato_label, self.valor_aprox_label = QLabel("N/A"), QLabel("N/A")
        self.erro_abs_label, self.erro_rel_label = QLabel("N/A"), QLabel("N/A")

        right_layout.addWidget(self.create_result_box("Valor Exato", self.valor_exato_label))
        right_layout.addWidget(self.create_result_box("Valor Aproximado", self.valor_aprox_label))
        right_layout.addWidget(self.create_result_box("Erro Absoluto", self.erro_abs_label))
        right_layout.addWidget(self.create_result_box("Erro Relativo", self.erro_rel_label))

        main_layout.addLayout(left_layout, 1); main_layout.addWidget(divider); main_layout.addLayout(right_layout, 1)
        
        final_layout = QVBoxLayout(self)
        final_layout.setContentsMargins(0, 0, 0, 0); final_layout.setSpacing(0)
        final_layout.addWidget(header); final_layout.addLayout(main_layout)

    def atualizar_modo_calculo(self):
        self.y_label.setText("Nº de Operações:" if self.prop_rb.isChecked() else "Valor de Y:")

    def create_result_box(self, title, value_label):
        box = QGroupBox()
        box.setFixedHeight(85)
        box.setStyleSheet("QGroupBox { border: 1px solid #4caf50; border-radius: 8px; background-color: white; margin-top: 0.5em; }")
        layout = QVBoxLayout(); layout.setContentsMargins(10, 5, 10, 5)
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 10, QFont.Weight.Bold)); title_label.setStyleSheet("color: #4caf50;")
        value_label.setFont(QFont("Arial", 12, QFont.Weight.Bold)); value_label.setStyleSheet("color: black;")
        layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(value_label, alignment=Qt.AlignmentFlag.AlignCenter)
        box.setLayout(layout)
        return box

    def realizar_calculo(self):
        try:
            x = float(self.x_input.text().replace(',', '.'))
            n_casas = int(self.casas_input.text()) # MUDANÇA AQUI
            metodo = 1 if self.arr_rb.isChecked() else 2
            valor_exato = 0
            valor_aproximado = 0

            if self.op_padrao_rb.isChecked():
                y = float(self.y_input.text().replace(',', '.'))
                if self.soma_rb.isChecked():
                    valor_exato, valor_aproximado = x + y, calculos.aproximarEsomar(x, y, n_casas, metodo)
                elif self.sub_rb.isChecked():
                    valor_exato, valor_aproximado = x - y, calculos.aproximarEsubtrair(x, y, n_casas, metodo)
                elif self.mult_rb.isChecked():
                    valor_exato, valor_aproximado = x * y, calculos.aproximarEmultiplicar(x, y, n_casas, metodo)
                elif self.div_rb.isChecked():
                    if y == 0: self.mostrar_erro("Divisão por zero não é permitida."); return
                    valor_exato, valor_aproximado = x / y, calculos.aproximarEdividir(x, y, n_casas, metodo)
            else:
                n_vezes = int(self.y_input.text())
                if self.soma_rb.isChecked():
                    valor_exato, valor_aproximado = calculos.propagValorExSoma(x, n_vezes), calculos.propagValorApSoma(x, n_vezes, n_casas, metodo)
                elif self.sub_rb.isChecked():
                    valor_exato, valor_aproximado = calculos.propagValorExSub(x, n_vezes), calculos.propagValorApSub(x, n_vezes, n_casas, metodo)
                elif self.mult_rb.isChecked():
                    valor_exato, valor_aproximado = calculos.propagValorExMult(x, n_vezes), calculos.propagValorApMult(x, n_vezes, n_casas, metodo)
                elif self.div_rb.isChecked():
                    valor_exato, valor_aproximado = calculos.propagValorExDiv(x, n_vezes), calculos.propagValorApDiv(x, n_vezes, n_casas, metodo)



            erro_abs = calculos.erroAbsoluto(valor_exato, valor_aproximado)
            erro_rel = calculos.erroRelativo(valor_exato, valor_aproximado)
            
            # Função interna para formatar a saída em notação científica
            def formatar_saida(valor):
                if valor is None or math.isnan(valor): return "Indefinido (NaN)"
                if math.isinf(valor): return "Infinito"
                precisao = 4 # Precisão fixa para a mantissa na exibição
                mantissa, expoente = calculos.para_notacao_cientifica(valor)
                # Retorna o texto formatado como rich text para o <sup>
                return f"{mantissa:.{precisao}f} x 10<sup>{expoente}</sup>"

            # Atualiza os labels dos resultados
            self.valor_exato_label.setText(formatar_saida(valor_exato))
            self.valor_aprox_label.setText(formatar_saida(valor_aproximado))
            self.erro_abs_label.setText(formatar_saida(erro_abs))
            

            if erro_rel is None or math.isnan(erro_rel): 
                erro_rel_texto = "Indefinido (NaN)"
            elif math.isinf(erro_rel): 
                erro_rel_texto = "Infinito %"
            else: 
 
                erro_rel_texto = f"{erro_rel * 100:.4f} %"
                
            self.erro_rel_label.setText(erro_rel_texto)

        except ValueError: 
            # Esta mensagem de erro agora só aparecerá para entradas realmente inválidas
            self.mostrar_erro("Por favor, insira valores numéricos válidos. Verifique se o 'Nº de Operações' é um número inteiro.")
        except Exception as e: 
            self.mostrar_erro(f"Ocorreu um erro inesperado: {e}")

    def mostrar_erro(self, mensagem):
        msg = QMessageBox(); msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Erro de Entrada"); msg.setInformativeText(mensagem)
        msg.setWindowTitle("Erro"); msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimuladorErro()
    window.show()
    sys.exit(app.exec())