import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import sqlite3


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('main.ui', self)

        self.setWindowTitle("Кофе")

        # Создание главного виджета и размещение его на главном окне
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Создание вертикального контейнера для размещения виджетов
        layout = QVBoxLayout(self.centralWidget)

        layout.addWidget(self.ui.id_label)
        layout.addWidget(self.ui.name_label)
        layout.addWidget(self.ui.roast_label)
        layout.addWidget(self.ui.grind_label)
        layout.addWidget(self.ui.taste_label)
        layout.addWidget(self.ui.price_label)
        layout.addWidget(self.ui.volume_label)

        # Получение информации о кофе из базы данных
        coffee_info = self.get_coffee_info()

        # Отображение информации о кофе
        for info in coffee_info:
            self.ui.id_label.setText(f"ID: {info['ID']}")
            self.ui.name_label.setText(f"Название сорта: {info['Название сорта']}")
            self.ui.roast_label.setText(f"Степень обжарки: {info['Степень обжарки']}")
            self.ui.grind_label.setText(f"Молотый/в зернах: {info['Молотый/в зернах']}")
            self.ui.taste_label.setText(f"Описание вкуса: {info['Описание вкуса']}")
            self.ui.price_label.setText(f"Цена: {info['Цена']}")
            self.ui.volume_label.setText(f"Объем упаковки: {info['Объем упаковки']}")

    def get_coffee_info(self):
        # Подключение к базе данных
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        # Выполнение SQL-запроса для извлечения данных
        cursor.execute("SELECT * FROM coffe")

        # Получение результатов запроса
        coffee_info = []
        for row in cursor.fetchall():
            info = {'ID': row[0], 'Название сорта': row[1], 'Степень обжарки': row[2], 'Молотый/в зернах': row[3],
                    'Описание вкуса': row[4], 'Цена': row[5], 'Объем упаковки': row[6]}
            coffee_info.append(info)

        # Закрытие соединения с базой данных
        cursor.close()
        connection.close()

        return coffee_info


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())