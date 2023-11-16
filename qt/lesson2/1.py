import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QMainWindow

from lesson2.ui_task_1 import Ui_MainWindow


# Унаследуем наш класс от простейшего графического примитива QWidget
class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_minus.clicked.connect(self.minus_click)
        self.pushButton_plus.clicked.connect(self.plus_click)
        self.pushButton_mul.clicked.connect(self.mul_click)

    def minus_click(self):
        a = int(self.lineEdit_1.text())
        b = int(self.lineEdit_2.text())
        self.lcdNumber.display(a - b)

    def plus_click(self):
        a = int(self.lineEdit_1.text())
        b = int(self.lineEdit_2.text())
        self.lcdNumber.display(a + b)

    def mul_click(self):
        a = int(self.lineEdit_1.text())
        b = int(self.lineEdit_2.text())
        self.lcdNumber.display(a * b)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Form()
    ex.show()

    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())