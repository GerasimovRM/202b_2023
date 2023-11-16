import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QMainWindow, QRadioButton

from lesson2.ui_task_2 import Ui_MainWindow


# Унаследуем наш класс от простейшего графического примитива QWidget
class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_flag)

    def create_flag(self):
        """
        for radio_button in self.findChildren(QRadioButton):
            print(radio_button)
            print(radio_button.text())
        """
        # st = "radioButton_1"
        # getattr(self, 'radioButton_1_r')  # self.radioButton1
        box1 = [self.radioButton_1_b, self.radioButton_1_g, self.radioButton_1_r]
        box2 = [self.radioButton_2_b, self.radioButton_2_g, self.radioButton_2_r]
        box3 = [self.radioButton_3_b, self.radioButton_3_g, self.radioButton_3_r]
        b1 = next(filter(lambda x: x.isChecked(), box1), None)
        b2 = next(filter(lambda x: x.isChecked(), box2), None)
        b3 = next(filter(lambda x: x.isChecked(), box3), None)
        colors = [b1, b2, b3]
        colors = list(map(lambda x: x.text() if isinstance(x, QRadioButton) else "", colors))
        self.label_4.setText(f"Цвета: {', '.join(colors)}")


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