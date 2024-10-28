# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projeto_cripto.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 440)
        MainWindow.setMaximumSize(QSize(800, 440))
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/*\n"
"QWidget{\n"
"	background-color: rgb(145, 145, 145);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.header_container = QFrame(self.centralwidget)
        self.header_container.setObjectName(u"header_container")
        self.header_container.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.header_container.setFrameShape(QFrame.StyledPanel)
        self.header_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toogle = QPushButton(self.header_container)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setMaximumSize(QSize(25, 16777215))
        self.btn_toogle.setStyleSheet(u"QPushButton{\n"
"	border:0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/threebars.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toogle.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_toogle)

        self.lb_name = QLabel(self.header_container)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lb_name)


        self.verticalLayout.addWidget(self.header_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.main_container)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(200, 16777215))
        self.left_menu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border:1px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(193, 193, 193);\n"
"	border-color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"/*\n"
"QPushButton{\n"
"	background-color: rgb(65, 105, 225);\n"
"	color: rgb(255, 255, 255);\n"
"	border:1px solid;\n"
"	border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}\n"
"*/")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_cripto = QPushButton(self.left_menu)
        self.btn_cripto.setObjectName(u"btn_cripto")
        self.btn_cripto.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.btn_cripto)

        self.btn_descripto = QPushButton(self.left_menu)
        self.btn_descripto.setObjectName(u"btn_descripto")
        self.btn_descripto.setMinimumSize(QSize(100, 20))

        self.verticalLayout_2.addWidget(self.btn_descripto)

        self.btn_config = QPushButton(self.left_menu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.btn_config)

        self.btn_suporte = QPushButton(self.left_menu)
        self.btn_suporte.setObjectName(u"btn_suporte")
        self.btn_suporte.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.btn_suporte)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_menu = QFrame(self.main_container)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(240, 240, 240);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.main_menu.setFrameShape(QFrame.StyledPanel)
        self.main_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_pages = QStackedWidget(self.main_menu)
        self.main_pages.setObjectName(u"main_pages")
        self.pg_cripto = QWidget()
        self.pg_cripto.setObjectName(u"pg_cripto")
        self.verticalLayout_4 = QVBoxLayout(self.pg_cripto)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.pg_cripto)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.ed_texto = QLineEdit(self.frame)
        self.ed_texto.setObjectName(u"ed_texto")

        self.horizontalLayout_4.addWidget(self.ed_texto)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.pg_cripto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/icons/paste.png);\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-image: url(:/icons/paste_clicked.png);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(202, 202, 202);\n"
"	border:1px solid;\n"
"}\n"
"\n"
"QLabel{\n"
"	border:0px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_cript = QLabel(self.frame_4)
        self.lb_cript.setObjectName(u"lb_cript")

        self.horizontalLayout_7.addWidget(self.lb_cript)

        self.btn_paste_cript = QPushButton(self.frame_4)
        self.btn_paste_cript.setObjectName(u"btn_paste_cript")
        self.btn_paste_cript.setEnabled(False)
        self.btn_paste_cript.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.btn_paste_cript)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(202, 202, 202);\n"
"	border:1px solid;\n"
"}\n"
"\n"
"QLabel{\n"
"	border:0px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_codigo = QLabel(self.frame_5)
        self.lb_codigo.setObjectName(u"lb_codigo")

        self.horizontalLayout_6.addWidget(self.lb_codigo)

        self.btn_paste_code = QPushButton(self.frame_5)
        self.btn_paste_code.setObjectName(u"btn_paste_code")
        self.btn_paste_code.setEnabled(False)
        self.btn_paste_code.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.btn_paste_code)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.btn_crip = QPushButton(self.frame_2)
        self.btn_crip.setObjectName(u"btn_crip")

        self.verticalLayout_5.addWidget(self.btn_crip)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.main_pages.addWidget(self.pg_cripto)
        self.pg_descripto = QWidget()
        self.pg_descripto.setObjectName(u"pg_descripto")
        self.verticalLayout_6 = QVBoxLayout(self.pg_descripto)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.pg_descripto)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_texto = QLabel(self.frame_8)
        self.lb_texto.setObjectName(u"lb_texto")
        self.lb_texto.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_8.addWidget(self.lb_texto)

        self.ed_descripto_texto = QLineEdit(self.frame_8)
        self.ed_descripto_texto.setObjectName(u"ed_descripto_texto")

        self.horizontalLayout_8.addWidget(self.ed_descripto_texto)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_code = QLabel(self.frame_9)
        self.lb_code.setObjectName(u"lb_code")
        self.lb_code.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_9.addWidget(self.lb_code)

        self.ed_descripto_code = QLineEdit(self.frame_9)
        self.ed_descripto_code.setObjectName(u"ed_descripto_code")

        self.horizontalLayout_9.addWidget(self.ed_descripto_code)


        self.verticalLayout_7.addWidget(self.frame_9)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.pg_descripto)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/icons/paste.png);\n"
"	background-color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-image: url(:/icons/paste_clicked.png);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(202, 202, 202);\n"
"	border:1px solid;\n"
"}\n"
"\n"
"QLabel{\n"
"	border:0px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_descripto_texto = QLabel(self.frame_10)
        self.lb_descripto_texto.setObjectName(u"lb_descripto_texto")

        self.horizontalLayout_10.addWidget(self.lb_descripto_texto)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(27, 16777215))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	border:0px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_paste_texto = QPushButton(self.frame_11)
        self.btn_paste_texto.setObjectName(u"btn_paste_texto")
        self.btn_paste_texto.setEnabled(False)
        self.btn_paste_texto.setMinimumSize(QSize(25, 25))
        self.btn_paste_texto.setMaximumSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.btn_paste_texto)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_10.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.btn_descrip = QPushButton(self.frame_7)
        self.btn_descrip.setObjectName(u"btn_descrip")

        self.verticalLayout_8.addWidget(self.btn_descrip)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.main_pages.addWidget(self.pg_descripto)
        self.pg_suporte = QWidget()
        self.pg_suporte.setObjectName(u"pg_suporte")
        self.verticalLayout_10 = QVBoxLayout(self.pg_suporte)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_12 = QFrame(self.pg_suporte)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_3)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	border:1px solid;\n"
"}")
        self.label_4.setPixmap(QPixmap(u":/icons/qrcode.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_12.addWidget(self.frame_14)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.main_pages.addWidget(self.pg_suporte)
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.main_pages.addWidget(self.pg_config)

        self.verticalLayout_3.addWidget(self.main_pages)


        self.horizontalLayout.addWidget(self.main_menu)


        self.verticalLayout.addWidget(self.main_container)

        self.footer_container = QFrame(self.centralwidget)
        self.footer_container.setObjectName(u"footer_container")
        self.footer_container.setFrameShape(QFrame.StyledPanel)
        self.footer_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lb_arroba = QLabel(self.footer_container)
        self.lb_arroba.setObjectName(u"lb_arroba")

        self.horizontalLayout_3.addWidget(self.lb_arroba)


        self.verticalLayout.addWidget(self.footer_container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.main_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toogle.setText("")
        self.lb_name.setText(QCoreApplication.translate("MainWindow", u"PyCripto", None))
        self.btn_cripto.setText(QCoreApplication.translate("MainWindow", u"Criptografar", None))
        self.btn_descripto.setText(QCoreApplication.translate("MainWindow", u"Descriptografar", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_suporte.setText(QCoreApplication.translate("MainWindow", u"Suporte", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Texto: ", None))
        self.lb_cript.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_paste_cript.setText("")
        self.lb_codigo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_paste_code.setText("")
        self.btn_crip.setText(QCoreApplication.translate("MainWindow", u"Criptografar", None))
        self.lb_texto.setText(QCoreApplication.translate("MainWindow", u"Texto", None))
        self.lb_code.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.lb_descripto_texto.setText("")
        self.btn_paste_texto.setText("")
        self.btn_descrip.setText(QCoreApplication.translate("MainWindow", u"Descriptografar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Esse \u00e9 um Software criado por Rigimon sobre criptografia\n"
"Email de Contato:\n"
"rigi.dev@hotmail.com\n"
"Doa\u00e7\u00f5es:", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o 0.1", None))
        self.lb_arroba.setText(QCoreApplication.translate("MainWindow", u"@Rigimon", None))
    # retranslateUi

