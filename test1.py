from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt6 import uic
import sys
class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitleb.ui", self)
        self.setWindowTitle("Home")
    def home_view(self):
        self.login_window = HomeWindow()
        self.login_window.show()
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())