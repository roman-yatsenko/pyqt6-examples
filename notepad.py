import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QMessageBox,
    QTextEdit,
    QFileDialog,
    QInputDialog,
    QFontDialog,
    QColorDialog,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QTextCursor, QColor


class MainWindow(QMainWindow):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setMinimumSize(400, 500)
        self.setWindowTitle("PyQt Notepad")
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        """Створення дій"""
        self.quit_act = QAction("&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        """Налаштування меню"""
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.quit_act)


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
