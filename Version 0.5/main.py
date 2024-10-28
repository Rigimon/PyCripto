from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow)
from PySide6 import QtCore
from ui_main import Ui_MainWindow
import os
import sys
import Rcripto as rc
import pyperclip
import Esteganografia as etg

CRIPTO_TYPE = ""
KEY_WORD = ""
END = ""
BITS = ""

try:
    with open("config.cfg","r") as arq:
        texto = arq.readlines()
        CRIPTO_TYPE = texto[0].split("=")[1].replace("\n","")
        KEY_WORD = texto[1].split("=")[1].replace("\n","")
        END = texto[2].split("=")[1].replace("\n","")
        BITS = texto[3].split("=")[1].replace("\n","")
except FileNotFoundError:
    with open("config.cfg","x") as arq:
        arq.write("SIMPLE_CRIPTO=\nKEY_WORD=\nEND=;\nBITS=")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyCripto")
        #appIcon = QIcon(u"icone.ico")
        #self.setWindowIcon(appIcon)

        ## TOGGLE BUTTON ##
        self.btn_toogle.clicked.connect(self.LeftMenu)

        ## CRIPTOGRAFAR PAGE BUTTONS ##
        self.btn_crip.clicked.connect(self.cripto)
        self.btn_paste_code.clicked.connect(lambda:pyperclip.copy(self.lb_codigo.text()))
        self.btn_paste_cript.clicked.connect(lambda:pyperclip.copy(self.lb_cript.text()))

        ## DESCRIPTOGRAFAR PAGE BUTTONS ##
        self.btn_descrip.clicked.connect(self.descripto)
        self.btn_paste_texto.clicked.connect(lambda:pyperclip.copy(self.lb_descripto_texto.text()))

        ## ESTEGANOGRAFAR PAGE BUTTONS ##
        self.btn_esteg.clicked.connect(self.estegano)
        self.btn_desteg.clicked.connect(self.destegano)
        self.btn_open_dir.clicked.connect(self.open_path)

        ## CONFIG PAGE BUTTONS ##
        self.btn_config_cripto.clicked.connect(self.ConfigPageCripto)
        self.btn_config_esteg.clicked.connect(self.ConfigPageEsteg)
        ### CONFIG CRIPT PAGE ###
        self.btn_cripto_aplicar.clicked.connect(self.Save)
        self.cb_simple_cripto.clicked.connect(self.ButtonSimpleCripto)
        ### CONFIG ESTEG PAGE ###
        self.btn_esteg_aplicar.clicked.connect(self.Save)

        ## LEFT MENU BUTTONS ##
        self.btn_cripto.clicked.connect(self.CriptoPage)
        self.btn_descripto.clicked.connect(self.DescriptoPage)
        self.btn_estegano.clicked.connect(self.EstegPage)
        self.btn_config.clicked.connect(self.ConfigPage)
        self.btn_suporte.clicked.connect(self.SuportePage)

        ### EXECUÇÃO ###
        self.CriptoPage()

    def CriptoPage(self):
        if CRIPTO_TYPE == "true":
            self.frame_5.setMaximumWidth(0)
        else:
            self.frame_5.setMaximumWidth(16777215)
        self.main_pages.setCurrentWidget(self.pg_cripto)
        self.btn_paste_code.setEnabled(False)
        self.btn_paste_cript.setEnabled(False)
        self.lb_cript.setText("")
        self.lb_codigo.setText("")
        self.ed_texto.setText("")

    def DescriptoPage(self):
        if CRIPTO_TYPE == "true":
            self.frame_9.setMaximumHeight(0)
        else:
            self.frame_9.setMaximumHeight(16777215)
        self.main_pages.setCurrentWidget(self.pg_descripto)
        self.btn_paste_texto.setEnabled(False)
        self.ed_descripto_texto.setText("")
        self.ed_descripto_code.setText("")
        self.lb_descripto_texto.setText("")

    def EstegPage(self):
        self.main_pages.setCurrentWidget(self.pg_esteg)
        self.path_dir.setText("")
        self.texte_esteg.setText("")
        self.lb_succes.setText("")
        
    def open_path(self):
            self.path = QFileDialog.getOpenFileNames(self, str("Open Files"),
                                                        f"C:/Users/{os.environ.get('USERNAME')}/Desktop")#, QFileDialog.ShowDirsOnly
                                                        #| QFileDialog.DontResolveSymlinks)
            #print(self.path[0])
            try:
                self.path_dir.setText(self.path[0][0])
            except IndexError:
                pass
            except Exception:
                print("erro")

    def ButtonSimpleCripto(self):
        if self.cb_simple_cripto.checkState() == QtCore.Qt.CheckState.Unchecked:
            self.ed_keypass.setDisabled(True)
        else:
            self.ed_keypass.setDisabled(False)

    def ConfigPage(self):
        self.main_pages.setCurrentWidget(self.pg_config)
        self.ConfigPageCripto()
    
    def ConfigPageCripto(self):
        self.config_pages.setCurrentWidget(self.pg_config_cripto)
        if CRIPTO_TYPE == "true":
            self.cb_simple_cripto.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.cb_simple_cripto.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.ButtonSimpleCripto()
        self.ed_keypass.setText(KEY_WORD)

    def ConfigPageEsteg(self):
        self.config_pages.setCurrentWidget(self.pg_config_esteg)
        self.ed_end.setText(END)

    def SuportePage(self):self.main_pages.setCurrentWidget(self.pg_suporte)

    def cripto(self):
        text = self.ed_texto.text()
        if text != "":
            self.btn_paste_code.setEnabled(True)
            self.btn_paste_cript.setEnabled(True)
            if CRIPTO_TYPE == "false":
                texto, code = rc.cripto(text)
                self.lb_codigo.setText(code)
            else:
                texto = rc.simple_cripto(text,KEY_WORD)
            self.lb_cript.setText(texto)

    def descripto(self):
        text = self.ed_descripto_texto.text()
        cod = self.ed_descripto_code.text()
        if CRIPTO_TYPE == "false":
            if text != "" and cod != "":
                self.btn_paste_texto.setEnabled(True)
                texto = rc.descripto(text, cod)
                self.lb_descripto_texto.setText(texto)
        else:
            if text != "":
                texto = rc.simple_descripto(text,KEY_WORD)
                self.lb_descripto_texto.setText(texto)

    def estegano(self):
        imagem = self.path_dir.text().replace("/","\\")
        texto = self.texte_esteg.toPlainText()
        result = etg.esteganografar(imagem, texto)
        if type(result) == tuple:
            self.lb_succes.setText(result[1])
        else:
            self.lb_succes.setText(result)

    def destegano(self):
        imagem = self.path_dir.text().replace("/","\\")
        texto = etg.desesteganografar(imagem)
        if type(texto) == tuple:
            self.lb_succes.setText(texto[1])
        else:
            self.lb_succes.setText("")
            self.texte_esteg.setPlainText(texto)

    def Save(self):
            global KEY_WORD, CRIPTO_TYPE, END, BITS
            KEY_WORD = self.ed_keypass.text()
            END = self.ed_end.text()
            if self.cb_simple_cripto.checkState() == QtCore.Qt.CheckState.Checked : CRIPTO_TYPE = "true"
            else : CRIPTO_TYPE = "false"
            with open("config.cfg","r") as arq:
                c = arq.readlines()
                c[0] = f"SIMPLE_CRIPTO={CRIPTO_TYPE}\n"
                c[1] = f"KEY_WORD={KEY_WORD}\n"
                c[2] = f"END={END}\n"
                c[3] = f"BITS={BITS}"
                c = c[0]+c[1]+c[2]+c[3]
            with open("config.cfg","w") as arq:
                arq.write(c)

    def LeftMenu(self):
        width = self.left_menu.width()

        if width == 0:
            newWidht = 200
        else:
            newWidht = 0

        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidht)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
