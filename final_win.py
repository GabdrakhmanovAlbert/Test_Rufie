from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *


class ResultWin(QWidget):
    '''Последнее окно с результатами'''

    def __init__(self, results):
        '''Инициализация окна с результатами'''
        super().__init__()
        self.results = results
        self.message = self.get_results()
        self.appear()
        self.initUI()
        self.show()

    def appear(self):
        self.setWindowTitle(TXT_FINALWIN)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.index = QLabel(TXT_INDEX + str(self.index))
        self.heartwork = QLabel(TXT_WORKHEART + self.message)

        self.main_layout.addWidget(self.index, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.heartwork, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)

    def get_results(self):
        '''Подсчёт индекса Руфье и определение сообщения'''
        self.index = (4*(int(self.results.test1) +
                      int(self.results.test2)+int(self.results.test3))-200)/10
        if self.results.age >= 15:
            if self.index >= 15:
                return TXT_RES1
            elif self.index >= 11:
                return TXT_RES2
            elif self.index >= 6:
                return TXT_RES3
            elif self.index >= 0.5:
                return TXT_RES4
            else:
                return TXT_RES5
        if self.results.age >= 13:
            if self.index >= 16.5:
                return TXT_RES1
            elif self.index >= 12.5:
                return TXT_RES2
            elif self.index >= 7.5:
                return TXT_RES3
            elif self.index >= 2:
                return TXT_RES4
            else:
                return TXT_RES5
        if self.results.age >= 11:
            if self.index >= 18:
                return TXT_RES1
            elif self.index >= 14:
                return TXT_RES2
            elif self.index >= 9:
                return TXT_RES3
            elif self.index >= 3.5:
                return TXT_RES4
            else:
                return TXT_RES5
        if self.results.age >= 9:
            if self.index >= 19.5:
                return TXT_RES1
            elif self.index >= 15.5:
                return TXT_RES2
            elif self.index >= 10.5:
                return TXT_RES3
            elif self.index >= 5:
                return TXT_RES4
            else:
                return TXT_RES5
        else:
            if self.index >= 21:
                return TXT_RES1
            elif self.index >= 17:
                return TXT_RES2
            elif self.index >= 12:
                return TXT_RES3
            elif self.index >= 6.5:
                return TXT_RES4
            else:
                return TXT_RES5
