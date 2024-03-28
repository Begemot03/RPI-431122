import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from random import choices


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.reset.clicked.connect(self.res)
        self.gen.clicked.connect(self.generate)

    def generate(self):
        DIGIT = '1234567890'
        ALPHA_LOVER = 'qwertyuiopasdfghjklzxcvbnm'
        ALPHA_UPPER = ALPHA_LOVER.upper()
        SYMBOL = '~!@#$%^&*()_+/<>'
        line = ''
        if self.digit.isChecked():
            line += DIGIT
        if self.alpha.isChecked():
            line += ALPHA_LOVER + ALPHA_UPPER
        if self.symbol.isChecked():
            line += SYMBOL
        data = []
        for elem in range(self.count_pass.value()):
            data.append(''.join(choices(line, k=self.count_symbols.value())))
        fname = QFileDialog.getSaveFileName(self, 'Сохранить', '/passwords.txt')[0]
        with open(fname, 'w') as f:
            for elem in data:
                f.write(elem)
                f.write('\n')
        f.close()

    def res(self):
        self.count_pass.setValue(0)
        self.count_symbols.setValue(0)
        self.digit.setChecked(False)
        self.alpha.setChecked(False)
        self.symbol.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

