# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmAddCertificado.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmAddCertificado(object):
    def setupUi(self, FrmAddCertificado):
        FrmAddCertificado.setObjectName("FrmAddCertificado")
        FrmAddCertificado.resize(652, 556)
        FrmAddCertificado.setFixedSize(652, 556)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/btnAdicionarCertificado.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmAddCertificado.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(FrmAddCertificado)
        self.tableWidget.setGeometry(QtCore.QRect(20, 260, 611, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.btnInsert = QtWidgets.QPushButton(FrmAddCertificado)
        self.btnInsert.setGeometry(QtCore.QRect(530, 470, 101, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInsert.setIcon(icon1)
        self.btnInsert.setIconSize(QtCore.QSize(30, 30))
        self.btnInsert.setObjectName("btnInsert")

        self.tabWidget = QtWidgets.QTabWidget(FrmAddCertificado)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 611, 201))
        self.tabWidget.setObjectName("tabWidget")
        self.tabDiretorio = QtWidgets.QWidget()
        self.tabDiretorio.setObjectName("tabDiretorio")

        self.labelHelp = QtWidgets.QLabel(self.tabDiretorio)
        self.labelHelp.setGeometry(QtCore.QRect(20, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelHelp.setFont(font)
        self.labelHelp.setObjectName("labelHelp")

        self.btnFolder = QtWidgets.QPushButton(self.tabDiretorio)
        self.btnFolder.setGeometry(QtCore.QRect(20, 60, 121, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/folder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFolder.setIcon(icon2)
        self.btnFolder.setObjectName("btnFolder")

        self.labelNomeDir = QtWidgets.QLabel(self.tabDiretorio)
        self.labelNomeDir.setGeometry(QtCore.QRect(20, 100, 51, 21))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(True)
        self.labelNomeDir.setFont(font)
        self.labelNomeDir.setObjectName("labelNomeDir")

        self.labelDir = QtWidgets.QLabel(self.tabDiretorio)
        self.labelDir.setGeometry(QtCore.QRect(80, 100, 411, 21))
        self.labelDir.setText("")
        self.labelDir.setObjectName("labelDir")
        self.tabWidget.addTab(self.tabDiretorio, "")


        self.tabRegistro = QtWidgets.QWidget()
        self.tabRegistro.setObjectName("tabRegistro")


        self.labelID = QtWidgets.QLabel(self.tabRegistro)
        self.labelID.setGeometry(QtCore.QRect(20, 20, 21, 16))
        self.labelID.setObjectName("labelID")

        self.lineEditID = QtWidgets.QLineEdit(self.tabRegistro)
        self.lineEditID.setGeometry(QtCore.QRect(20, 40, 81, 20))
        self.lineEditID.setObjectName("lineEditID")

        self.labelPad = QtWidgets.QLabel(self.tabRegistro)
        self.labelPad.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.labelPad.setObjectName("labelPad")

        self.lineEditPad = QtWidgets.QLineEdit(self.tabRegistro)
        self.lineEditPad.setGeometry(QtCore.QRect(20, 100, 191, 20))
        self.lineEditPad.setObjectName("lineEditPad")

        self.lineEditFab = QtWidgets.QLineEdit(self.tabRegistro)
        self.lineEditFab.setGeometry(QtCore.QRect(250, 40, 113, 20))
        self.lineEditFab.setObjectName("lineEditFab")

        self.lineEditPatri = QtWidgets.QLineEdit(self.tabRegistro)
        self.lineEditPatri.setGeometry(QtCore.QRect(250, 100, 231, 20))
        self.lineEditPatri.setObjectName("lineEditPatri")

        self.labelFab = QtWidgets.QLabel(self.tabRegistro)
        self.labelFab.setGeometry(QtCore.QRect(250, 20, 51, 16))
        self.labelFab.setObjectName("labelFab")

        self.labelPatri = QtWidgets.QLabel(self.tabRegistro)
        self.labelPatri.setGeometry(QtCore.QRect(250, 80, 61, 16))
        self.labelPatri.setObjectName("labelPatri")
        
        self.pushButton = QtWidgets.QPushButton(self.tabRegistro)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tabRegistro, "")

        self.retranslateUi(FrmAddCertificado)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FrmAddCertificado)

    def retranslateUi(self, FrmAddCertificado):
        _translate = QtCore.QCoreApplication.translate
        FrmAddCertificado.setWindowTitle(_translate("FrmAddCertificado", "Adicionar Certificado"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FrmAddCertificado", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FrmAddCertificado", "Padrão"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FrmAddCertificado", "Fabricante"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FrmAddCertificado", "Patrimônio"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FrmAddCertificado", "Data Cali"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FrmAddCertificado", "Data Prox Cali"))
        self.btnInsert.setText(_translate("FrmAddCertificado", "inserir"))
        self.labelHelp.setText(_translate("FrmAddCertificado", "Inserir a pasta com os certificados.xlsx"))
        self.btnFolder.setText(_translate("FrmAddCertificado", "Pesquisar Pasta"))
        self.labelNomeDir.setText(_translate("FrmAddCertificado", "Diretório:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDiretorio), _translate("FrmAddCertificado", "Tab 1"))
        self.labelID.setText(_translate("FrmAddCertificado", "ID"))
        self.labelPad.setText(_translate("FrmAddCertificado", "Padrão"))
        self.labelFab.setText(_translate("FrmAddCertificado", "Fabricante"))
        self.labelPatri.setText(_translate("FrmAddCertificado", "Patrimônio"))
        self.pushButton.setText(_translate("FrmAddCertificado", "Limpar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRegistro), _translate("FrmAddCertificado", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmAddCertificado = QtWidgets.QDialog()
    ui = Ui_FrmAddCertificado()
    ui.setupUi(FrmAddCertificado)
    FrmAddCertificado.show()
    sys.exit(app.exec_())
