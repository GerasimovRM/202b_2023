import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber


# Унаследуем наш класс от простейшего графического примитива QWidget
class FirstForm(QWidget):
    def __init__(self):
        sad'kas;dj' \
           ';aksjd'
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.buttons = []
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(300, 300, 600, 200)
        # А также его заголовок
        self.setWindowTitle('Первая форма')
        base_ord = ord('a')
        for i in range(13):
            btn = QPushButton(chr(base_ord + i), self)
            btn.resize(30, 30)
            btn.move(i * 30, 30)
            btn.clicked.connect(self.click)
            self.buttons.append(btn)
        for i in range(13, 26):
            btn = QPushButton(chr(base_ord + i), self)
            btn.resize(30, 30)
            btn.move((i - 13) * 30, 70)
            btn.clicked.connect(self.click)
            self.buttons.append(btn)

    def click(self):
        print(self.sender().text())



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