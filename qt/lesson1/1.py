import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Кнопка", self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.hello)
        self.btn.clicked.connect(self.hello2)
        # Зададим размер и положение нашего виджета,
        self.setGeometry(0, 300, 300, 300)
        # А также его заголовок
        self.setWindowTitle('Первая программа')

    def hello(self):
        self.btn.setText("Привет!")

    def hello2(self):
        print("привет")


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