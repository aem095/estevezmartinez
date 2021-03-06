# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(400, 90, 211, 41))
        self.lblClientes.setStyleSheet("font: 75 italic 18pt \"Noto Sans\";")
        self.lblClientes.setObjectName("lblClientes")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(400, 340, 83, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(500, 340, 82, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 270, 185, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblSexo = QtWidgets.QLabel(self.layoutWidget)
        self.lblSexo.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblSexo.setObjectName("lblSexo")
        self.horizontalLayout.addWidget(self.lblSexo)
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtFem.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.horizontalLayout.addWidget(self.rbtFem)
        self.rbtHom = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtHom.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.rbtHom.setObjectName("rbtHom")
        self.rbtGroupSex.addButton(self.rbtHom)
        self.horizontalLayout.addWidget(self.rbtHom)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 300, 472, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblFormaDePago = QtWidgets.QLabel(self.layoutWidget1)
        self.lblFormaDePago.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblFormaDePago.setObjectName("lblFormaDePago")
        self.horizontalLayout_2.addWidget(self.lblFormaDePago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.chkGroupPago = QtWidgets.QButtonGroup(MainWindow)
        self.chkGroupPago.setObjectName("chkGroupPago")
        self.chkGroupPago.setExclusive(False)
        self.chkGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_2.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_2.addWidget(self.chkTarjeta)
        self.chkCargoCuenta = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chkCargoCuenta.setObjectName("chkCargoCuenta")
        self.chkGroupPago.addButton(self.chkCargoCuenta)
        self.horizontalLayout_2.addWidget(self.chkCargoCuenta)
        self.chkTransfe = QtWidgets.QCheckBox(self.layoutWidget1)
        self.chkTransfe.setObjectName("chkTransfe")
        self.chkGroupPago.addButton(self.chkTransfe)
        self.horizontalLayout_2.addWidget(self.chkTransfe)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(230, 210, 511, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDir = QtWidgets.QLabel(self.layoutWidget2)
        self.lblDir.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_3.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(self.layoutWidget2)
        self.txtDir.setEnabled(True)
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_3.addWidget(self.txtDir)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(230, 180, 511, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblApel = QtWidgets.QLabel(self.layoutWidget3)
        self.lblApel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_4.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(self.layoutWidget3)
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_4.addWidget(self.txtApel)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblNome = QtWidgets.QLabel(self.layoutWidget3)
        self.lblNome.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblNome.setObjectName("lblNome")
        self.horizontalLayout_4.addWidget(self.lblNome)
        self.txtNome = QtWidgets.QLineEdit(self.layoutWidget3)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout_4.addWidget(self.txtNome)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(230, 150, 231, 25))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblDNI = QtWidgets.QLabel(self.layoutWidget4)
        self.lblDNI.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout_5.addWidget(self.lblDNI)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.txtDNI = QtWidgets.QLineEdit(self.layoutWidget4)
        self.txtDNI.setObjectName("txtDNI")
        self.horizontalLayout_5.addWidget(self.txtDNI)
        self.lblValidoDni = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidoDni.sizePolicy().hasHeightForWidth())
        self.lblValidoDni.setSizePolicy(sizePolicy)
        self.lblValidoDni.setText("")
        self.lblValidoDni.setObjectName("lblValidoDni")
        self.horizontalLayout_5.addWidget(self.lblValidoDni)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(230, 240, 201, 21))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblPro = QtWidgets.QLabel(self.layoutWidget5)
        self.lblPro.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblPro.setObjectName("lblPro")
        self.horizontalLayout_6.addWidget(self.lblPro)
        self.cmbPro = QtWidgets.QComboBox(self.layoutWidget5)
        self.cmbPro.setObjectName("cmbPro")
        self.horizontalLayout_6.addWidget(self.cmbPro)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(500, 240, 241, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(1, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.lblMun = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblMun.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblMun.setObjectName("lblMun")
        self.horizontalLayout_7.addWidget(self.lblMun)
        self.cmbMun = QtWidgets.QComboBox(self.layoutWidget_2)
        self.cmbMun.setObjectName("cmbMun")
        self.horizontalLayout_7.addWidget(self.cmbMun)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 150, 271, 26))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblAlta = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblAlta.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lblAlta.setObjectName("lblAlta")
        self.horizontalLayout_8.addWidget(self.lblAlta)
        self.txtFechaAlta = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txtFechaAlta.setObjectName("txtFechaAlta")
        self.horizontalLayout_8.addWidget(self.txtFechaAlta)
        self.btnCalendario = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnCalendario.setFont(font)
        self.btnCalendario.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendario.setIcon(icon)
        self.btnCalendario.setObjectName("btnCalendario")
        self.horizontalLayout_8.addWidget(self.btnCalendario)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblClientes.setText(_translate("MainWindow", "XESTI??N CLIENTES"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo:"))
        self.rbtFem.setText(_translate("MainWindow", "Mujer"))
        self.rbtHom.setText(_translate("MainWindow", "Hombre"))
        self.lblFormaDePago.setText(_translate("MainWindow", "Forma de Pago:"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkCargoCuenta.setText(_translate("MainWindow", "Cargo en cuenta"))
        self.chkTransfe.setText(_translate("MainWindow", "Transferencia"))
        self.lblDir.setText(_translate("MainWindow", "Direcci??n:"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblNome.setText(_translate("MainWindow", "Nombre:"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.lblPro.setText(_translate("MainWindow", "Provincia:"))
        self.lblMun.setText(_translate("MainWindow", "Municipio:"))
        self.lblAlta.setText(_translate("MainWindow", "Fecha Alta:"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
