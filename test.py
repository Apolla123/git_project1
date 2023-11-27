import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF
from random import randint


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(479, 415)
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(150, 140, 181, 91)
        self.pushButton.setText("Нажми На Меня")


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.flag = False

        self.ui.pushButton.clicked.connect(self.draw_circles)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)

            for _ in range(10):
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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

