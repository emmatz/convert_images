# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWinsMYcgm.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(495, 285)
        MainWindow.setMinimumSize(QSize(495, 285))
        MainWindow.setMaximumSize(QSize(495, 285))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/avatar_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushBuscar = QPushButton(self.centralwidget)
        self.pushBuscar.setObjectName(u"pushBuscar")
        self.pushBuscar.setGeometry(QRect(10, 20, 151, 31))
        self.pushIco = QPushButton(self.centralwidget)
        self.pushIco.setObjectName(u"pushIco")
        self.pushIco.setGeometry(QRect(10, 60, 151, 31))
        self.pushWebp = QPushButton(self.centralwidget)
        self.pushWebp.setObjectName(u"pushWebp")
        self.pushWebp.setGeometry(QRect(10, 100, 151, 51))
        self.pushWebp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushRed = QPushButton(self.centralwidget)
        self.pushRed.setObjectName(u"pushRed")
        self.pushRed.setGeometry(QRect(10, 160, 151, 31))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(185, 60, 291, 201))
        self.pushSalir = QPushButton(self.centralwidget)
        self.pushSalir.setObjectName(u"pushSalir")
        self.pushSalir.setGeometry(QRect(10, 230, 151, 31))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 20, 281, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Convertidor de Imagenes", None))
#if QT_CONFIG(statustip)
        self.pushBuscar.setStatusTip(QCoreApplication.translate("MainWindow", u"Buscar imagen", None))
#endif // QT_CONFIG(statustip)
        self.pushBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar archivo", None))
#if QT_CONFIG(statustip)
        self.pushIco.setStatusTip(QCoreApplication.translate("MainWindow", u"Generar icono", None))
#endif // QT_CONFIG(statustip)
        self.pushIco.setText(QCoreApplication.translate("MainWindow", u"Convertir a ICO", None))
#if QT_CONFIG(tooltip)
        self.pushWebp.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushWebp.setStatusTip(QCoreApplication.translate("MainWindow", u"transformar webp a jpg y png", None))
#endif // QT_CONFIG(statustip)
        self.pushWebp.setText(QCoreApplication.translate("MainWindow", u"Convertir de Webp\n"
"a PNG y JPEG", None))
#if QT_CONFIG(statustip)
        self.pushRed.setStatusTip(QCoreApplication.translate("MainWindow", u"cambiar tama\u00f1o", None))
#endif // QT_CONFIG(statustip)
        self.pushRed.setText(QCoreApplication.translate("MainWindow", u"Redimensionar", None))
#if QT_CONFIG(statustip)
        self.graphicsView.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushSalir.setStatusTip(QCoreApplication.translate("MainWindow", u"salir", None))
#endif // QT_CONFIG(statustip)
        self.pushSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

