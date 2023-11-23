import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QPointF
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.flag = False

        self.pushButton.clicked.connect(self.draw_circles)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.setBrush(QColor(255, 255, 0))  # Установка кисти

            for _ in range(10):  # Отрисовка 10 окружностей
                x = randint(0, self.width())
                y = randint(0, self.height())
                diameter = randint(10, 100)
                qp.drawEllipse(QPointF(x, y), diameter, diameter)

    def draw_circles(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
