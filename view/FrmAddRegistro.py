# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmAddRegistro2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime

from os import getcwd
from sys import path, platform
path.extend(['/'.join(getcwd().split('/')[0:-4])])

from controller.RegistroCTR import RegistroCTR


class Ui_FrmAddRegistro(object):

    #PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self,Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida):


        self.lineEditLab.setText(Laboratorio)
        self.lineEditPatri.setText(NumeroPatri)
        self.lineEditNSer.setText(NumeroSerie)
        self.lineEditPad.setText(Padrao)
        self.lineEditMod.setText(Modelo)
        self.lineEditFab.setText(Fabricante)
        self.dateEditCali.setDate(datetime.date(year=int(DataCali[6:]), month=int(DataCali[3:5]), day=int(DataCali[0:2])))
        self.dateEditChec.setDate(datetime.date(year=int(DataChec[6:]), month=int(DataChec[3:5]), day=int(DataChec[0:2])))
        self.dateEditVenc.setDate(datetime.date(year=int(DataVenc[6:]), month=int(DataVenc[3:5]), day=int(DataVenc[0:2])))
        self.dateEditProxCali.setDate(datetime.date(year=int(DataProxCali[6:]), month=int(DataProxCali[3:5]), day=int(DataProxCali[0:2])))
        self.dateEditSaida.setDate(datetime.date(year=int(DataSaida[6:]), month=int(DataSaida[3:5]), day=int(DataSaida[0:2])))
        

    #CLICK BTN_SALVAR
    def btnSalvar_Click(self, estado, IDReg):

        Laboratorio = self.lineEditLab.text()
        NumeroPatri = self.lineEditPatri.text()
        NumeroSerie = self.lineEditNSer.text()
        Padrao = self.lineEditPad.text()
        Modelo = self.lineEditMod.text()
        Fabricante = self.lineEditFab.text()
        DataCali = self.dateEditCali.text()
        DataChec = self.dateEditChec.text()
        DataVenc = self.dateEditVenc.text()
        DataProxCali = self.dateEditProxCali.text()
        DataSaida = self.dateEditSaida.text()

        #VERIFICA O ESTADO INSERIR/ALTERAR PARA CHAMAR A FUNÇAO APROPRIADA
        if estado=='adicionar':
            registro = RegistroCTR()
            registro.CadastrarRegistro(Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Registro inserido com sucesso!")
            msg.setWindowTitle("Adicionar Registro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        if estado=='alterar':
            registro = RegistroCTR()
            registro.AtualizarRegistro(IDReg,Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Registro alterado com sucesso!")
            msg.setWindowTitle("Alterar Registro")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        self.lineEditLab.setText('')
        self.lineEditPatri.setText('')
        self.lineEditNSer.setText('')
        self.lineEditPad.setText('')
        self.lineEditMod.setText('')
        self.lineEditFab.setText('')
        self.dateEditCali.setDate(datetime.date(year=2020, month=1, day=1))
        self.dateEditChec.setDate(datetime.date(year=2020, month=1, day=1))
        self.dateEditVenc.setDate(datetime.date(year=2020, month=1, day=1))
        self.dateEditProxCali.setDate(datetime.date(year=2020, month=1, day=1))
        self.dateEditSaida.setDate(datetime.date(year=2020, month=1, day=1))

    



    def setupUi(self, FrmAddRegistro, estado, IDReg):


        FrmAddRegistro.setObjectName("FrmAddRegistro")
        FrmAddRegistro.resize(630, 577)
        FrmAddRegistro.setFixedSize(630, 577)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/btnAdicionarRegistro.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmAddRegistro.setWindowIcon(icon)
        FrmAddRegistro.setAutoFillBackground(False)
        FrmAddRegistro.setStyleSheet("border-top-color: rgb(135, 181, 255);\n""")

        self.TopFrame = QtWidgets.QFrame(FrmAddRegistro)
        self.TopFrame.setGeometry(QtCore.QRect(31, 21, 541, 401))
        self.TopFrame.setSizeIncrement(QtCore.QSize(10, 10))
        self.TopFrame.setBaseSize(QtCore.QSize(10, 10))
        self.TopFrame.setAutoFillBackground(False)
        self.TopFrame.setStyleSheet("")
        self.TopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopFrame.setObjectName("TopFrame")
        self.layoutWidget = QtWidgets.QWidget(self.TopFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 241, 377))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.lineEditPatri = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPatri.setObjectName("lineEditPatri")
        self.gridLayout.addWidget(self.lineEditPatri, 14, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)

        self.labelMod = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMod.setFont(font)
        self.labelMod.setObjectName("labelMod")
        self.gridLayout.addWidget(self.labelMod, 10, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)

        self.lineEditNSer = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNSer.setObjectName("lineEditNSer")
        self.gridLayout.addWidget(self.lineEditNSer, 17, 0, 1, 1)

        self.labelNSerie = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNSerie.setFont(font)
        self.labelNSerie.setObjectName("labelNSerie")
        self.gridLayout.addWidget(self.labelNSerie, 16, 0, 1, 1)

        self.lineEditMod = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditMod.setObjectName("lineEditMod")
        self.gridLayout.addWidget(self.lineEditMod, 11, 0, 1, 1)

        self.labelLab = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLab.setFont(font)
        self.labelLab.setObjectName("labelLab")
        self.gridLayout.addWidget(self.labelLab, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)

        self.labelPatri = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPatri.setFont(font)
        self.labelPatri.setObjectName("labelPatri")
        self.gridLayout.addWidget(self.labelPatri, 13, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 15, 0, 1, 1)

        self.lineEditFab = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditFab.setObjectName("lineEditFab")
        self.gridLayout.addWidget(self.lineEditFab, 8, 0, 1, 1)

        self.labelFab = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFab.setFont(font)
        self.labelFab.setObjectName("labelFab")
        self.gridLayout.addWidget(self.labelFab, 7, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 12, 0, 1, 1)

        self.lineEditLab = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditLab.setObjectName("lineEditLab")
        self.gridLayout.addWidget(self.lineEditLab, 2, 0, 1, 1)

        self.labelPad = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPad.setFont(font)
        self.labelPad.setObjectName("labelPad")
        self.gridLayout.addWidget(self.labelPad, 4, 0, 1, 1)

        self.lineEditPad = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPad.setObjectName("lineEditPad")
        self.gridLayout.addWidget(self.lineEditPad, 5, 0, 1, 1)

        self.groupBox = QtWidgets.QGroupBox(self.TopFrame)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 521, 401))
        self.groupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(330, 10, 158, 311))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(13, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)

        self.labelDCali = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDCali.setFont(font)
        self.labelDCali.setObjectName("labelDCali")
        self.gridLayout_2.addWidget(self.labelDCali, 1, 0, 1, 1)

        self.dateEditCali = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEditCali.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditCali.setObjectName("dateEditCali")
        self.gridLayout_2.addWidget(self.dateEditCali, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 3, 0, 1, 1)

        self.labelDChec = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDChec.setFont(font)
        self.labelDChec.setObjectName("labelDChec")
        self.gridLayout_2.addWidget(self.labelDChec, 4, 0, 1, 1)

        self.dateEditChec = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEditChec.setObjectName("dateEditChec")
        self.gridLayout_2.addWidget(self.dateEditChec, 5, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 6, 0, 1, 1)

        self.labelDVenc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDVenc.setFont(font)
        self.labelDVenc.setObjectName("labelDVenc")
        self.gridLayout_2.addWidget(self.labelDVenc, 7, 0, 1, 1)

        self.dateEditVenc = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEditVenc.setObjectName("dateEditVenc")
        self.gridLayout_2.addWidget(self.dateEditVenc, 8, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 9, 0, 1, 1)

        self.labelDProCali = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDProCali.setFont(font)
        self.labelDProCali.setObjectName("labelDProCali")
        self.gridLayout_2.addWidget(self.labelDProCali, 10, 0, 1, 1)

        self.dateEditProxCali = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEditProxCali.setObjectName("dateEditProxCali")
        self.gridLayout_2.addWidget(self.dateEditProxCali, 11, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 12, 0, 1, 1)

        self.labelDSaida = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDSaida.setFont(font)
        self.labelDSaida.setObjectName("labelDSaida")
        self.gridLayout_2.addWidget(self.labelDSaida, 13, 0, 1, 1)

        self.dateEditSaida = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEditSaida.setObjectName("dateEditSaida")
        self.gridLayout_2.addWidget(self.dateEditSaida, 14, 0, 1, 1)

        self.groupBox.raise_()
        self.layoutWidget.raise_()
        self.DownFrame = QtWidgets.QFrame(FrmAddRegistro)
        self.DownFrame.setGeometry(QtCore.QRect(30, 430, 541, 101))
        self.DownFrame.setAutoFillBackground(False)
        self.DownFrame.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.DownFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DownFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DownFrame.setObjectName("DownFrame")
        self.groupBox_2 = QtWidgets.QGroupBox(self.DownFrame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 521, 81))
        self.groupBox_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_2.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.btnSalvar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(420, 10, 91, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSalvar.setFont(font)
        self.btnSalvar.setAutoFillBackground(False)
        self.btnSalvar.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon)
        self.btnSalvar.setIconSize(QtCore.QSize(26, 40))
        self.btnSalvar.setObjectName("btnSalvar")
        #BTN SALVAR
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, IDReg))

        self.retranslateUi(FrmAddRegistro)
        QtCore.QMetaObject.connectSlotsByName(FrmAddRegistro)

    def retranslateUi(self, FrmAddRegistro):
        _translate = QtCore.QCoreApplication.translate
        FrmAddRegistro.setWindowTitle(_translate("FrmAddRegistro", "FrmAddRegistro"))
        self.labelMod.setText(_translate("FrmAddRegistro", "Modelo"))
        self.labelNSerie.setText(_translate("FrmAddRegistro", "Número de Série"))
        self.labelLab.setText(_translate("FrmAddRegistro", "Labortório"))
        self.labelPatri.setText(_translate("FrmAddRegistro", "Patrimônio"))
        self.labelFab.setText(_translate("FrmAddRegistro", "Fabricante"))
        self.labelPad.setText(_translate("FrmAddRegistro", "Padrão"))
        self.labelDCali.setText(_translate("FrmAddRegistro", "Data de Calibração"))
        self.labelDChec.setText(_translate("FrmAddRegistro", "Data de Checagem"))
        self.labelDVenc.setText(_translate("FrmAddRegistro", "Data de Vencimento"))
        self.labelDProCali.setText(_translate("FrmAddRegistro", "Data da Próxima Calibração"))
        self.labelDSaida.setText(_translate("FrmAddRegistro", "Data de Saída"))
        self.btnSalvar.setText(_translate("FrmAddRegistro", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmAddRegistro = QtWidgets.QDialog()
    ui = Ui_FrmAddRegistro()
    ui.setupUi(FrmAddRegistro)
    FrmAddRegistro.show()
    sys.exit(app.exec_())
