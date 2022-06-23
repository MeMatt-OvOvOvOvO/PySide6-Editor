from main import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(QSize(400, 220))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()