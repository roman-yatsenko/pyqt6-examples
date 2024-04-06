import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QCheckBox,
    QTextEdit,
    QDockWidget,
    QToolBar,
    QStatusBar,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("MainWindow")
        self.setUpMainWindow()
        # self.createDockWidget()
        self.createActions()
        self.createMenu()
        # self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.setStatusBar(QStatusBar())

    def createActions(self):
        """Створення дій"""
        self.quit_act = QAction("&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.full_screen_act = QAction("На весь екран", checkable=True)
        self.full_screen_act.setStatusTip("Перейти в режим на весь екран")
        self.full_screen_act.triggered.connect(self.switchToFullScreen)

    def createMenu(self):
        """Налаштування меню"""
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.quit_act)

        view_menu = self.menuBar().addMenu("Перегляд")
        apperance_submenu = view_menu.addMenu("Зовнішній вигляд")
        apperance_submenu.addAction(self.full_screen_act)

    def switchToFullScreen(self, state):
        if state:
            self.showFullScreen()
        else:
            self.showNormal()


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
