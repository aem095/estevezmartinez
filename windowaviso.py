# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowaviso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Aviso(object):
    def setupUi(self, Aviso):
        Aviso.setObjectName("Aviso")
        Aviso.resize(360, 200)
        Aviso.setModal(True)
        self.btnBoxAviso = QtWidgets.QDialogButtonBox(Aviso)
        self.btnBoxAviso.setGeometry(QtCore.QRect(100, 140, 151, 32))
        self.btnBoxAviso.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.btnBoxAviso.setOrientation(QtCore.Qt.Horizontal)
        self.btnBoxAviso.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxAviso.setObjectName("btnBoxAviso")
        self.lblimagenaviso = QtWidgets.QLabel(Aviso)
        self.lblimagenaviso.setGeometry(QtCore.QRect(120, 0, 111, 101))
        self.lblimagenaviso.setText("")
        self.lblimagenaviso.setPixmap(QtGui.QPixmap("img/Warning.png"))
        self.lblimagenaviso.setScaledContents(True)
        self.lblimagenaviso.setObjectName("lblimagenaviso")
        self.lblaviso = QtWidgets.QLabel(Aviso)
        self.lblaviso.setGeometry(QtCore.QRect(100, 90, 191, 61))
        self.lblaviso.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.lblaviso.setObjectName("lblaviso")

        self.retranslateUi(Aviso)
        self.btnBoxAviso.accepted.connect(Aviso.accept)
        self.btnBoxAviso.rejected.connect(Aviso.reject)
        QtCore.QMetaObject.connectSlotsByName(Aviso)

    def retranslateUi(self, Aviso):
        _translate = QtCore.QCoreApplication.translate
        Aviso.setWindowTitle(_translate("Aviso", "Dialog"))
        self.lblaviso.setText(_translate("Aviso", "¿Desea Salir?"))
