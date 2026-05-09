# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Update(object):
    def setupUi(self, Update):
        if not Update.objectName():
            Update.setObjectName(u"Update")
        Update.resize(522, 345)
        self.btnBuscAtua = QPushButton(Update)
        self.btnBuscAtua.setObjectName(u"btnBuscAtua")
        self.btnBuscAtua.setGeometry(QRect(90, 290, 101, 23))
        self.btnAtualizar = QPushButton(Update)
        self.btnAtualizar.setObjectName(u"btnAtualizar")
        self.btnAtualizar.setGeometry(QRect(210, 290, 101, 23))
        self.btnSair = QPushButton(Update)
        self.btnSair.setObjectName(u"btnSair")
        self.btnSair.setGeometry(QRect(340, 290, 101, 23))
        self.horizontalLayoutWidget = QWidget(Update)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 40, 261, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelVersao = QLabel(self.horizontalLayoutWidget)
        self.labelVersao.setObjectName(u"labelVersao")
        self.labelVersao.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout.addWidget(self.labelVersao)

        self.labelVerInfo = QLabel(self.horizontalLayoutWidget)
        self.labelVerInfo.setObjectName(u"labelVerInfo")

        self.horizontalLayout.addWidget(self.labelVerInfo)

        self.horizontalLayoutWidget_2 = QWidget(Update)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 90, 261, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelNovaVersao = QLabel(self.horizontalLayoutWidget_2)
        self.labelNovaVersao.setObjectName(u"labelNovaVersao")
        self.labelNovaVersao.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.labelNovaVersao)

        self.labelInfoNovaVersao = QLabel(self.horizontalLayoutWidget_2)
        self.labelInfoNovaVersao.setObjectName(u"labelInfoNovaVersao")

        self.horizontalLayout_2.addWidget(self.labelInfoNovaVersao)


        self.retranslateUi(Update)

        QMetaObject.connectSlotsByName(Update)
    # setupUi

    def retranslateUi(self, Update):
        Update.setWindowTitle(QCoreApplication.translate("Update", u"Form", None))
        self.btnBuscAtua.setText(QCoreApplication.translate("Update", u"Buscar Atualiza\u00e7\u00e3o", None))
        self.btnAtualizar.setText(QCoreApplication.translate("Update", u"Atualizar", None))
        self.btnSair.setText(QCoreApplication.translate("Update", u"Sair", None))
        self.labelVersao.setText(QCoreApplication.translate("Update", u"Vers\u00e3o Atual: ", None))
        self.labelVerInfo.setText("")
        self.labelNovaVersao.setText(QCoreApplication.translate("Update", u"Nova vers\u00e3o:", None))
        self.labelInfoNovaVersao.setText("")
    # retranslateUi

