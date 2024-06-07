import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMainWindow, QMessageBox 
from login import Ui_LoginPage, Ui_CreateAccount
import resources
import webbrowser as wb

class MainApp(QWidget, Ui_LoginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.new_account.clicked.connect(self.newaccount_page)
        self.facebook.clicked.connect(self.facebooks)
        self.instagram.clicked.connect(self.igpage)
        self.email.clicked.connect(self.gmailpage)
        
    def newaccount_page(self):
        self.newacc_window = NewAcc()
        self.newacc_window.show()
        self.close()
        
    def facebooks(self):
        wb.open("https://www.facebook.com")
        
    def igpage(self):
        wb.open("https://www.instagram.com")
        
    def gmailpage(self):
        wb.open("https://mail.google.com/mail/u/0/#inbox")
        
class NewAcc(QWidget, Ui_CreateAccount):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        
        self.backbtn.clicked.connect(self.mainapp)
        
    def mainapp(self):
        self.mainapp = MainApp()
        self.mainapp.show()
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())