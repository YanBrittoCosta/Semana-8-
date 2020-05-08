# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from os import getcwd
from sys import path, platform

path.extend(['/'.join(getcwd().split('/')[0:-4])])

from view.FrmAddRegistro import Ui_FrmAddRegistro
from view.FrmListRegistro import Ui_FrmListRegistro
from view.FrmAddCertificado import Ui_FrmAddCertificado


class Ui_FrmPrincipal(object):

    #btn FrmAddRegistro.CLICK
    def FrmAddRegistro_Click(self):
        self.FrmAddRegistro = QtWidgets.QMainWindow()
        self.ui = Ui_FrmAddRegistro()
        self.ui.setupUi(self.FrmAddRegistro,'adicionar',0)
        self.FrmAddRegistro.show()

    #btn FrmListRegistro.CLICK
    def FrmListRegistro_Click(self):
        self.FrmListRegistro = QtWidgets.QMainWindow()
        self.ui = Ui_FrmListRegistro()
        self.ui.setupUi(self.FrmListRegistro)
        self.FrmListRegistro.show()

    #btn FrmAddCertificado.CLICK
    def FrmAddCertificado_Click(self):
        self.FrmAddCertificado = QtWidgets.QMainWindow()
        self.ui = Ui_FrmAddCertificado()
        self.ui.setupUi(self.FrmAddCertificado)
        self.FrmAddCertificado.show()


    def setupUi(self, FrmPrincipal):

        FrmPrincipal.setObjectName("FrmPrincipal")
        FrmPrincipal.resize(800, 420)
        FrmPrincipal.setFixedSize(800, 420)
        FrmPrincipal.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.btnsFrame = QtWidgets.QFrame(self.centralwidget)
        self.btnsFrame.setGeometry(QtCore.QRect(19, 10, 761, 111))
        self.btnsFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.btnsFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.btnsFrame.setObjectName("btnsFrame")

        self.splitter = QtWidgets.QSplitter(self.btnsFrame)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 721, 71))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.btnAdicionarRegistro = QtWidgets.QPushButton(self.splitter)
        self.btnAdicionarRegistro.setStyleSheet("background-color: rgb(241, 241, 241);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/btnAdicionarRegistro.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdicionarRegistro.setIcon(icon)
        self.btnAdicionarRegistro.setIconSize(QtCore.QSize(30, 30))
        self.btnAdicionarRegistro.setObjectName("btnAdicionarRegistro")

        #BTN ADICIONAR REGISTRO CLICK EVENT
        self.btnAdicionarRegistro.clicked.connect(self.FrmAddRegistro_Click)
        
        self.btnListarRegistro = QtWidgets.QPushButton(self.splitter)
        self.btnListarRegistro.setStyleSheet("background-color: rgb(241, 241, 241);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/btnListarRegistro.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListarRegistro.setIcon(icon1)
        self.btnListarRegistro.setIconSize(QtCore.QSize(30, 30))
        self.btnListarRegistro.setObjectName("btnListarRegistro")
        #BTN LISTAR REGISTRO CLICK EVENT
        self.btnListarRegistro.clicked.connect(self.FrmListRegistro_Click)

        self.btnAdicionarCertificado = QtWidgets.QPushButton(self.splitter)
        self.btnAdicionarCertificado.setStyleSheet("background-color: rgb(241, 241, 241);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/btnAdicionarCertificado.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdicionarCertificado.setIcon(icon2)
        self.btnAdicionarCertificado.setIconSize(QtCore.QSize(30, 30))
        self.btnAdicionarCertificado.setObjectName("btnAdicionarCertificado")
        #BTN ADICIONAR CERTIFICADO CLICK EVENT
        self.btnAdicionarCertificado.clicked.connect(self.FrmAddCertificado_Click)

        self.btnEstabilidade = QtWidgets.QPushButton(self.splitter)
        self.btnEstabilidade.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.btnListarCertificado = QtWidgets.QPushButton(self.splitter)
        self.btnListarCertificado.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.btnListarCertificado.setIcon(icon1)
        self.btnListarCertificado.setIconSize(QtCore.QSize(30, 30))
        self.btnListarCertificado.setObjectName("btnListarCertificado")
        #BTN LISTAR CERTIFICADO CLICK EVENT
        #self.btnListarCertificado.clicked.connect()


        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/btnEstabilidade.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEstabilidade.setIcon(icon3)
        self.btnEstabilidade.setIconSize(QtCore.QSize(30, 30))
        self.btnEstabilidade.setObjectName("btnEstabilidade")
        #BTN ESTABILIDADE CLICK EVENT
        #self.btnEstabilidade.clicked.connect()

        

        

        self.BGImage = QtWidgets.QLabel(self.centralwidget)
        self.BGImage.setGeometry(QtCore.QRect(20, 129, 760, 241))
        self.BGImage.setFrameShape(QtWidgets.QFrame.Box)
        self.BGImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BGImage.setLineWidth(2)
        self.BGImage.setText("")
        self.BGImage.setPixmap(QtGui.QPixmap("Images/BGImageFinal.png"))
        self.BGImage.setObjectName("BGImage")
        FrmPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FrmPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmPrincipal)
        self.statusbar.setObjectName("statusbar")
        FrmPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

    def retranslateUi(self, FrmPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FrmPrincipal.setWindowTitle(_translate("FrmPrincipal", "Registro de Certificado"))
        self.btnAdicionarRegistro.setText(_translate("FrmPrincipal", "Adicionar Registro"))
        self.btnListarRegistro.setText(_translate("FrmPrincipal", "Listar Registro"))
        self.btnAdicionarCertificado.setText(_translate("FrmPrincipal", "Adicionar Certificado"))
        self.btnListarCertificado.setText(_translate("FrmPrincipal", "Listar Certificado"))
        self.btnEstabilidade.setText(_translate("FrmPrincipal", "Estabilidade"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())
