from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(543, 390)
        
        flags = QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint
        LoginPage.setWindowFlags(flags)
        LoginPage.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        LoginPage.setMinimumSize(QtCore.QSize(543, 390))
        LoginPage.setMaximumSize(QtCore.QSize(629, 528))
        self.horizontalLayout = QtWidgets.QHBoxLayout(LoginPage)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=LoginPage)
        self.frame.setStyleSheet("background:transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 391))
        self.label.setStyleSheet("border-top-left-radius: 60%;\n"
"border-image: url(:/icons/logindesign.jpg);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=LoginPage)
        self.frame_2.setMinimumSize(QtCore.QSize(259, 372))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(parent=self.frame_2)
        self.username.setGeometry(QtCore.QRect(30, 100, 201, 31))
        self.username.setStyleSheet("border: none;\n"
"border-bottom: 2px solid black;\n"
"background-color: #ecefef;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(parent=self.frame_2)
        self.password.setGeometry(QtCore.QRect(30, 160, 201, 31))
        self.password.setStyleSheet("border: none;\n"
"border-bottom: 2px solid black;\n"
"background-color: #ecefef;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setMaxLength(32769)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.new_account = QtWidgets.QPushButton(parent=self.frame_2)
        self.new_account.setGeometry(QtCore.QRect(70, 200, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.new_account.setFont(font)
        self.new_account.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_account.setStyleSheet("background-color: none;\n"
"border: none;")
        self.new_account.setCheckable(True)
        self.new_account.setObjectName("new_account")
        self.loginbtn = QtWidgets.QPushButton(parent=self.frame_2)
        self.loginbtn.setGeometry(QtCore.QRect(70, 250, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.loginbtn.setFont(font)
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.loginbtn.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    color: white;\n"
"    background-color: black;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: black;\n"
"    background-color: white;\n"
"}")
        self.loginbtn.setCheckable(True)
        self.loginbtn.setObjectName("loginbtn")
        self.facebook = QtWidgets.QPushButton(parent=self.frame_2)
        self.facebook.setGeometry(QtCore.QRect(60, 320, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(18)
        self.facebook.setFont(font)
        self.facebook.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.facebook.setStyleSheet("border: none;")
        self.facebook.setObjectName("facebook")
        self.instagram = QtWidgets.QPushButton(parent=self.frame_2)
        self.instagram.setGeometry(QtCore.QRect(110, 320, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(18)
        self.instagram.setFont(font)
        self.instagram.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.instagram.setStyleSheet("border: none;")
        self.instagram.setObjectName("instagram")
        self.email = QtWidgets.QPushButton(parent=self.frame_2)
        self.email.setGeometry(QtCore.QRect(160, 320, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(18)
        self.email.setFont(font)
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.email.setStyleSheet("border: none;")
        self.email.setObjectName("email")
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "LOGIN"))
        self.label_2.setText(_translate("LoginPage", "L O G I N  A C C O U N T"))
        self.username.setPlaceholderText(_translate("LoginPage", "User Name"))
        self.password.setPlaceholderText(_translate("LoginPage", "Password"))
        self.new_account.setText(_translate("LoginPage", "Create new account"))
        self.loginbtn.setText(_translate("LoginPage", "L O G I N"))
        self.facebook.setText(_translate("LoginPage", "E"))
        self.instagram.setText(_translate("LoginPage", "Q"))
        self.email.setText(_translate("LoginPage", "k"))



class Ui_CreateAccount(object):
    def setupUi(self, CreateAccount):
        CreateAccount.setObjectName("CreateAccount")
        CreateAccount.resize(259, 372)
        
        flags = QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint
        CreateAccount.setWindowFlags(flags)
        
        CreateAccount.setMinimumSize(QtCore.QSize(259, 372))
        CreateAccount.setMaximumSize(QtCore.QSize(259, 372))
        CreateAccount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3 = QtWidgets.QLabel(parent=CreateAccount)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(parent=CreateAccount)
        self.username.setGeometry(QtCore.QRect(30, 100, 201, 31))
        self.username.setStyleSheet("border: none;\n"
"border-bottom: 2px solid black;\n"
"background-color: #ecefef;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(parent=CreateAccount)
        self.password.setGeometry(QtCore.QRect(30, 160, 201, 31))
        self.password.setStyleSheet("border: none;\n"
"border-bottom: 2px solid black;\n"
"background-color: #ecefef;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setMaxLength(32769)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.password.setObjectName("password")
        self.createbtn = QtWidgets.QPushButton(parent=CreateAccount)
        self.createbtn.setGeometry(QtCore.QRect(70, 230, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.createbtn.setFont(font)
        self.createbtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.createbtn.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    color: white;\n"
"    background-color: black;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: black;\n"
"    background-color: white;\n"
"}")
        self.createbtn.setCheckable(True)
        self.createbtn.setObjectName("createbtn")
        self.backbtn = QtWidgets.QPushButton(parent=CreateAccount)
        self.backbtn.setGeometry(QtCore.QRect(70, 280, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.backbtn.setFont(font)
        self.backbtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backbtn.setStyleSheet("background-color: none;\n"
"border: none;")
        self.backbtn.setCheckable(True)
        self.backbtn.setObjectName("backbtn")
        self.frame = QtWidgets.QFrame(parent=CreateAccount)
        self.frame.setGeometry(QtCore.QRect(-20, 330, 291, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(CreateAccount)
        QtCore.QMetaObject.connectSlotsByName(CreateAccount)

    def retranslateUi(self, CreateAccount):
        _translate = QtCore.QCoreApplication.translate
        CreateAccount.setWindowTitle(_translate("CreateAccount", "Create New Account"))
        self.label_3.setText(_translate("CreateAccount", "C R E A T E  A C C O U N T"))
        self.username.setPlaceholderText(_translate("CreateAccount", "User Name"))
        self.password.setPlaceholderText(_translate("CreateAccount", "Password"))
        self.createbtn.setText(_translate("CreateAccount", "C R E A T E"))
        self.backbtn.setText(_translate("CreateAccount", "B A C K"))
