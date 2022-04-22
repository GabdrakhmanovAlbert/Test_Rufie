from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from second_win import TestWin


class HelloWin(QWidget):
    '''Первое окно приветствия программы'''

    def __init__(self):
        '''Инициализация окна'''
        super().__init__()
        self.appear()
        self.initUI()
        self.connects()
        self.show()

    def appear(self):
        '''Появление окна'''
        self.setWindowTitle(TXT_TITLE)
        self.move(WIN_X, WIN_Y)
        self.resize(WIN_WIDTH, WIN_HEIGHT)

    def initUI(self):
        '''Инициализация элементов интерфейса'''
        self.layout = QVBoxLayout()
        self.welcome = QLabel(TXT_HELLO)
        self.instruction = QLabel(TXT_INSTRUCTION)
        self.begin_butt = QPushButton(TXT_NEXT)

        self.layout.addWidget(self.welcome, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.begin_butt, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def connects(self):
        '''Обработка событий (нажатие на кнопку)'''
        self.begin_butt.clicked.connect(self.next_win)

    def next_win(self):
        '''Переход на новый экран'''
        self.second_win = TestWin()
        self.hide()


app = QApplication([])
first_win = HelloWin()
app.exec_()
