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
        self.quit_act = QAction(QIcon("images/exit.png"), "&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.new_act = QAction(QIcon("images/new_file.png"), "Новий")
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.triggered.connect(self.clearText)

        self.open_act = QAction(QIcon("images/open_file.png"), "Відкрити")
        self.open_act.setShortcut("Ctrl+O")
        # self.open_act.triggered.connect(self.openFile)

        self.save_act = QAction(QIcon("images/save_file.png"), "Зберегти")
        self.save_act.setShortcut("Ctrl+S")
        # self.save_act.triggered.connect(self.saveToFile)

        self.undo_act = QAction(QIcon("images/undo.png"), "Скасувати")
        self.undo_act.setShortcut("Ctrl+Z")
        self.undo_act.triggered.connect(self.text_edit.undo)

        self.redo_act = QAction(QIcon("images/redo.png"), "Повторити")
        self.redo_act.setShortcut("Ctrl+Shift+Z")
        self.redo_act.triggered.connect(self.text_edit.redo)

        self.cut_act = QAction(QIcon("images/cut.png"), "Вирізати")
        self.cut_act.setShortcut("Ctrl+X")
        self.cut_act.triggered.connect(self.text_edit.cut)

        self.copy_act = QAction(QIcon("images/copy.png"), "Копіювати")
        self.copy_act.setShortcut("Ctrl+C")
        self.copy_act.triggered.connect(self.text_edit.copy)

        self.paste_act = QAction(QIcon("images/paste.png"), "Вставити")
        self.paste_act.setShortcut("Ctrl+V")
        self.paste_act.triggered.connect(self.text_edit.paste)

        self.find_act = QAction(QIcon("images/find.png"), "Пошук")
        self.find_act.setShortcut("Ctrl+F")
        # self.find_act_act.triggered.connect(self.searchText)

        self.font_act = QAction(QIcon("images/font.png"), "Шрифт")
        self.font_act.setShortcut("Ctrl+T")
        # self.font_act_act.triggered.connect(self.chooseFont)

        self.color_act = QAction(QIcon("images/color.png"), "Колір")
        self.color_act.setShortcut("Ctrl+Shift+C")
        # self.color_act_act.triggered.connect(self.chooseFontColor)

        self.highlight_act = QAction(QIcon("images/highlight.png"), "Виділити")
        self.highlight_act.setShortcut("Ctrl+Shift+H")
        # self.color_act_act.triggered.connect(self.chooseFontBackgroundColor)

        self.about_act = QAction("Про програму")
        # self.about_act.connect(self.aboutDialog)

    def createMenu(self):
        """Налаштування меню"""
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.new_act)
        file_menu.addSeparator()
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        edit_menu = self.menuBar().addMenu("Редагувати")
        edit_menu.addAction(self.undo_act)
        edit_menu.addAction(self.redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.cut_act)
        edit_menu.addAction(self.copy_act)
        edit_menu.addAction(self.paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.find_act)

        tool_menu = self.menuBar().addMenu("Інструменти")
        tool_menu.addAction(self.font_act)
        tool_menu.addAction(self.color_act)
        tool_menu.addAction(self.highlight_act)

        help_menu = self.menuBar().addMenu("Допомога")
        help_menu.addAction(self.about_act)

    def clearText(self):
        answer = QMessageBox.question(
            self,
            "Очистка тексту",
            "Ви хочете очистити весь текст?",
            QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.Yes,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.text_edit.clear()


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
