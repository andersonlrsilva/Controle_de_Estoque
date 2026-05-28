# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProd.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AddProd(object):
    def setupUi(self, AddProd):
        if not AddProd.objectName():
            AddProd.setObjectName(u"AddProd")
        AddProd.resize(1366, 768)
        AddProd.setMinimumSize(QSize(1366, 768))
        AddProd.setMaximumSize(QSize(1366, 16777215))
        self.verticalLayout = QVBoxLayout(AddProd)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(AddProd)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nomeProduto = QGroupBox(self.groupBox)
        self.nomeProduto.setObjectName(u"nomeProduto")
        self.nomeProduto.setMinimumSize(QSize(400, 200))
        self.nomeProduto.setMaximumSize(QSize(400, 200))
        self.verticalLayoutWidget_4 = QWidget(self.nomeProduto)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 30, 371, 41))
        self.layout_nome = QVBoxLayout(self.verticalLayoutWidget_4)
        self.layout_nome.setObjectName(u"layout_nome")
        self.layout_nome.setContentsMargins(0, 0, 0, 0)
        self.labelNome = QLabel(self.verticalLayoutWidget_4)
        self.labelNome.setObjectName(u"labelNome")

        self.layout_nome.addWidget(self.labelNome)

        self.txtNomeProd = QLineEdit(self.verticalLayoutWidget_4)
        self.txtNomeProd.setObjectName(u"txtNomeProd")

        self.layout_nome.addWidget(self.txtNomeProd)

        self.verticalLayoutWidget_5 = QWidget(self.nomeProduto)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 80, 371, 41))
        self.layout_nome_comercial = QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_nome_comercial.setObjectName(u"layout_nome_comercial")
        self.layout_nome_comercial.setContentsMargins(0, 0, 0, 0)
        self.labelNomeComercial = QLabel(self.verticalLayoutWidget_5)
        self.labelNomeComercial.setObjectName(u"labelNomeComercial")

        self.layout_nome_comercial.addWidget(self.labelNomeComercial)

        self.txtNomeComercial = QLineEdit(self.verticalLayoutWidget_5)
        self.txtNomeComercial.setObjectName(u"txtNomeComercial")

        self.layout_nome_comercial.addWidget(self.txtNomeComercial)

        self.verticalLayoutWidget_6 = QWidget(self.nomeProduto)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 130, 371, 41))
        self.layout_marca = QVBoxLayout(self.verticalLayoutWidget_6)
        self.layout_marca.setObjectName(u"layout_marca")
        self.layout_marca.setContentsMargins(0, 0, 0, 0)
        self.labelMarca = QLabel(self.verticalLayoutWidget_6)
        self.labelMarca.setObjectName(u"labelMarca")

        self.layout_marca.addWidget(self.labelMarca)

        self.txtMarca = QLineEdit(self.verticalLayoutWidget_6)
        self.txtMarca.setObjectName(u"txtMarca")

        self.layout_marca.addWidget(self.txtMarca)


        self.horizontalLayout.addWidget(self.nomeProduto)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(400, 200))
        self.groupBox_3.setMaximumSize(QSize(16777215, 200))
        self.verticalLayoutWidget_7 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 30, 331, 41))
        self.CodigoSku = QVBoxLayout(self.verticalLayoutWidget_7)
        self.CodigoSku.setObjectName(u"CodigoSku")
        self.CodigoSku.setContentsMargins(0, 0, 0, 0)
        self.labelCodSku = QLabel(self.verticalLayoutWidget_7)
        self.labelCodSku.setObjectName(u"labelCodSku")

        self.CodigoSku.addWidget(self.labelCodSku)

        self.txtCodSku = QLineEdit(self.verticalLayoutWidget_7)
        self.txtCodSku.setObjectName(u"txtCodSku")

        self.CodigoSku.addWidget(self.txtCodSku)

        self.verticalLayoutWidget_8 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 80, 331, 41))
        self.CodigoDeBarras = QVBoxLayout(self.verticalLayoutWidget_8)
        self.CodigoDeBarras.setObjectName(u"CodigoDeBarras")
        self.CodigoDeBarras.setContentsMargins(0, 0, 0, 0)
        self.labelCodBarras = QLabel(self.verticalLayoutWidget_8)
        self.labelCodBarras.setObjectName(u"labelCodBarras")

        self.CodigoDeBarras.addWidget(self.labelCodBarras)

        self.txtCodBarras = QLineEdit(self.verticalLayoutWidget_8)
        self.txtCodBarras.setObjectName(u"txtCodBarras")

        self.CodigoDeBarras.addWidget(self.txtCodBarras)

        self.verticalLayoutWidget_9 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 130, 331, 41))
        self.layoutForncedor = QVBoxLayout(self.verticalLayoutWidget_9)
        self.layoutForncedor.setObjectName(u"layoutForncedor")
        self.layoutForncedor.setContentsMargins(0, 0, 0, 0)
        self.labelFornecedor = QLabel(self.verticalLayoutWidget_9)
        self.labelFornecedor.setObjectName(u"labelFornecedor")

        self.layoutForncedor.addWidget(self.labelFornecedor)

        self.txtFornecedor = QLineEdit(self.verticalLayoutWidget_9)
        self.txtFornecedor.setObjectName(u"txtFornecedor")

        self.layoutForncedor.addWidget(self.txtFornecedor)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 450))

        self.horizontalLayout_2.addWidget(self.groupBox_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnGravarProd = QPushButton(AddProd)
        self.btnGravarProd.setObjectName(u"btnGravarProd")
        self.btnGravarProd.setMinimumSize(QSize(0, 30))
        self.btnGravarProd.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_5.addWidget(self.btnGravarProd)

        self.btnLimpaForm = QPushButton(AddProd)
        self.btnLimpaForm.setObjectName(u"btnLimpaForm")
        self.btnLimpaForm.setMinimumSize(QSize(0, 30))
        self.btnLimpaForm.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.btnLimpaForm)

        self.btnSair = QPushButton(AddProd)
        self.btnSair.setObjectName(u"btnSair")
        self.btnSair.setMinimumSize(QSize(0, 30))
        self.btnSair.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.btnSair)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(AddProd)

        QMetaObject.connectSlotsByName(AddProd)
    # setupUi

    def retranslateUi(self, AddProd):
        AddProd.setWindowTitle(QCoreApplication.translate("AddProd", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddProd", u"Cadastro de Produtos", None))
        self.nomeProduto.setTitle(QCoreApplication.translate("AddProd", u"Nome do produto", None))
        self.labelNome.setText(QCoreApplication.translate("AddProd", u"Nome", None))
        self.labelNomeComercial.setText(QCoreApplication.translate("AddProd", u"Nome Comercial", None))
        self.labelMarca.setText(QCoreApplication.translate("AddProd", u"Marca", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AddProd", u"GroupBox", None))
        self.labelCodSku.setText(QCoreApplication.translate("AddProd", u"Codigo SKU", None))
        self.labelCodBarras.setText(QCoreApplication.translate("AddProd", u"Codigo de barras", None))
        self.labelFornecedor.setText(QCoreApplication.translate("AddProd", u"Fornecedor", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("AddProd", u"GroupBox", None))
        self.btnGravarProd.setText(QCoreApplication.translate("AddProd", u"Gravar Produto", None))
        self.btnLimpaForm.setText(QCoreApplication.translate("AddProd", u"Limpar Formulario", None))
        self.btnSair.setText(QCoreApplication.translate("AddProd", u"Sair", None))
    # retranslateUi

