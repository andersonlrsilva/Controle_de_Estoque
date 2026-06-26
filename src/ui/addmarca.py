# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addMarca.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddMarca(object):
    def setupUi(self, AddMarca):
        if not AddMarca.objectName():
            AddMarca.setObjectName(u"AddMarca")
        AddMarca.resize(376, 275)
        self.groupBox = QGroupBox(AddMarca)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 9, 361, 251))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 341, 41))
        self.marca = QVBoxLayout(self.verticalLayoutWidget_2)
        self.marca.setObjectName(u"marca")
        self.marca.setContentsMargins(0, 0, 0, 0)
        self.labelMarca = QLabel(self.verticalLayoutWidget_2)
        self.labelMarca.setObjectName(u"labelMarca")

        self.marca.addWidget(self.labelMarca)

        self.txtMarca = QLineEdit(self.verticalLayoutWidget_2)
        self.txtMarca.setObjectName(u"txtMarca")

        self.marca.addWidget(self.txtMarca)

        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 110, 341, 41))
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
        self.horizontalLayoutWidget.setGeometry(QRect(100, 180, 160, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSalvar = QPushButton(self.horizontalLayoutWidget)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout.addWidget(self.btnSalvar)

        self.btnCancelar = QPushButton(self.horizontalLayoutWidget)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.horizontalLayout.addWidget(self.btnCancelar)

        QWidget.setTabOrder(self.txtMarca, self.txtSite)
        QWidget.setTabOrder(self.txtSite, self.btnSalvar)
        QWidget.setTabOrder(self.btnSalvar, self.btnCancelar)

        self.retranslateUi(AddMarca)

        QMetaObject.connectSlotsByName(AddMarca)
    # setupUi

    def retranslateUi(self, AddMarca):
        AddMarca.setWindowTitle(QCoreApplication.translate("AddMarca", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddMarca", u"Adcionar Marca", None))
        self.labelMarca.setText(QCoreApplication.translate("AddMarca", u"Marca", None))
        self.labelSite.setText(QCoreApplication.translate("AddMarca", u"Site", None))
        self.btnSalvar.setText(QCoreApplication.translate("AddMarca", u"Salvar", None))
        self.btnCancelar.setText(QCoreApplication.translate("AddMarca", u"Cancelar", None))
    # retranslateUi

