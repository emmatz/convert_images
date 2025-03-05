# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'redimensionareogUuz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)
import resources_rc

class Ui_rediForm(object):
    def setupUi(self, rediForm):
        if not rediForm.objectName():
            rediForm.setObjectName(u"rediForm")
        rediForm.resize(280, 160)
        rediForm.setMinimumSize(QSize(280, 160))
        rediForm.setMaximumSize(QSize(340, 160))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        rediForm.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/avatar_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        rediForm.setWindowIcon(icon)
        self.formLayout = QFormLayout(rediForm)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(rediForm)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinBoxAncho = QSpinBox(rediForm)
        self.spinBoxAncho.setObjectName(u"spinBoxAncho")
        self.spinBoxAncho.setMaximum(100000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBoxAncho)

        self.label_2 = QLabel(rediForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinBoxAlto = QSpinBox(rediForm)
        self.spinBoxAlto.setObjectName(u"spinBoxAlto")
        self.spinBoxAlto.setMaximum(100000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBoxAlto)

        self.pushRedi = QPushButton(rediForm)
        self.pushRedi.setObjectName(u"pushRedi")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushRedi)

        self.pushSalir = QPushButton(rediForm)
        self.pushSalir.setObjectName(u"pushSalir")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pushSalir)

        self.pushReset = QPushButton(rediForm)
        self.pushReset.setObjectName(u"pushReset")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushReset)


        self.retranslateUi(rediForm)

        QMetaObject.connectSlotsByName(rediForm)
    # setupUi

    def retranslateUi(self, rediForm):
        rediForm.setWindowTitle(QCoreApplication.translate("rediForm", u"Redimensionar.", None))
        self.label.setText(QCoreApplication.translate("rediForm", u"Ancho:", None))
        self.label_2.setText(QCoreApplication.translate("rediForm", u"Alto:", None))
        self.pushRedi.setText(QCoreApplication.translate("rediForm", u"Redimensionar", None))
        self.pushSalir.setText(QCoreApplication.translate("rediForm", u"Salir", None))
        self.pushReset.setText(QCoreApplication.translate("rediForm", u"Restablecer valores", None))
    # retranslateUi

