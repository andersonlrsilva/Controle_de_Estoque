# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addFornecedor.ui'
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

class Ui_Fornecedor(object):
    def setupUi(self, Fornecedor):
        if not Fornecedor.objectName():
            Fornecedor.setObjectName(u"Fornecedor")
        Fornecedor.resize(376, 591)
        self.groupBox = QGroupBox(Fornecedor)
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
        self.fornecedor = QVBoxLayout(self.verticalLayoutWidget_2)
        self.fornecedor.setObjectName(u"fornecedor")
        self.fornecedor.setContentsMargins(0, 0, 0, 0)
        self.labelFornecedor = QLabel(self.verticalLayoutWidget_2)
        self.labelFornecedor.setObjectName(u"labelFornecedor")

        self.fornecedor.addWidget(self.labelFornecedor)

        self.txtFornecedor = QLineEdit(self.verticalLayoutWidget_2)
        self.txtFornecedor.setObjectName(u"txtFornecedor")

        self.fornecedor.addWidget(self.txtFornecedor)

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

        self.horizontalLayoutWidget_2 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 400, 341, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.cmbEstado = QComboBox(self.horizontalLayoutWidget_2)
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.setObjectName(u"cmbEstado")
        self.cmbEstado.setMinimumSize(QSize(130, 0))

        self.verticalLayout_7.addWidget(self.cmbEstado)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.txtCep = QLineEdit(self.horizontalLayoutWidget_2)
        self.txtCep.setObjectName(u"txtCep")

        self.verticalLayout_9.addWidget(self.txtCep)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.txtBairro = QLineEdit(self.horizontalLayoutWidget_2)
        self.txtBairro.setObjectName(u"txtBairro")

        self.verticalLayout_8.addWidget(self.txtBairro)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

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

        self.verticalLayoutWidget_6 = QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 350, 261, 41))
        self.site_2 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.site_2.setObjectName(u"site_2")
        self.site_2.setContentsMargins(0, 0, 0, 0)
        self.labelRua = QLabel(self.verticalLayoutWidget_6)
        self.labelRua.setObjectName(u"labelRua")

        self.site_2.addWidget(self.labelRua)

        self.txtRua = QLineEdit(self.verticalLayoutWidget_6)
        self.txtRua.setObjectName(u"txtRua")

        self.site_2.addWidget(self.txtRua)

        self.verticalLayoutWidget_12 = QWidget(self.groupBox)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(280, 350, 71, 41))
        self.telefoneContato_6 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.telefoneContato_6.setObjectName(u"telefoneContato_6")
        self.telefoneContato_6.setContentsMargins(0, 0, 0, 0)
        self.labelNumero = QLabel(self.verticalLayoutWidget_12)
        self.labelNumero.setObjectName(u"labelNumero")

        self.telefoneContato_6.addWidget(self.labelNumero)

        self.txtNumero = QLineEdit(self.verticalLayoutWidget_12)
        self.txtNumero.setObjectName(u"txtNumero")

        self.telefoneContato_6.addWidget(self.txtNumero)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 310, 51, 16))
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 320, 341, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.chboxFrete = QCheckBox(self.groupBox)
        self.chboxFrete.setObjectName(u"chboxFrete")
        self.chboxFrete.setGeometry(QRect(10, 460, 91, 17))
        QWidget.setTabOrder(self.txtFornecedor, self.txtCnpj)
        QWidget.setTabOrder(self.txtCnpj, self.txtEmail)
        QWidget.setTabOrder(self.txtEmail, self.txtTelCtt)
        QWidget.setTabOrder(self.txtTelCtt, self.txtTelCtt_2)
        QWidget.setTabOrder(self.txtTelCtt_2, self.txtSite)
        QWidget.setTabOrder(self.txtSite, self.cmbEstado)
        QWidget.setTabOrder(self.cmbEstado, self.txtCep)
        QWidget.setTabOrder(self.txtCep, self.txtBairro)
        QWidget.setTabOrder(self.txtBairro, self.btnSalvar)
        QWidget.setTabOrder(self.btnSalvar, self.btnCancelar)

        self.retranslateUi(Fornecedor)

        QMetaObject.connectSlotsByName(Fornecedor)
    # setupUi

    def retranslateUi(self, Fornecedor):
        Fornecedor.setWindowTitle(QCoreApplication.translate("Fornecedor", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Fornecedor", u"Adcionar Fornecedor", None))
        self.labelCnpj.setText(QCoreApplication.translate("Fornecedor", u"CNPJ", None))
        self.labelFornecedor.setText(QCoreApplication.translate("Fornecedor", u"Fornecedor", None))
        self.labelEmail.setText(QCoreApplication.translate("Fornecedor", u"Email", None))
        self.labelTelCtt.setText(QCoreApplication.translate("Fornecedor", u"Telefone", None))
        self.labelSite.setText(QCoreApplication.translate("Fornecedor", u"Site", None))
        self.btnSalvar.setText(QCoreApplication.translate("Fornecedor", u"Salvar", None))
        self.btnCancelar.setText(QCoreApplication.translate("Fornecedor", u"Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("Fornecedor", u"Estado", None))
        self.cmbEstado.setItemText(0, QCoreApplication.translate("Fornecedor", u"Acre", None))
        self.cmbEstado.setItemText(1, QCoreApplication.translate("Fornecedor", u"Alagoas", None))
        self.cmbEstado.setItemText(2, QCoreApplication.translate("Fornecedor", u"Amap\u00e1", None))
        self.cmbEstado.setItemText(3, QCoreApplication.translate("Fornecedor", u"Amazonas", None))
        self.cmbEstado.setItemText(4, QCoreApplication.translate("Fornecedor", u"Bahia", None))
        self.cmbEstado.setItemText(5, QCoreApplication.translate("Fornecedor", u"Cear\u00e1", None))
        self.cmbEstado.setItemText(6, QCoreApplication.translate("Fornecedor", u"Distrito Federal", None))
        self.cmbEstado.setItemText(7, QCoreApplication.translate("Fornecedor", u"Esp\u00edrito Santo", None))
        self.cmbEstado.setItemText(8, QCoreApplication.translate("Fornecedor", u"Goi\u00e1s", None))
        self.cmbEstado.setItemText(9, QCoreApplication.translate("Fornecedor", u"Maranh\u00e3o", None))
        self.cmbEstado.setItemText(10, QCoreApplication.translate("Fornecedor", u"Mato Grosso", None))
        self.cmbEstado.setItemText(11, QCoreApplication.translate("Fornecedor", u"Mato Grosso do Sul", None))
        self.cmbEstado.setItemText(12, QCoreApplication.translate("Fornecedor", u"Minas Gerais", None))
        self.cmbEstado.setItemText(13, QCoreApplication.translate("Fornecedor", u"Par\u00e1", None))
        self.cmbEstado.setItemText(14, QCoreApplication.translate("Fornecedor", u"Para\u00edba", None))
        self.cmbEstado.setItemText(15, QCoreApplication.translate("Fornecedor", u"Paran\u00e1", None))
        self.cmbEstado.setItemText(16, QCoreApplication.translate("Fornecedor", u"Pernambuco", None))
        self.cmbEstado.setItemText(17, QCoreApplication.translate("Fornecedor", u"Piau\u00ed", None))
        self.cmbEstado.setItemText(18, QCoreApplication.translate("Fornecedor", u"Rio de Janeiro", None))
        self.cmbEstado.setItemText(19, QCoreApplication.translate("Fornecedor", u"Rio Grande do Norte", None))
        self.cmbEstado.setItemText(20, QCoreApplication.translate("Fornecedor", u"Rio Grande do Sul", None))
        self.cmbEstado.setItemText(21, QCoreApplication.translate("Fornecedor", u"Rond\u00f4nia", None))
        self.cmbEstado.setItemText(22, QCoreApplication.translate("Fornecedor", u"Roraima", None))
        self.cmbEstado.setItemText(23, QCoreApplication.translate("Fornecedor", u"Santa Catarina", None))
        self.cmbEstado.setItemText(24, QCoreApplication.translate("Fornecedor", u"S\u00e3o Paulo", None))
        self.cmbEstado.setItemText(25, QCoreApplication.translate("Fornecedor", u"Sergipe", None))
        self.cmbEstado.setItemText(26, QCoreApplication.translate("Fornecedor", u"Tocantins", None))

        self.label_9.setText(QCoreApplication.translate("Fornecedor", u"CEP", None))
        self.txtCep.setText("")
        self.label_8.setText(QCoreApplication.translate("Fornecedor", u"Bairro", None))
        self.labelTelCtt_2.setText(QCoreApplication.translate("Fornecedor", u"Celular / Whatsapp", None))
        self.labelRua.setText(QCoreApplication.translate("Fornecedor", u"Rua", None))
        self.labelNumero.setText(QCoreApplication.translate("Fornecedor", u"Numero", None))
        self.label.setText(QCoreApplication.translate("Fornecedor", u"Endere\u00e7o", None))
        self.chboxFrete.setText(QCoreApplication.translate("Fornecedor", u"Possui Frete", None))
    # retranslateUi

