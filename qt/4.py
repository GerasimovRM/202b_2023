import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(300, 300, 300, 300)
        # А также его заголовок
        self.setWindowTitle('Первая программа')

        self.btn1 = QPushButton("Собака", self)
        self.btn1.move(50, 150)
        self.btn1.clicked.connect(self.who_are_you)

        self.btn2 = QPushButton("Кошка", self)
        self.btn2.move(200, 150)
        self.btn2.clicked.connect(self.who_are_you)


        self.label = QLabel(self)
        self.label.move(50, 50)
        self.label.setText("Кто вы?")

    def who_are_you(self):
        btn = self.sender()
        self.label.setText(f"Вы: {btn.text()}")
        self.label.resize(self.label.sizeHint())




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
    ex = Example()
    ex.show()

    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())