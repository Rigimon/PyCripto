# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projeto_cripto.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTextEdit, QVBoxLayout,
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
        self.left_menu.setMaximumSize(QSize(0, 16777215))
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

        self.btn_estegano = QPushButton(self.left_menu)
        self.btn_estegano.setObjectName(u"btn_estegano")
        self.btn_estegano.setMinimumSize(QSize(100, 20))

        self.verticalLayout_2.addWidget(self.btn_estegano)

        self.btn_config = QPushButton(self.left_menu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setEnabled(True)
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
        self.pg_esteg = QWidget()
        self.pg_esteg.setObjectName(u"pg_esteg")
        self.gridLayout = QGridLayout(self.pg_esteg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_20 = QFrame(self.pg_esteg)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.path_image_frame = QFrame(self.frame_20)
        self.path_image_frame.setObjectName(u"path_image_frame")
        self.path_image_frame.setFrameShape(QFrame.StyledPanel)
        self.path_image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.path_image_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.path_dir = QLineEdit(self.path_image_frame)
        self.path_dir.setObjectName(u"path_dir")
        self.path_dir.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.path_dir)

        self.btn_open_dir = QPushButton(self.path_image_frame)
        self.btn_open_dir.setObjectName(u"btn_open_dir")
        self.btn_open_dir.setStyleSheet(u"QPushButton{\n"
"	border:0px;\n"
"	border-image: url(:/icons/open_dir.png);\n"
"	width:25px;\n"
"	height:25px;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_open_dir)


        self.verticalLayout_19.addWidget(self.path_image_frame)

        self.text_frame = QFrame(self.frame_20)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.text_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.texte_esteg = QTextEdit(self.text_frame)
        self.texte_esteg.setObjectName(u"texte_esteg")

        self.verticalLayout_18.addWidget(self.texte_esteg)


        self.verticalLayout_19.addWidget(self.text_frame)

        self.lb_succes = QLabel(self.frame_20)
        self.lb_succes.setObjectName(u"lb_succes")

        self.verticalLayout_19.addWidget(self.lb_succes)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_23)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_esteg = QPushButton(self.frame_23)
        self.btn_esteg.setObjectName(u"btn_esteg")

        self.gridLayout_2.addWidget(self.btn_esteg, 0, 0, 1, 1)

        self.btn_desteg = QPushButton(self.frame_23)
        self.btn_desteg.setObjectName(u"btn_desteg")

        self.gridLayout_2.addWidget(self.btn_desteg, 0, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_23)


        self.gridLayout.addWidget(self.frame_20, 0, 1, 1, 1)

        self.main_pages.addWidget(self.pg_esteg)
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.verticalLayout_13 = QVBoxLayout(self.pg_config)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_15 = QFrame(self.pg_config)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(123, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, -1, -1)
        self.scrollArea = QScrollArea(self.frame_16)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/*QFrame{\n"
"	border:0px;\n"
"}\n"
"*/\n"
"QPushButton{\n"
"	border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(54, 54, 54);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 110, 257))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 3, 2, 3)
        self.btn_config_cripto = QPushButton(self.scrollAreaWidgetContents)
        self.btn_config_cripto.setObjectName(u"btn_config_cripto")

        self.verticalLayout_16.addWidget(self.btn_config_cripto)

        self.btn_config_esteg = QPushButton(self.scrollAreaWidgetContents)
        self.btn_config_esteg.setObjectName(u"btn_config_esteg")

        self.verticalLayout_16.addWidget(self.btn_config_esteg)

        self.btn_config_style = QPushButton(self.scrollAreaWidgetContents)
        self.btn_config_style.setObjectName(u"btn_config_style")

        self.verticalLayout_16.addWidget(self.btn_config_style)

        self.btn_config_help = QPushButton(self.scrollAreaWidgetContents)
        self.btn_config_help.setObjectName(u"btn_config_help")

        self.verticalLayout_16.addWidget(self.btn_config_help)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_16.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_16.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_16.addWidget(self.pushButton_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.horizontalLayout_12.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.config_pages = QStackedWidget(self.frame_17)
        self.config_pages.setObjectName(u"config_pages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_17 = QVBoxLayout(self.page)
        self.verticalLayout_17.setSpacing(4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.frame_19 = QFrame(self.page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_13.addWidget(self.label_5)

        self.ed_keypass = QLineEdit(self.frame_19)
        self.ed_keypass.setObjectName(u"ed_keypass")
        self.ed_keypass.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_13.addWidget(self.ed_keypass)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_17.addWidget(self.frame_19)

        self.cb_simple_cripto = QCheckBox(self.page)
        self.cb_simple_cripto.setObjectName(u"cb_simple_cripto")

        self.verticalLayout_17.addWidget(self.cb_simple_cripto)

        self.frame_18 = QFrame(self.page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_aplicar = QPushButton(self.frame_18)
        self.btn_aplicar.setObjectName(u"btn_aplicar")
        self.btn_aplicar.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_14.addWidget(self.btn_aplicar)


        self.verticalLayout_17.addWidget(self.frame_18)

        self.config_pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.config_pages.addWidget(self.page_2)

        self.verticalLayout_15.addWidget(self.config_pages)


        self.horizontalLayout_12.addWidget(self.frame_17)


        self.verticalLayout_13.addWidget(self.frame_15)

        self.main_pages.addWidget(self.pg_config)
        self.pg_suporte = QWidget()
        self.pg_suporte.setObjectName(u"pg_suporte")
        self.verticalLayout_10 = QVBoxLayout(self.pg_suporte)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.frame_12 = QFrame(self.pg_suporte)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setSpacing(0)
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
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
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
        self.config_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toogle.setText("")
        self.lb_name.setText(QCoreApplication.translate("MainWindow", u"PyCripto", None))
        self.btn_cripto.setText(QCoreApplication.translate("MainWindow", u"Criptografar", None))
        self.btn_descripto.setText(QCoreApplication.translate("MainWindow", u"Descriptografar", None))
        self.btn_estegano.setText(QCoreApplication.translate("MainWindow", u"Esteganografar", None))
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
        self.path_dir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleciona o arquivo que deseja descobrir a senha", None))
#if QT_CONFIG(whatsthis)
        self.btn_open_dir.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_open_dir.setText("")
        self.lb_succes.setText("")
#if QT_CONFIG(whatsthis)
        self.btn_esteg.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Esconder Texto na imagem</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_esteg.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
#if QT_CONFIG(whatsthis)
        self.btn_desteg.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Descobrir o Texto escondido na imagem</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_desteg.setText(QCoreApplication.translate("MainWindow", u"Descobrir", None))
        self.btn_config_cripto.setText(QCoreApplication.translate("MainWindow", u"Criptografia", None))
        self.btn_config_esteg.setText(QCoreApplication.translate("MainWindow", u"Esteganografia", None))
        self.btn_config_style.setText(QCoreApplication.translate("MainWindow", u"Estilo", None))
        self.btn_config_help.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Palavra-Chave", None))
        self.cb_simple_cripto.setText(QCoreApplication.translate("MainWindow", u"Simple Cripto", None))
        self.btn_aplicar.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Esse \u00e9 um Software criado por Rigimon sobre criptografia\n"
"Email de Contato:\n"
"rigi.dev@hotmail.com\n"
"Doa\u00e7\u00f5es:", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o 0.1", None))
        self.lb_arroba.setText(QCoreApplication.translate("MainWindow", u"@Rigimon", None))
    # retranslateUi

