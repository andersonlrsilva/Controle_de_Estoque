# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcliente.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_addCliente(object):
    def setupUi(self, addCliente):
        if not addCliente.objectName():
            addCliente.setObjectName(u"addCliente")
        addCliente.resize(552, 670)
        self.GrupoEndereco = QGroupBox(addCliente)
        self.GrupoEndereco.setObjectName(u"GrupoEndereco")
        self.GrupoEndereco.setGeometry(QRect(10, 430, 531, 151))
        self.verticalLayoutWidget_17 = QWidget(self.GrupoEndereco)
        self.verticalLayoutWidget_17.setObjectName(u"verticalLayoutWidget_17")
        self.verticalLayoutWidget_17.setGeometry(QRect(10, 30, 281, 41))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.labelEndereco = QLabel(self.verticalLayoutWidget_17)
        self.labelEndereco.setObjectName(u"labelEndereco")
        self.labelEndereco.setMinimumSize(QSize(0, 2))
        self.labelEndereco.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_17.addWidget(self.labelEndereco)

        self.txtEndereco = QLineEdit(self.verticalLayoutWidget_17)
        self.txtEndereco.setObjectName(u"txtEndereco")

        self.verticalLayout_17.addWidget(self.txtEndereco)

        self.verticalLayoutWidget_16 = QWidget(self.GrupoEndereco)
        self.verticalLayoutWidget_16.setObjectName(u"verticalLayoutWidget_16")
        self.verticalLayoutWidget_16.setGeometry(QRect(170, 80, 171, 41))
        self.LayoutCidade = QVBoxLayout(self.verticalLayoutWidget_16)
        self.LayoutCidade.setObjectName(u"LayoutCidade")
        self.LayoutCidade.setContentsMargins(0, 0, 0, 0)
        self.labelCidade = QLabel(self.verticalLayoutWidget_16)
        self.labelCidade.setObjectName(u"labelCidade")
        self.labelCidade.setMinimumSize(QSize(0, 2))
        self.labelCidade.setMaximumSize(QSize(16777215, 12))

        self.LayoutCidade.addWidget(self.labelCidade)

        self.txtCidade = QLineEdit(self.verticalLayoutWidget_16)
        self.txtCidade.setObjectName(u"txtCidade")

        self.LayoutCidade.addWidget(self.txtCidade)

        self.verticalLayoutWidget_15 = QWidget(self.GrupoEndereco)
        self.verticalLayoutWidget_15.setObjectName(u"verticalLayoutWidget_15")
        self.verticalLayoutWidget_15.setGeometry(QRect(350, 80, 171, 41))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.labelBairro = QLabel(self.verticalLayoutWidget_15)
        self.labelBairro.setObjectName(u"labelBairro")
        self.labelBairro.setMinimumSize(QSize(0, 2))
        self.labelBairro.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_15.addWidget(self.labelBairro)

        self.txtBairro = QLineEdit(self.verticalLayoutWidget_15)
        self.txtBairro.setObjectName(u"txtBairro")

        self.verticalLayout_15.addWidget(self.txtBairro)

        self.verticalLayoutWidget_18 = QWidget(self.GrupoEndereco)
        self.verticalLayoutWidget_18.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget_18.setGeometry(QRect(300, 30, 91, 41))
        self.verticalLayout_18 = QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.verticalLayoutWidget_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 2))
        self.label_18.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_18.addWidget(self.label_18)

        self.txtNumero = QLineEdit(self.verticalLayoutWidget_18)
        self.txtNumero.setObjectName(u"txtNumero")

        self.verticalLayout_18.addWidget(self.txtNumero)

        self.verticalLayoutWidget_19 = QWidget(self.GrupoEndereco)
        self.verticalLayoutWidget_19.setObjectName(u"verticalLayoutWidget_19")
        self.verticalLayoutWidget_19.setGeometry(QRect(10, 80, 151, 41))
        self.verticalLayout_19 = QVBoxLayout(self.verticalLayoutWidget_19)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.verticalLayoutWidget_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 2))
        self.label_19.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_19.addWidget(self.label_19)

        self.cmbEstado = QComboBox(self.verticalLayoutWidget_19)
        self.cmbEstado.setObjectName(u"cmbEstado")

        self.verticalLayout_19.addWidget(self.cmbEstado)

        self.verticalLayoutWidget_20 = QWidget(self.GrupoEndereco)
        self.verticalLayoutWidget_20.setObjectName(u"verticalLayoutWidget_20")
        self.verticalLayoutWidget_20.setGeometry(QRect(400, 30, 121, 41))
        self.verticalLayout_20 = QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.verticalLayoutWidget_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 2))
        self.label_20.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_20.addWidget(self.label_20)

        self.txtCep = QLineEdit(self.verticalLayoutWidget_20)
        self.txtCep.setObjectName(u"txtCep")

        self.verticalLayout_20.addWidget(self.txtCep)

        self.GrupoContato = QGroupBox(addCliente)
        self.GrupoContato.setObjectName(u"GrupoContato")
        self.GrupoContato.setGeometry(QRect(10, 290, 531, 131))
        self.verticalLayoutWidget_8 = QWidget(self.GrupoContato)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 20, 111, 41))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.labelTel1 = QLabel(self.verticalLayoutWidget_8)
        self.labelTel1.setObjectName(u"labelTel1")
        self.labelTel1.setMinimumSize(QSize(0, 2))
        self.labelTel1.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_8.addWidget(self.labelTel1)

        self.txtTel1 = QLineEdit(self.verticalLayoutWidget_8)
        self.txtTel1.setObjectName(u"txtTel1")

        self.verticalLayout_8.addWidget(self.txtTel1)

        self.verticalLayoutWidget_7 = QWidget(self.GrupoContato)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(130, 20, 111, 41))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelTel2 = QLabel(self.verticalLayoutWidget_7)
        self.labelTel2.setObjectName(u"labelTel2")
        self.labelTel2.setMinimumSize(QSize(0, 2))
        self.labelTel2.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_7.addWidget(self.labelTel2)

        self.txtTel2 = QLineEdit(self.verticalLayoutWidget_7)
        self.txtTel2.setObjectName(u"txtTel2")

        self.verticalLayout_7.addWidget(self.txtTel2)

        self.verticalLayoutWidget_9 = QWidget(self.GrupoContato)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(250, 20, 111, 41))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.labelCelWhats = QLabel(self.verticalLayoutWidget_9)
        self.labelCelWhats.setObjectName(u"labelCelWhats")
        self.labelCelWhats.setMinimumSize(QSize(0, 2))
        self.labelCelWhats.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_9.addWidget(self.labelCelWhats)

        self.txtCel = QLineEdit(self.verticalLayoutWidget_9)
        self.txtCel.setObjectName(u"txtCel")

        self.verticalLayout_9.addWidget(self.txtCel)

        self.verticalLayoutWidget_11 = QWidget(self.GrupoContato)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(210, 70, 191, 41))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.verticalLayoutWidget_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 2))
        self.label_11.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_11.addWidget(self.label_11)

        self.txtUrl = QLineEdit(self.verticalLayoutWidget_11)
        self.txtUrl.setObjectName(u"txtUrl")

        self.verticalLayout_11.addWidget(self.txtUrl)

        self.verticalLayoutWidget_10 = QWidget(self.GrupoContato)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 70, 191, 41))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.verticalLayoutWidget_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 2))
        self.label_10.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_10.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_10.addWidget(self.lineEdit_9)

        self.GrupoCliente = QGroupBox(addCliente)
        self.GrupoCliente.setObjectName(u"GrupoCliente")
        self.GrupoCliente.setGeometry(QRect(10, 30, 531, 251))
        self.verticalLayoutWidget_3 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 150, 161, 41))
        self.labe = QVBoxLayout(self.verticalLayoutWidget_3)
        self.labe.setObjectName(u"labe")
        self.labe.setContentsMargins(0, 0, 0, 0)
        self.labelCPF = QLabel(self.verticalLayoutWidget_3)
        self.labelCPF.setObjectName(u"labelCPF")
        self.labelCPF.setMinimumSize(QSize(0, 2))
        self.labelCPF.setMaximumSize(QSize(16777215, 12))

        self.labe.addWidget(self.labelCPF)

        self.txtCpfCnpj = QLineEdit(self.verticalLayoutWidget_3)
        self.txtCpfCnpj.setObjectName(u"txtCpfCnpj")

        self.labe.addWidget(self.txtCpfCnpj)

        self.verticalLayoutWidget_2 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 361, 41))
        self.NomeFantasia = QVBoxLayout(self.verticalLayoutWidget_2)
        self.NomeFantasia.setObjectName(u"NomeFantasia")
        self.NomeFantasia.setContentsMargins(0, 0, 0, 0)
        self.labelNomeFantasia = QLabel(self.verticalLayoutWidget_2)
        self.labelNomeFantasia.setObjectName(u"labelNomeFantasia")
        self.labelNomeFantasia.setMinimumSize(QSize(0, 2))
        self.labelNomeFantasia.setMaximumSize(QSize(16777215, 12))

        self.NomeFantasia.addWidget(self.labelNomeFantasia)

        self.txtNomeFantasia = QLineEdit(self.verticalLayoutWidget_2)
        self.txtNomeFantasia.setObjectName(u"txtNomeFantasia")

        self.NomeFantasia.addWidget(self.txtNomeFantasia)

        self.verticalLayoutWidget = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 90, 361, 41))
        self.RazaoSocial = QVBoxLayout(self.verticalLayoutWidget)
        self.RazaoSocial.setObjectName(u"RazaoSocial")
        self.RazaoSocial.setContentsMargins(0, 0, 0, 0)
        self.labelRazaoSoc = QLabel(self.verticalLayoutWidget)
        self.labelRazaoSoc.setObjectName(u"labelRazaoSoc")
        self.labelRazaoSoc.setMinimumSize(QSize(0, 2))
        self.labelRazaoSoc.setMaximumSize(QSize(16777215, 12))

        self.RazaoSocial.addWidget(self.labelRazaoSoc)

        self.txtRazoaSocial = QLineEdit(self.verticalLayoutWidget)
        self.txtRazoaSocial.setObjectName(u"txtRazoaSocial")

        self.RazaoSocial.addWidget(self.txtRazoaSocial)

        self.verticalLayoutWidget_4 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(380, 30, 121, 41))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 2))
        self.label_4.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_4.addWidget(self.label_4)

        self.txtCodeCliente = QLineEdit(self.verticalLayoutWidget_4)
        self.txtCodeCliente.setObjectName(u"txtCodeCliente")
        self.txtCodeCliente.setEnabled(False)

        self.verticalLayout_4.addWidget(self.txtCodeCliente)

        self.verticalLayoutWidget_5 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(380, 90, 121, 41))
        self.TipoCliente = QVBoxLayout(self.verticalLayoutWidget_5)
        self.TipoCliente.setObjectName(u"TipoCliente")
        self.TipoCliente.setContentsMargins(0, 0, 0, 0)
        self.labelTipoCliente = QLabel(self.verticalLayoutWidget_5)
        self.labelTipoCliente.setObjectName(u"labelTipoCliente")
        self.labelTipoCliente.setMinimumSize(QSize(0, 2))
        self.labelTipoCliente.setMaximumSize(QSize(16777215, 12))

        self.TipoCliente.addWidget(self.labelTipoCliente)

        self.cmbTipoCliente = QComboBox(self.verticalLayoutWidget_5)
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.setObjectName(u"cmbTipoCliente")

        self.TipoCliente.addWidget(self.cmbTipoCliente)

        self.verticalLayoutWidget_6 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(180, 150, 251, 41))
        self.IeRg = QVBoxLayout(self.verticalLayoutWidget_6)
        self.IeRg.setObjectName(u"IeRg")
        self.IeRg.setContentsMargins(0, 0, 0, 0)
        self.labelIeRg = QLabel(self.verticalLayoutWidget_6)
        self.labelIeRg.setObjectName(u"labelIeRg")
        self.labelIeRg.setMinimumSize(QSize(0, 2))
        self.labelIeRg.setMaximumSize(QSize(16777215, 12))

        self.IeRg.addWidget(self.labelIeRg)

        self.txtIeRg = QLineEdit(self.verticalLayoutWidget_6)
        self.txtIeRg.setObjectName(u"txtIeRg")

        self.IeRg.addWidget(self.txtIeRg)

        self.verticalLayoutWidget_12 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(10, 200, 221, 41))
        self.ramoAtividade = QVBoxLayout(self.verticalLayoutWidget_12)
        self.ramoAtividade.setObjectName(u"ramoAtividade")
        self.ramoAtividade.setContentsMargins(0, 0, 0, 0)
        self.labelAtividade = QLabel(self.verticalLayoutWidget_12)
        self.labelAtividade.setObjectName(u"labelAtividade")
        self.labelAtividade.setMinimumSize(QSize(0, 2))
        self.labelAtividade.setMaximumSize(QSize(16777215, 12))

        self.ramoAtividade.addWidget(self.labelAtividade)

        self.txtAtividade = QLineEdit(self.verticalLayoutWidget_12)
        self.txtAtividade.setObjectName(u"txtAtividade")

        self.ramoAtividade.addWidget(self.txtAtividade)

        self.verticalLayoutWidget_13 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(240, 200, 141, 41))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.labelClienteDesde = QLabel(self.verticalLayoutWidget_13)
        self.labelClienteDesde.setObjectName(u"labelClienteDesde")
        self.labelClienteDesde.setMinimumSize(QSize(0, 2))
        self.labelClienteDesde.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_13.addWidget(self.labelClienteDesde)

        self.dateEditCliente = QDateEdit(self.verticalLayoutWidget_13)
        self.dateEditCliente.setObjectName(u"dateEditCliente")

        self.verticalLayout_13.addWidget(self.dateEditCliente)

        self.verticalLayoutWidget_21 = QWidget(self.GrupoCliente)
        self.verticalLayoutWidget_21.setObjectName(u"verticalLayoutWidget_21")
        self.verticalLayoutWidget_21.setGeometry(QRect(440, 150, 61, 41))
        self.campoUf = QVBoxLayout(self.verticalLayoutWidget_21)
        self.campoUf.setObjectName(u"campoUf")
        self.campoUf.setContentsMargins(0, 0, 0, 0)
        self.labelUf = QLabel(self.verticalLayoutWidget_21)
        self.labelUf.setObjectName(u"labelUf")
        self.labelUf.setMinimumSize(QSize(0, 2))
        self.labelUf.setMaximumSize(QSize(16777215, 12))

        self.campoUf.addWidget(self.labelUf)

        self.cmboxUf = QComboBox(self.verticalLayoutWidget_21)
        self.cmboxUf.addItem("")
        self.cmboxUf.setObjectName(u"cmboxUf")

        self.campoUf.addWidget(self.cmboxUf)

        self.btnGravar = QPushButton(addCliente)
        self.btnGravar.setObjectName(u"btnGravar")
        self.btnGravar.setGeometry(QRect(180, 610, 75, 23))
        self.btnCancelar = QPushButton(addCliente)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(280, 610, 75, 23))
        QWidget.setTabOrder(self.txtNomeFantasia, self.txtCodeCliente)
        QWidget.setTabOrder(self.txtCodeCliente, self.txtRazoaSocial)
        QWidget.setTabOrder(self.txtRazoaSocial, self.cmbTipoCliente)
        QWidget.setTabOrder(self.cmbTipoCliente, self.txtCpfCnpj)
        QWidget.setTabOrder(self.txtCpfCnpj, self.txtIeRg)
        QWidget.setTabOrder(self.txtIeRg, self.txtTel1)
        QWidget.setTabOrder(self.txtTel1, self.txtTel2)
        QWidget.setTabOrder(self.txtTel2, self.txtCel)
        QWidget.setTabOrder(self.txtCel, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.txtUrl)
        QWidget.setTabOrder(self.txtUrl, self.txtEndereco)
        QWidget.setTabOrder(self.txtEndereco, self.txtNumero)
        QWidget.setTabOrder(self.txtNumero, self.txtCep)
        QWidget.setTabOrder(self.txtCep, self.cmbEstado)
        QWidget.setTabOrder(self.cmbEstado, self.txtCidade)
        QWidget.setTabOrder(self.txtCidade, self.txtBairro)
        QWidget.setTabOrder(self.txtBairro, self.btnGravar)
        QWidget.setTabOrder(self.btnGravar, self.btnCancelar)

        self.retranslateUi(addCliente)

        QMetaObject.connectSlotsByName(addCliente)
    # setupUi

    def retranslateUi(self, addCliente):
        addCliente.setWindowTitle(QCoreApplication.translate("addCliente", u"Form", None))
        self.GrupoEndereco.setTitle(QCoreApplication.translate("addCliente", u"Endere\u00e7o", None))
        self.labelEndereco.setText(QCoreApplication.translate("addCliente", u"Endere\u00e7o", None))
        self.txtEndereco.setText("")
        self.labelCidade.setText(QCoreApplication.translate("addCliente", u"Cidade", None))
        self.labelBairro.setText(QCoreApplication.translate("addCliente", u"Bairro", None))
        self.label_18.setText(QCoreApplication.translate("addCliente", u"Numero", None))
        self.label_19.setText(QCoreApplication.translate("addCliente", u"Estado", None))
        self.label_20.setText(QCoreApplication.translate("addCliente", u"CEP", None))
        self.GrupoContato.setTitle(QCoreApplication.translate("addCliente", u"Contatos", None))
        self.labelTel1.setText(QCoreApplication.translate("addCliente", u"Telefone", None))
        self.txtTel1.setText("")
        self.labelTel2.setText(QCoreApplication.translate("addCliente", u"Telefone 2", None))
        self.txtTel2.setText("")
        self.labelCelWhats.setText(QCoreApplication.translate("addCliente", u"Cel / Whatsapp", None))
        self.txtCel.setText("")
        self.label_11.setText(QCoreApplication.translate("addCliente", u"Site", None))
        self.txtUrl.setText("")
        self.label_10.setText(QCoreApplication.translate("addCliente", u"email", None))
        self.lineEdit_9.setText("")
        self.GrupoCliente.setTitle(QCoreApplication.translate("addCliente", u"Cliente", None))
        self.labelCPF.setText(QCoreApplication.translate("addCliente", u"CPF / CNPJ", None))
        self.txtCpfCnpj.setText("")
        self.labelNomeFantasia.setText(QCoreApplication.translate("addCliente", u"Nome Fantasia", None))
        self.labelRazaoSoc.setText(QCoreApplication.translate("addCliente", u"Raz\u00e3o Social", None))
        self.label_4.setText(QCoreApplication.translate("addCliente", u"C\u00f3digo Cliente", None))
        self.labelTipoCliente.setText(QCoreApplication.translate("addCliente", u"Tipo do  Cliente", None))
        self.cmbTipoCliente.setItemText(0, QCoreApplication.translate("addCliente", u"Juridico", None))
        self.cmbTipoCliente.setItemText(1, QCoreApplication.translate("addCliente", u"Fisica", None))

        self.labelIeRg.setText(QCoreApplication.translate("addCliente", u"IE / RG", None))
        self.labelAtividade.setText(QCoreApplication.translate("addCliente", u"Ramo de Atividade", None))
        self.labelClienteDesde.setText(QCoreApplication.translate("addCliente", u"Cliente desde", None))
        self.labelUf.setText(QCoreApplication.translate("addCliente", u"UF", None))
        self.cmboxUf.setItemText(0, QCoreApplication.translate("addCliente", u"RJ", None))

        self.btnGravar.setText(QCoreApplication.translate("addCliente", u"Gravar", None))
        self.btnCancelar.setText(QCoreApplication.translate("addCliente", u"Cancelar", None))
    # retranslateUi

