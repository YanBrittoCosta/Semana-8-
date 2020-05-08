# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmListRegistro.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

#QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import datetime

from os import getcwd
from sys import path, platform
path.extend(['/'.join(getcwd().split('/')[0:-4])])


from view.FrmAddRegistro import Ui_FrmAddRegistro
from controller.RegistroCTR import RegistroCTR

class Ui_FrmListRegistro(object):
    
    def PesquisarTodosRegistros(self):
        registro = RegistroCTR()
        query = registro.PesquisarTodosRegistros()
        total = 0
        while (self.gridRegistro.rowCount() > 0):
                self.gridRegistro.removeRow(0)

        for lin in range(0,len(query)):
            self.gridRegistro.insertRow(lin)
            total += 1
            for col in range(0,len(query[0])):
                self.gridRegistro.setItem(lin,col,QTableWidgetItem(str(query[lin][col])))
            
        self.lblTotal.setText('Total: '+str(total))

    def PesquisarRegistro_Click(self, tipo, valor):
        if valor == '':
            self.PesquisarTodosRegistros()

        else:
            registro = RegistroCTR()
            query = registro.PesquisarRegistro(tipo, valor)
            
            self.edtPesquisa.setText('')

            while (self.gridRegistro.rowCount() > 0):
                self.gridRegistro.removeRow(0)

            total = 0
            for lin in range(0,len(query)):
                self.gridRegistro.insertRow(lin)
                total += 1
                for col in range(0,len(query[0])):
                    self.gridRegistro.setItem(lin,col,QTableWidgetItem(str(query[lin][col])))
                
            self.lblTotal.setText('Total: '+str(total))

    def ExcluirRegistro_Click(self):

        linha = self.gridRegistro.currentItem().row()
        IDReg = self.gridRegistro.item(linha, 0).text()

        self.gridRegistro.removeRow(linha)
        registro = RegistroCTR()
        registro.ExcluirRegistro(IDReg)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registro Excluído!")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Excluir Registro")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def AlterarRegistro_Click(self):
    
        linha = self.gridRegistro.currentItem().row()
        
        IDReg = self.gridRegistro.item(linha, 0).text()
        Laboratorio = self.gridRegistro.item(linha, 1).text()
        NumeroPatri = self.gridRegistro.item(linha, 2).text()
        NumeroSerie = self.gridRegistro.item(linha, 3).text()
        Padrao = self.gridRegistro.item(linha, 4).text()
        Modelo = self.gridRegistro.item(linha, 5).text()
        Fabricante = self.gridRegistro.item(linha, 6).text()

        DataCali = self.gridRegistro.item(linha, 7).text()
        DataChec = self.gridRegistro.item(linha, 8).text()
        DataVenc = self.gridRegistro.item(linha, 9).text()
        DataProxCali = self.gridRegistro.item(linha, 10).text()
        DataSaida = self.gridRegistro.item(linha, 11).text()


        self.FrmAddRegistro = QtWidgets.QDialog()
        self.ui = Ui_FrmAddRegistro()
        self.ui.setupUi(self.FrmAddRegistro, 'alterar', IDReg)
        self.ui.PreencherAlterar(Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida)
        self.FrmAddRegistro.show()
        
            

    def setupUi(self, FrmListRegistro):
        FrmListRegistro.setObjectName("FrmListRegistro")
        FrmListRegistro.resize(942, 576)
        FrmListRegistro.setFixedSize(942, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/btnListarRegistro.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmListRegistro.setWindowIcon(icon)

        self.cbPesquisa = QtWidgets.QComboBox(FrmListRegistro)
        self.cbPesquisa.setGeometry(QtCore.QRect(20, 100, 161, 22))
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.setItemText(0, "")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")

        self.btnAlterar = QtWidgets.QPushButton(FrmListRegistro)
        self.btnAlterar.setGeometry(QtCore.QRect(700, 480, 101, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon1)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName("btnAlterar")
        #BTN ALTERAR CLICK
        self.btnAlterar.clicked.connect(lambda: self.AlterarRegistro_Click())

        self.lblTotal = QtWidgets.QLabel(FrmListRegistro)
        self.lblTotal.setGeometry(QtCore.QRect(20, 490, 111, 16))
        self.lblTotal.setObjectName("lblTotal")
        


        self.label = QtWidgets.QLabel(FrmListRegistro)
        self.label.setGeometry(QtCore.QRect(20, 70, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        

        self.gridRegistro = QtWidgets.QTableWidget(FrmListRegistro)
        self.gridRegistro.setGeometry(QtCore.QRect(10, 170, 911, 291))
        self.gridRegistro.setObjectName("gridRegistro")
        self.gridRegistro.setColumnCount(12)
        self.gridRegistro.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridRegistro.setHorizontalHeaderItem(11, item)
        #AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridRegistro.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridRegistro.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gridRegistro.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        

        self.edtPesquisa = QtWidgets.QLineEdit(FrmListRegistro)
        self.edtPesquisa.setGeometry(QtCore.QRect(190, 100, 451, 20))
        self.edtPesquisa.setObjectName("edtPesquisa")

    
        self.btnPesquisar = QtWidgets.QPushButton(FrmListRegistro)
        self.btnPesquisar.setGeometry(QtCore.QRect(670, 80, 111, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/Lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon2)
        self.btnPesquisar.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisar.setObjectName("btnPesquisar")
        #BTN PESQUISAR CLICK 
        self.btnPesquisar.clicked.connect(lambda: self.PesquisarRegistro_Click(self.cbPesquisa.currentText(),self.edtPesquisa.text()))


        self.btnExcluir = QtWidgets.QPushButton(FrmListRegistro)
        self.btnExcluir.setGeometry(QtCore.QRect(820, 480, 91, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon3)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName("btnExcluir")
        #BTN EXCLUIR CLICK
        self.btnExcluir.clicked.connect(lambda: self.ExcluirRegistro_Click())

        self.retranslateUi(FrmListRegistro)
        QtCore.QMetaObject.connectSlotsByName(FrmListRegistro)

        self.PesquisarTodosRegistros()

        

    def retranslateUi(self, FrmListRegistro):
        _translate = QtCore.QCoreApplication.translate
        FrmListRegistro.setWindowTitle(_translate("FrmListRegistro", "Listar Registro"))
        self.cbPesquisa.setItemText(0, _translate("FrmListRegistro", "ID"))
        self.cbPesquisa.setItemText(1, _translate("FrmListRegistro", "Padrão"))
        self.cbPesquisa.setItemText(2, _translate("FrmListRegistro", "Número de Série"))
        self.cbPesquisa.setItemText(3, _translate("FrmListRegistro", "Patrimônio"))
        self.btnAlterar.setText(_translate("FrmListRegistro", "Alterar"))
        self.lblTotal.setText(_translate("FrmListRegistro", "Total:"))
        self.label.setText(_translate("FrmListRegistro", "Selecione o Tipo de Pesquisa:"))
        item = self.gridRegistro.horizontalHeaderItem(0)
        item.setText(_translate("FrmListRegistro", "ID"))
        item = self.gridRegistro.horizontalHeaderItem(1)
        item.setText(_translate("FrmListRegistro", "Laboratório"))
        item = self.gridRegistro.horizontalHeaderItem(2)
        item.setText(_translate("FrmListRegistro", "Patrimônio"))
        item = self.gridRegistro.horizontalHeaderItem(3)
        item.setText(_translate("FrmListRegistro", "Número de Série"))
        item = self.gridRegistro.horizontalHeaderItem(4)
        item.setText(_translate("FrmListRegistro", "Padrão"))
        item = self.gridRegistro.horizontalHeaderItem(5)
        item.setText(_translate("FrmListRegistro", "Modelo"))
        item = self.gridRegistro.horizontalHeaderItem(6)
        item.setText(_translate("FrmListRegistro", "Fabricante"))
        item = self.gridRegistro.horizontalHeaderItem(7)
        item.setText(_translate("FrmListRegistro", "Data de Cali"))
        item = self.gridRegistro.horizontalHeaderItem(8)
        item.setText(_translate("FrmListRegistro", "Data de Chec"))
        item = self.gridRegistro.horizontalHeaderItem(9)
        item.setText(_translate("FrmListRegistro", "Data de Venc"))
        item = self.gridRegistro.horizontalHeaderItem(10)
        item.setText(_translate("FrmListRegistro", "Data Próx Cali"))
        item = self.gridRegistro.horizontalHeaderItem(11)
        item.setText(_translate("FrmListRegistro", "Data de Saída"))
        self.btnPesquisar.setText(_translate("FrmListRegistro", "Pesquisar"))
        self.btnExcluir.setText(_translate("FrmListRegistro", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmListRegistro = QtWidgets.QDialog()
    ui = Ui_FrmListRegistro()
    ui.setupUi(FrmListRegistro)
    FrmListRegistro.show()
    sys.exit(app.exec_())
