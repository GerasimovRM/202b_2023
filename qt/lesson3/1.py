import sys
from random import choice

from PyQt5.QtWidgets import QApplication, QMainWindow

from lesson3.ui_task1 import Ui_MainWindow


class FirstForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        filename = self.lineEdit_filename.text()
        if not filename:
            self.lineEdit_output.setText("Имя файла не задано!")
            return
        try:
            with open(filename, "r", encoding="utf-8") as input_file:
                line = choice(input_file.readlines()).strip()
                self.lineEdit_output.setText(line)
        except FileNotFoundError:
            self.lineEdit_output.setText("Файл не найден!")
            return
        except UnicodeDecodeError:
            self.lineEdit_output.setText("Файл содержит символы из неподдерживаемой кодировки!")



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
    ex = FirstForm()
    ex.show()

    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())