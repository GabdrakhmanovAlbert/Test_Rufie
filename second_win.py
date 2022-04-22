from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from instr import *
from final_win import ResultWin


class Results():
    '''Результаты заполнения текстовых полей'''

    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3


class TestWin(QWidget):
    '''Окно для заполнения тестов'''

    def __init__(self):
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
        '''Интерфейс окна с тестами'''
        self.main_layout = QHBoxLayout()
        self.v_line1 = QVBoxLayout()
        self.v_line2 = QVBoxLayout()

        self.descr_name = QLabel(TXT_NAME)
        self.descr_age = QLabel(TXT_AGE)
        self.instr1 = QLabel(TXT_TEST1)
        self.instr2 = QLabel(TXT_TEST2)
        self.timer_txt = QLabel(TXT_TIMER)
        self.instr3 = QLabel(TXT_TEST3)
        self.btn_start1 = QPushButton(TXT_STARTEST1)
        self.btn_start2 = QPushButton(TXT_STARTEST2)
        self.btn_start3 = QPushButton(TXT_STARTEST3)
        self.btn_send = QPushButton(TXT_SENDRESULTS)
        self.input_name = QLineEdit(TXT_HINTNAME)
        self.input_age = QLineEdit(TXT_HINTAGE)
        self.input_result1 = QLineEdit(TXT_HINTEST1)
        self.input_result2 = QLineEdit(TXT_HINTEST2)
        self.input_result3 = QLineEdit(TXT_HINTEST3)

        self.v_line1.addWidget(self.descr_name, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.input_name, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.descr_age, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.input_age, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.instr1, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.btn_start1, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.input_result1, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.instr2, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.btn_start2, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.instr3, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.btn_start3, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.input_result2, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.input_result3, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.btn_send, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.timer_txt, alignment=Qt.AlignRight)

        self.main_layout.addLayout(self.v_line1)
        self.main_layout.addLayout(self.v_line2)
        self.setLayout(self.main_layout)

    def connects(self):
        '''Обработка событий'''
        self.btn_send.clicked.connect(self.next_win)
        self.btn_start1.clicked.connect(self.first_test)
        self.btn_start2.clicked.connect(self.second_test)
        self.btn_start3.clicked.connect(self.final_test)

    def next_win(self):
        '''Переход на следующее окно'''
        if self.is_normal_input():
            self.results = Results(self.input_age.text(),
                                   self.input_result1.text(),
                                   self.input_result2.text(),
                                   self.input_result3.text())
            self.final_win = ResultWin(self.results)
            self.hide()
        else:
            print('Неверные данные')

    def first_test(self):
        '''Первый тест. Таймер для замера пульса'''
        global time
        time = QTime(0, 0, 16)
        self.timer_format = 'hh:mm:ss'
        self.is_different_colours = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.timer.start(1000)

    def second_test(self):
        '''Второй тест.'''
        global time
        time = QTime(0, 0, 31)
        self.timer_format = 'ss'
        self.is_different_colours = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.timer.start(1500)

    def final_test(self):
        '''Третий последний тест.'''
        global time
        time = QTime(0, 1, 1)
        self.timer_format = 'hh:mm:ss'
        self.is_different_colours = True
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.timer.start(1000)

    def timer_event(self):
        '''Изменение показаний таймеров'''
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString(self.timer_format))
        self.timer_txt.setFont(QFont('Times', 28, QFont.Bold))
        if self.is_different_colours:
            if time.toString('mm') >= '01' or int(time.toString('ss')) == 15:
                self.timer_txt.setStyleSheet("color: rgb(0,255,0)")
            elif int(time.toString('ss')) == 45:
                self.timer_txt.setStyleSheet("color: rgb(0,0,0)")
        else:
            self.timer_txt.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def is_normal_input(self):
        '''Возвращает True, если пользователь ввёл правильные данные'''
        fio_list = self.input_name.text().split()
        if len(fio_list) != 3:
            print('len')
            return False
        for name in fio_list:
            if not name.istitle():
                print('title')
                return False

        if not self.input_age.text().isdigit():
            print('wrong age')
            return False
        elif int(self.input_age.text()) >= 300:
            print('too large age')
            return False

        return True
