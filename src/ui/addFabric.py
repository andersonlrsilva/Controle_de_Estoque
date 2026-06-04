# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addFabricante.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddFabricante(object):
    def setupUi(self, AddFabricante):
        if not AddFabricante.objectName():
            AddFabricante.setObjectName(u"AddFabricante")
        AddFabricante.resize(376, 590)
        self.groupBox = QGroupBox(AddFabricante)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 9, 361, 571))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 341, 41))
        self.cnpj = QVBoxLayout(self.verticalLayoutWidget)
        self.cnpj.setObjectName(u"cnpj")
        self.cnpj.setContentsMargins(0, 0, 0, 0)
        self.labelCnpj = QLabel(self.verticalLayoutWidget)
        self.labelCnpj.setObjectName(u"labelCnpj")

        self.cnpj.addWidget(self.labelCnpj)

        self.txtCnpj = QLineEdit(self.verticalLayoutWidget)
        self.txtCnpj.setObjectName(u"txtCnpj")

        self.cnpj.addWidget(self.txtCnpj)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 341, 41))
        self.fabricante = QVBoxLayout(self.verticalLayoutWidget_2)
        self.fabricante.setObjectName(u"fabricante")
        self.fabricante.setContentsMargins(0, 0, 0, 0)
        self.labelFabricante = QLabel(self.verticalLayoutWidget_2)
        self.labelFabricante.setObjectName(u"labelFabricante")

        self.fabricante.addWidget(self.labelFabricante)

        self.txtFabricante = QLineEdit(self.verticalLayoutWidget_2)
        self.txtFabricante.setObjectName(u"txtFabricante")

        self.fabricante.addWidget(self.txtFabricante)

        self.verticalLayoutWidget_3 = QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 150, 341, 41))
        self.email = QVBoxLayout(self.verticalLayoutWidget_3)
        self.email.setObjectName(u"email")
        self.email.setContentsMargins(0, 0, 0, 0)
        self.labelEmail = QLabel(self.verticalLayoutWidget_3)
        self.labelEmail.setObjectName(u"labelEmail")

        self.email.addWidget(self.labelEmail)

        self.txtEmail = QLineEdit(self.verticalLayoutWidget_3)
        self.txtEmail.setObjectName(u"txtEmail")

        self.email.addWidget(self.txtEmail)

        self.verticalLayoutWidget_4 = QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 200, 161, 41))
        self.telefoneContato = QVBoxLayout(self.verticalLayoutWidget_4)
        self.telefoneContato.setObjectName(u"telefoneContato")
        self.telefoneContato.setContentsMargins(0, 0, 0, 0)
        self.labelTelCtt = QLabel(self.verticalLayoutWidget_4)
        self.labelTelCtt.setObjectName(u"labelTelCtt")

        self.telefoneContato.addWidget(self.labelTelCtt)

        self.txtTelCtt = QLineEdit(self.verticalLayoutWidget_4)
        self.txtTelCtt.setObjectName(u"txtTelCtt")

        self.telefoneContato.addWidget(self.txtTelCtt)

        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 250, 341, 41))
        self.site = QVBoxLayout(self.verticalLayoutWidget_5)
        self.site.setObjectName(u"site")
        self.site.setContentsMargins(0, 0, 0, 0)
        self.labelSite = QLabel(self.verticalLayoutWidget_5)
        self.labelSite.setObjectName(u"labelSite")

        self.site.addWidget(self.labelSite)

        self.txtSite = QLineEdit(self.verticalLayoutWidget_5)
        self.txtSite.setObjectName(u"txtSite")

        self.site.addWidget(self.txtSite)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 330, 271, 41))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_6.addWidget(self.lineEdit_6)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 450, 141, 17))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 510, 160, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSalvar = QPushButton(self.horizontalLayoutWidget)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout.addWidget(self.btnSalvar)

        self.btnCancelar = QPushButton(self.horizontalLayoutWidget)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.horizontalLayout.addWidget(self.btnCancelar)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(7, 310, 341, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 300, 61, 16))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 380, 341, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.cmbEstado = QComboBox(self.horizontalLayoutWidget_2)
        self.cmbEstado.setObjectName(u"cmbEstado")
        self.cmbEstado.setMinimumSize(QSize(130, 0))

        self.verticalLayout_7.addWidget(self.cmbEstado)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_9.addWidget(self.lineEdit_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_8.addWidget(self.lineEdit_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayoutWidget_10 = QWidget(self.groupBox)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(290, 330, 61, 41))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.verticalLayoutWidget_10)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.lineEdit_10 = QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_10.addWidget(self.lineEdit_10)

        self.verticalLayoutWidget_11 = QWidget(self.groupBox)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(180, 200, 171, 41))
        self.telefoneContato_2 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.telefoneContato_2.setObjectName(u"telefoneContato_2")
        self.telefoneContato_2.setContentsMargins(0, 0, 0, 0)
        self.labelTelCtt_2 = QLabel(self.verticalLayoutWidget_11)
        self.labelTelCtt_2.setObjectName(u"labelTelCtt_2")

        self.telefoneContato_2.addWidget(self.labelTelCtt_2)

        self.txtTelCtt_2 = QLineEdit(self.verticalLayoutWidget_11)
        self.txtTelCtt_2.setObjectName(u"txtTelCtt_2")

        self.telefoneContato_2.addWidget(self.txtTelCtt_2)

        QWidget.setTabOrder(self.txtFabricante, self.txtCnpj)
        QWidget.setTabOrder(self.txtCnpj, self.txtEmail)
        QWidget.setTabOrder(self.txtEmail, self.txtTelCtt)
        QWidget.setTabOrder(self.txtTelCtt, self.txtTelCtt_2)
        QWidget.setTabOrder(self.txtTelCtt_2, self.txtSite)
        QWidget.setTabOrder(self.txtSite, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.cmbEstado)
        QWidget.setTabOrder(self.cmbEstado, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.btnSalvar)
        QWidget.setTabOrder(self.btnSalvar, self.btnCancelar)

        self.retranslateUi(AddFabricante)

        QMetaObject.connectSlotsByName(AddFabricante)
    # setupUi

    def retranslateUi(self, AddFabricante):
        AddFabricante.setWindowTitle(QCoreApplication.translate("AddFabricante", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddFabricante", u"Adcionar Fabricante", None))
        self.labelCnpj.setText(QCoreApplication.translate("AddFabricante", u"CNPJ", None))
        self.labelFabricante.setText(QCoreApplication.translate("AddFabricante", u"Nome Fabricante", None))
        self.labelEmail.setText(QCoreApplication.translate("AddFabricante", u"Email", None))
        self.labelTelCtt.setText(QCoreApplication.translate("AddFabricante", u"Telefone", None))
        self.labelSite.setText(QCoreApplication.translate("AddFabricante", u"Site", None))
        self.label_6.setText(QCoreApplication.translate("AddFabricante", u"Rua", None))
        self.checkBox.setText(QCoreApplication.translate("AddFabricante", u"Possui Frete Proprio", None))
        self.btnSalvar.setText(QCoreApplication.translate("AddFabricante", u"Salvar", None))
        self.btnCancelar.setText(QCoreApplication.translate("AddFabricante", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("AddFabricante", u"Endere\u00e7o", None))
        self.label_7.setText(QCoreApplication.translate("AddFabricante", u"Estado", None))
        self.label_9.setText(QCoreApplication.translate("AddFabricante", u"CEP", None))
        self.lineEdit_9.setText("")
        self.label_8.setText(QCoreApplication.translate("AddFabricante", u"Bairro", None))
        self.label_10.setText(QCoreApplication.translate("AddFabricante", u"Numero", None))
        self.labelTelCtt_2.setText(QCoreApplication.translate("AddFabricante", u"Celular / Whatsapp", None))
    # retranslateUi

