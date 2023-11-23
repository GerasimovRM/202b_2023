import sys
from random import choice

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from lesson3.ui_task2 import Ui_MainWindow


class FirstForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.filename = ""

        self.pushButton.clicked.connect(self.click_button)
        self.pushButton_2.clicked.connect(self.open_file)
        self.radioButton.clicked.connect(self.click_rbutton)

    def click_button(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as input_file:
                line = choice(input_file.readlines()).strip()
                self.lineEdit_output.setText(line)
        except FileNotFoundError:
            self.lineEdit_output.setText("Файл не найден!")
            return
        except UnicodeDecodeError:
            self.lineEdit_output.setText("Файл содержит символы из неподдерживаемой кодировки!")

    def open_file(self):
        dialog_window_filename = QFileDialog.getOpenFileNames(self, "Выберите файл", "", "Text file (*.txt);;All files (*)")[0]
        if not dialog_window_filename:
            self.filename = ""
        else:
            self.filename = dialog_window_filename
            self.lineEdit_filename.setText(dialog_window_filename if self.radioButton.isChecked() else dialog_window_filename.split("/")[-1])

    def click_rbutton(self):
        self.lineEdit_filename.setText(self.filename if self.radioButton.isChecked() else self.filename.split("/")[-1])




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