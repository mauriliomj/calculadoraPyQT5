import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, \
    QPushButton, QLineEdit, QSizePolicy, QLabel, QMessageBox
from datetime import datetime


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        dataEHoraNow = datetime.now()
        dataEHoraNow = dataEHoraNow.strftime('%A %d %B %y %I:%M')

        self.setWindowTitle('Calculadora')
        self.setFixedSize(500, 600)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.display.setDisabled(False)
        self.display.setStyleSheet(
            '* {background: white; color black; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        copia = QPushButton('Copiar')
        copia.setCheckable(True)
        copia.clicked.connect(self.copiarColar)
        self.adicionaBtn(copia, 0, 4, 1, 1)

        self.dataEHora(QLabel(dataEHoraNow), 5, 3, 1, 2)

        self.addBotoes(QPushButton('7'), 1, 0, 1, 1)
        self.addBotoes(QPushButton('8'), 1, 1, 1, 1)
        self.addBotoes(QPushButton('9'), 1, 2, 1, 1)
        self.addBotoes(QPushButton('<-'), 1, 3, 1, 1, lambda: self.display.setText(self.display.text()[:-1]),
                       'background: orange; color: white; font-wheight: 700;')
        self.addBotoes(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''), 'background: red; color: white;'
                                                                                       ' font-wheight: 700;')
        self.addBotoes(QPushButton('4'), 2, 0, 1, 1)
        self.addBotoes(QPushButton('5'), 2, 1, 1, 1)
        self.addBotoes(QPushButton('6'), 2, 2, 1, 1)
        self.addBotoes(QPushButton('/'), 2, 3, 1, 1)
        self.addBotoes(QPushButton('*'), 2, 4, 1, 1)
        self.addBotoes(QPushButton('1'), 3, 0, 1, 1)
        self.addBotoes(QPushButton('2'), 3, 1, 1, 1)
        self.addBotoes(QPushButton('3'), 3, 2, 1, 1)
        self.addBotoes(QPushButton('-'), 4, 2, 1, 1)
        self.addBotoes(QPushButton('.'), 4, 0, 1, 1)
        self.addBotoes(QPushButton('0'), 4, 1, 1, 1)
        self.addBotoes(QPushButton('+'), 3, 3, 2, 1)
        self.addBotoes(QPushButton('='), 3, 4, 2, 1, self.igual, 'background: blue; color: white; font-wheigth: 700')

        self.setCentralWidget(self.cw)

    def copiarColar(self):
        cc = QApplication.clipboard()
        cc.clear(mode=cc.Clipboard)
        cc.setText(self.display.text(), mode=cc.Clipboard)
        QMessageBox.about(self, 'Resultado', 'Copiado para área de transferência!')

    def adicionaBtn(self, btn, row, col, rowspan, colspan):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

    def dataEHora(self, btn, row, col, rowspan, colspan):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

    def addBotoes(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Conta inválida.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clipboard = app.clipboard()
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()