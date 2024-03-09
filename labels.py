import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("Приклад QLabel")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Створення QLabel для відображення у головному вікні"""
        hello_label = QLabel(self)
        hello_label.setText("Привіт!")
        hello_label.move(105, 15)
        image = "images/world.png"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
