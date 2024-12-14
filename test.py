from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt6 import uic
import sys
class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.setWindowTitle("Home")
        self.btnnutLogIn.clicked.connect(self.login_view)
        self.btnnutSignIn.clicked.connect(self.signup_view)
        self.pushButton_15.clicked.connect(self.home_view)
    def home_view(self):
        self.login_window = HomeWindow()
        self.login_window.show()
        self.close()
    def login_view(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()
    def signup_view(self):
        self.login_window = Signup()
        self.login_window.show()
        self.close()
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitlelogin.ui", self)
        self.setWindowTitle("Login")
        self.pushButton.clicked.connect(self.newhome_view)
        self.pushButton_2.clicked.connect(self.signup_view)
    def newhome_view(self):
        password = self.lineEdit_2.text()
        username = self.lineEdit.text()
        if username == "guest" and password == "1234":
            print("Đăng nhập thành công!")
            self.login_window = NewHome()
            self.login_window.show()
            self.close()
        elif username == "" and password == "":
            self.show_error_popup("Vui lòng nhập email và mật khẩu")
        else:
            print("Đăng nhập thất bại! Vui lòng kiểm tra lại thông tin đăng nhập.")
            self.show_error_popup("Đăng nhập thất bại! Vui lòng kiểm tra lại thông tin đăng nhập.")
    def show_error_popup(self, msg_error):
        error_box = QMessageBox()
        error_box.setWindowTitle("Lỗi")
        error_box.setIcon(QMessageBox.Icon.Warning)
        error_box.setText(msg_error)
        cancel_button = QPushButton("Cancel")
        error_box.addButton(cancel_button, QMessageBox.ButtonRole.RejectRole)
        confirm_button = QPushButton("Ok")
        error_box.addButton(confirm_button, QMessageBox.ButtonRole.RejectRole)
        error_box.exec()
    def signup_view(self):
        self.login_window = Signup()
        self.login_window.show()
        self.close()
class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitleb.ui", self)
        self.setWindowTitle("Signup")
        self.pushButton.clicked.connect(self.newhome_view)
        self.pushButton_2.clicked.connect(self.login_view)
    def newhome_view(self):
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_2.text()
        if username == "" or password == "" or email == "":
            self.show_error_popup("Vui lòng nhập email, mật khẩu hoặc email")
        else:
            print("Đăng nhập thành công!")
            self.login_window = NewHome()
            self.login_window.show()
            self.close()
    def show_error_popup(self, msg_error):
        error_box = QMessageBox()
        error_box.setWindowTitle("Lỗi")
        error_box.setIcon(QMessageBox.Icon.Warning)
        error_box.setText(msg_error)
        cancel_button = QPushButton("Cancel")
        error_box.addButton(cancel_button, QMessageBox.ButtonRole.RejectRole)
        confirm_button = QPushButton("Ok")
        error_box.addButton(confirm_button, QMessageBox.ButtonRole.RejectRole)
        error_box.exec()
    def login_view(self):
        self.login_window = Login()
        self.login_window.show()
class NewHome(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("after.ui", self)
        self.setWindowTitle("Hom3")
        self.pushButton_14.clicked.connect(self.search_view)
        self.pushButton_15.clicked.connect(self.newhome_view)
        self.pushButton_16.clicked.connect(self.cart_view)
        self.pushButton_17.clicked.connect(self.profile_view)
    def newhome_view(self):
        self.login_window = NewHome()
        self.login_window.show()
        self.close()
    def cart_view(self):
        self.login_window = Cart()
        self.login_window.show()
        self.close()
    def profile_view(self):
        self.login_window = Profile()
        self.login_window.show()
        self.close()
    def search_view(self):
        self.login_window = Search()
        self.login_window.show()
        self.close()
class Search(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("search.ui", self)
        self.setWindowTitle("Search")
        self.pushButton_15.clicked.connect(self.newhome_view)
        self.pushButton_16.clicked.connect(self.cart_view)
        self.pushButton_17.clicked.connect(self.profile_view)
        self.pushButton_7.clicked.connect(self.info1_view)
    def newhome_view(self):
        self.login_window = NewHome()
        self.login_window.show()
        self.close()
    def cart_view(self):
        self.login_window = Cart()
        self.login_window.show()
        self.close()
    def profile_view(self):
        self.login_window = Profile()
        self.login_window.show()
        self.close()
    def info1_view(self):
        self.login_window = Info1()
        self.login_window.show()
class Info1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("info1.ui", self)
        self.setWindowTitle("Details")
        self.pushButton_3.clicked.connect(self.search_view)
    def search_view(self):
        self.login_window = Search()
        self.login_window.show()
        self.close()
class Cart(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cart.ui", self)
        self.setWindowTitle("Shopping Cart")
        self.pushButton_15.clicked.connect(self.newhome_view)
        self.pushButton_16.clicked.connect(self.cart_view)
        self.pushButton_17.clicked.connect(self.profile_view)
    def newhome_view(self):
        self.login_window = NewHome()
        self.login_window.show()
        self.close()
    def cart_view(self):
        self.login_window = Cart()
        self.login_window.show()
        self.close()
    def profile_view(self):
        self.login_window = Profile()
        self.login_window.show()
        self.close()
class Profile(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("profile.ui", self)
        self.setWindowTitle("Profile")
        self.pushButton.clicked.connect(self.newhome_view)
        self.pushButton_2.clicked.connect(self.login_view)
        self.pushButton_15.clicked.connect(self.newhome_view)
        self.pushButton_16.clicked.connect(self.cart_view)
        self.pushButton_17.clicked.connect(self.profile_view)
    def newhome_view(self):
        self.login_window = NewHome()
        self.login_window.show()
        self.close()
    def cart_view(self):
        self.login_window = Cart()
        self.login_window.show()
        self.close()
    def profile_view(self):
        self.login_window = Profile()
        self.login_window.show()
        self.close()
    def newhome_view(self):
        self.login_window = NewHome()
        self.login_window.show()
        self.close()
    def login_view(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())