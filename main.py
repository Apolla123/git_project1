import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
import sqlite3


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Кофе")

        # Создание главного виджета и размещение его на главном окне
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Создание вертикального контейнера для размещения виджетов
        layout = QVBoxLayout(self.centralWidget)

        # Получение информации о кофе из базы данных
        coffee_info = self.get_coffee_info()

        # Отображение информации о кофе
        for info in coffee_info:
            id_label = QLabel(f"ID: {info['ID']}")
            name_label = QLabel(f"Название сорта: {info['Название сорта']}")
            roast_label = QLabel(f"Степень обжарки: {info['Степень обжарки']}")
            grind_label = QLabel(f"Молотый/в зернах: {info['Молотый/в зернах']}")
            taste_label = QLabel(f"Описание вкуса: {info['Описание вкуса']}")
            price_label = QLabel(f"Цена: {info['Цена']}")
            volume_label = QLabel(f"Объем упаковки: {info['Объем упаковки']}")

            layout.addWidget(id_label)
            layout.addWidget(name_label)
            layout.addWidget(roast_label)
            layout.addWidget(grind_label)
            layout.addWidget(taste_label)
            layout.addWidget(price_label)
            layout.addWidget(volume_label)

    def get_coffee_info(self):
        # Подключение к базе данных
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        # Выполнение SQL-запроса для извлечения данных
        cursor.execute("SELECT * FROM coffee")

        # Получение результатов запроса
        coffee_info = []
        for row in cursor.fetchall():
            info = {
                'ID': row[0],
                'Название сорта': row[1],
                'Степень обжарки': row[2],
                'Молотый/в зернах': row[3],
                'Описание вкуса': row[4],
                'Цена': row[5],
                'Объем упаковки': row[6]
            }
            coffee_info.append(info)

        # Закрытие подключения к базе данных
        connection.close()

        return coffee_info


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
