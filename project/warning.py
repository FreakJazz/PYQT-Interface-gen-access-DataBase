# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Advertencia(object):
    def setupUi(self, Advertencia):
        Advertencia.setObjectName("Advertencia")
        Advertencia.resize(320, 101)
        self.buttonBox = QtWidgets.QDialogButtonBox(Advertencia)
        self.buttonBox.setGeometry(QtCore.QRect(10, 60, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Advertencia)
        self.label.setGeometry(QtCore.QRect(30, 30, 241, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Advertencia)
        self.buttonBox.accepted.connect(Advertencia.accept)
        self.buttonBox.rejected.connect(Advertencia.reject)
        QtCore.QMetaObject.connectSlotsByName(Advertencia)

    def retranslateUi(self, Advertencia):
        _translate = QtCore.QCoreApplication.translate
        Advertencia.setWindowTitle(_translate("Advertencia", "Dialog"))
        self.label.setText(_translate("Advertencia", "Debe seleccionar un documento para continuar"))
