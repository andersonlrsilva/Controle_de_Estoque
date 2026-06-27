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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddProd(object):
    def setupUi(self, AddProd):
        if not AddProd.objectName():
            AddProd.setObjectName(u"AddProd")
        AddProd.resize(900, 500)
        AddProd.setMinimumSize(QSize(900, 500))
        AddProd.setMaximumSize(QSize(900, 16777215))
        self.verticalLayout_9 = QVBoxLayout(AddProd)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(AddProd)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.TabDados = QWidget()
        self.TabDados.setObjectName(u"TabDados")
        self.groupBox = QGroupBox(self.TabDados)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 10, 851, 241))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 70, 151, 41))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label_2)

        self.txtCodBarras = QLineEdit(self.verticalLayoutWidget_2)
        self.txtCodBarras.setObjectName(u"txtCodBarras")

        self.verticalLayout_2.addWidget(self.txtCodBarras)

        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 151, 41))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(0)

        self.verticalLayout.addWidget(self.label)

        self.txtCodSku = QLineEdit(self.verticalLayoutWidget)
        self.txtCodSku.setObjectName(u"txtCodSku")

        self.verticalLayout.addWidget(self.txtCodSku)

        self.verticalLayoutWidget_3 = QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(170, 20, 371, 41))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.label_3)

        self.txtNomeProd = QLineEdit(self.verticalLayoutWidget_3)
        self.txtNomeProd.setObjectName(u"txtNomeProd")

        self.verticalLayout_3.addWidget(self.txtNomeProd)

        self.verticalLayoutWidget_4 = QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(170, 70, 371, 41))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.label_4)

        self.txtNomeComercial = QLineEdit(self.verticalLayoutWidget_4)
        self.txtNomeComercial.setObjectName(u"txtNomeComercial")

        self.verticalLayout_4.addWidget(self.txtNomeComercial)

        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 120, 151, 41))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLineWidth(0)

        self.verticalLayout_5.addWidget(self.label_5)

        self.txtCest = QLineEdit(self.verticalLayoutWidget_5)
        self.txtCest.setObjectName(u"txtCest")

        self.verticalLayout_5.addWidget(self.txtCest)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 170, 151, 41))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLineWidth(0)

        self.verticalLayout_6.addWidget(self.label_6)

        self.txtNcm = QLineEdit(self.verticalLayoutWidget_6)
        self.txtNcm.setObjectName(u"txtNcm")

        self.verticalLayout_6.addWidget(self.txtNcm)

        self.verticalLayoutWidget_7 = QWidget(self.groupBox)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(170, 120, 160, 41))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.cmbFabric = QComboBox(self.verticalLayoutWidget_7)
        self.cmbFabric.setObjectName(u"cmbFabric")

        self.verticalLayout_7.addWidget(self.cmbFabric)

        self.verticalLayoutWidget_8 = QWidget(self.groupBox)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(380, 120, 160, 41))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_8)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.cmbFornec = QComboBox(self.verticalLayoutWidget_8)
        self.cmbFornec.setObjectName(u"cmbFornec")

        self.verticalLayout_8.addWidget(self.cmbFornec)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(660, 20, 181, 211))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.labelFoto = QLabel(self.groupBox_2)
        self.labelFoto.setObjectName(u"labelFoto")
        self.labelFoto.setGeometry(QRect(6, 22, 171, 151))
        self.btnSalvaFoto = QPushButton(self.groupBox_2)
        self.btnSalvaFoto.setObjectName(u"btnSalvaFoto")
        self.btnSalvaFoto.setGeometry(QRect(10, 180, 81, 23))
        self.btnRemFoto = QPushButton(self.groupBox_2)
        self.btnRemFoto.setObjectName(u"btnRemFoto")
        self.btnRemFoto.setGeometry(QRect(90, 180, 81, 23))
        self.checkInativo = QCheckBox(self.groupBox)
        self.checkInativo.setObjectName(u"checkInativo")
        self.checkInativo.setGeometry(QRect(550, 40, 101, 17))
        self.verticalLayoutWidget_9 = QWidget(self.groupBox)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(170, 170, 160, 41))
        self.Marca = QVBoxLayout(self.verticalLayoutWidget_9)
        self.Marca.setObjectName(u"Marca")
        self.Marca.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.verticalLayoutWidget_9)
        self.label_9.setObjectName(u"label_9")

        self.Marca.addWidget(self.label_9)

        self.cmbMarca = QComboBox(self.verticalLayoutWidget_9)
        self.cmbMarca.setObjectName(u"cmbMarca")

        self.Marca.addWidget(self.cmbMarca)

        self.btnAddMarca = QPushButton(self.groupBox)
        self.btnAddMarca.setObjectName(u"btnAddMarca")
        self.btnAddMarca.setGeometry(QRect(330, 190, 30, 21))
        self.btnAddMarca.setMinimumSize(QSize(30, 21))
        self.btnAddMarca.setMaximumSize(QSize(30, 21))
        self.btnAddFabric = QPushButton(self.groupBox)
        self.btnAddFabric.setObjectName(u"btnAddFabric")
        self.btnAddFabric.setGeometry(QRect(330, 140, 31, 21))
        self.btnAddFabric.setMinimumSize(QSize(31, 21))
        self.btnAddFabric.setMaximumSize(QSize(30, 20))
        self.btnAddFornec = QPushButton(self.groupBox)
        self.btnAddFornec.setObjectName(u"btnAddFornec")
        self.btnAddFornec.setGeometry(QRect(540, 140, 30, 20))
        self.btnAddFornec.setMinimumSize(QSize(30, 20))
        self.btnAddFornec.setMaximumSize(QSize(30, 20))
        self.groupBox_3 = QGroupBox(self.TabDados)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 260, 851, 121))
        self.groupBox_3.setFlat(False)
        self.txtAplicacao = QTextEdit(self.groupBox_3)
        self.txtAplicacao.setObjectName(u"txtAplicacao")
        self.txtAplicacao.setGeometry(QRect(10, 23, 831, 91))
        self.tabWidget.addTab(self.TabDados, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(330, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnGravarProd = QPushButton(AddProd)
        self.btnGravarProd.setObjectName(u"btnGravarProd")

        self.horizontalLayout.addWidget(self.btnGravarProd)

        self.btnLimpaForm = QPushButton(AddProd)
        self.btnLimpaForm.setObjectName(u"btnLimpaForm")

        self.horizontalLayout.addWidget(self.btnLimpaForm)

        self.btnSair = QPushButton(AddProd)
        self.btnSair.setObjectName(u"btnSair")

        self.horizontalLayout.addWidget(self.btnSair)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout)


        self.retranslateUi(AddProd)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddProd)
    # setupUi

    def retranslateUi(self, AddProd):
        AddProd.setWindowTitle(QCoreApplication.translate("AddProd", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddProd", u"Dados do Produtos", None))
        self.label_2.setText(QCoreApplication.translate("AddProd", u"C\u00f3digo de Barras", None))
        self.label.setText(QCoreApplication.translate("AddProd", u"C\u00f3digo SKU", None))
        self.txtCodSku.setText("")
        self.label_3.setText(QCoreApplication.translate("AddProd", u"Nome do Produto", None))
        self.label_4.setText(QCoreApplication.translate("AddProd", u"Nome Comercial", None))
        self.label_5.setText(QCoreApplication.translate("AddProd", u"C\u00f3digo CEST", None))
        self.label_6.setText(QCoreApplication.translate("AddProd", u"C\u00f3digo NCM", None))
        self.label_7.setText(QCoreApplication.translate("AddProd", u"Fabricante", None))
        self.label_8.setText(QCoreApplication.translate("AddProd", u"Fornecedor", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AddProd", u"Imagem do produto", None))
        self.labelFoto.setText("")
        self.btnSalvaFoto.setText(QCoreApplication.translate("AddProd", u"Inserir Imagem", None))
        self.btnRemFoto.setText(QCoreApplication.translate("AddProd", u"Rem. imagem", None))
        self.checkInativo.setText(QCoreApplication.translate("AddProd", u"Produto Inativo", None))
        self.label_9.setText(QCoreApplication.translate("AddProd", u"Marca", None))
        self.btnAddMarca.setText(QCoreApplication.translate("AddProd", u"Add", None))
        self.btnAddFabric.setText(QCoreApplication.translate("AddProd", u"Add", None))
        self.btnAddFornec.setText(QCoreApplication.translate("AddProd", u"Add", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AddProd", u"Aplica\u00e7\u00e3o / Descri\u00e7\u00e3o detalhada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabDados), QCoreApplication.translate("AddProd", u"Dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("AddProd", u"Estoque", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("AddProd", u"Financeiro", None))
        self.btnGravarProd.setText(QCoreApplication.translate("AddProd", u"Salvar", None))
        self.btnLimpaForm.setText(QCoreApplication.translate("AddProd", u"Limpar Formulario", None))
        self.btnSair.setText(QCoreApplication.translate("AddProd", u"Sair", None))
    # retranslateUi

