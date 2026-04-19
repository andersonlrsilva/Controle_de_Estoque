from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(300, 401)
        login.setMinimumSize(QSize(295, 0))
        self.groupBox = QGroupBox(login)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 9, 282, 382))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txtUsuario = QLineEdit(self.groupBox)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(20, 210, 241, 26))
        self.txtSenha = QLineEdit(self.groupBox)
        self.txtSenha.setObjectName(u"txtSenha")
        self.txtSenha.setGeometry(QRect(20, 280, 241, 26))
        self.txtSenha.setEchoMode(QLineEdit.EchoMode.Password)
        self.groupBtn = QGroupBox(self.groupBox)
        self.groupBtn.setObjectName(u"groupBtn")
        self.groupBtn.setGeometry(QRect(10, 329, 261, 41))
        self.btnEntrar = QPushButton(self.groupBtn)
        self.btnEntrar.setObjectName(u"btnEntrar")
        self.btnEntrar.setGeometry(QRect(30, 10, 81, 26))
        self.btnSair = QPushButton(self.groupBtn)
        self.btnSair.setObjectName(u"btnSair")
        self.btnSair.setGeometry(QRect(150, 10, 81, 26))
        self.labelSenha = QLabel(self.groupBox)
        self.labelSenha.setObjectName(u"labelSenha")
        self.labelSenha.setGeometry(QRect(20, 260, 49, 16))
        self.labelUsuario = QLabel(self.groupBox)
        self.labelUsuario.setObjectName(u"labelUsuario")
        self.labelUsuario.setGeometry(QRect(20, 190, 49, 16))
        self.labelTitle = QLabel(self.groupBox)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(20, 50, 241, 101))

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(
            QCoreApplication.translate("login", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "login", u"Login no Sistema", None))
        self.groupBtn.setTitle("")
        self.btnEntrar.setText(
            QCoreApplication.translate("login", u"Entrar", None))
        self.btnSair.setText(
            QCoreApplication.translate("login", u"Sair", None))
        self.labelSenha.setText(
            QCoreApplication.translate("login", u"Senha", None))
        self.labelUsuario.setText(
            QCoreApplication.translate("login", u"Usuario", None))
        self.labelTitle.setText(QCoreApplication.translate(
            "login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">CONTROLE DE </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">ESTOQUE 2.0</span></p></body></html>", None))
    # retranslateUi
