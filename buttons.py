import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    """Клас для пустого вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QPushButton Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Створює та розташовує віджети у головному вікні"""
        self.times_pressed = 0
        self.name_label = QLabel("Не натискайте мене", self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60, 30)
        self.button = QPushButton("Натисни мене", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """Обробляє натиснення на кнопку"""
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Навіщо ти натиснув мене?")
            self.name_label.adjustSize()
        if self.times_pressed == 2:
            self.name_label.setText("Я попереджаю вас.")
            self.button.setText("Думаєш тобі пощастить?")
            self.button.adjustSize()
            self.button.move(70, 70)
        if self.times_pressed == 3:
            print("Вікно було закрито")
            self.close()


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
