# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addAtividade.ui'
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

class Ui_AddAtividade(object):
    def setupUi(self, AddAtividade):
        if not AddAtividade.objectName():
            AddAtividade.setObjectName(u"AddAtividade")
        AddAtividade.resize(376, 275)
        self.groupBox = QGroupBox(AddAtividade)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 9, 361, 211))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 341, 41))
        self.marca = QVBoxLayout(self.verticalLayoutWidget_2)
        self.marca.setObjectName(u"marca")
        self.marca.setContentsMargins(0, 0, 0, 0)
        self.labelAtividade = QLabel(self.verticalLayoutWidget_2)
        self.labelAtividade.setObjectName(u"labelAtividade")

        self.marca.addWidget(self.labelAtividade)

        self.txtAtividade = QLineEdit(self.verticalLayoutWidget_2)
        self.txtAtividade.setObjectName(u"txtAtividade")

        self.marca.addWidget(self.txtAtividade)

        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 130, 160, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSalvar = QPushButton(self.horizontalLayoutWidget)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout.addWidget(self.btnSalvar)

        self.btnCancelar = QPushButton(self.horizontalLayoutWidget)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.horizontalLayout.addWidget(self.btnCancelar)

        QWidget.setTabOrder(self.txtAtividade, self.btnSalvar)
        QWidget.setTabOrder(self.btnSalvar, self.btnCancelar)

        self.retranslateUi(AddAtividade)

        QMetaObject.connectSlotsByName(AddAtividade)
    # setupUi

    def retranslateUi(self, AddAtividade):
        AddAtividade.setWindowTitle(QCoreApplication.translate("AddAtividade", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddAtividade", u"Adcionar Marca", None))
        self.labelAtividade.setText(QCoreApplication.translate("AddAtividade", u"Atividade", None))
        self.btnSalvar.setText(QCoreApplication.translate("AddAtividade", u"Salvar", None))
        self.btnCancelar.setText(QCoreApplication.translate("AddAtividade", u"Cancelar", None))
    # retranslateUi

