# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalisysCheck(object):
    def setupUi(self, AnalisysCheck):
        AnalisysCheck.setObjectName("AnalisysCheck")
        AnalisysCheck.setEnabled(True)
        AnalisysCheck.resize(300, 387)
        AnalisysCheck.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(AnalisysCheck)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(20, 130, 261, 221))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Seleccion = QtWidgets.QScrollArea(self.frame)
        self.Seleccion.setGeometry(QtCore.QRect(10, 40, 201, 121))
        self.Seleccion.setWidgetResizable(True)
        self.Seleccion.setObjectName("Seleccion")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.splitter = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 138, 85))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pichincha = QtWidgets.QRadioButton(self.splitter)
        self.pichincha.setObjectName("pichincha")
        self.produbanco = QtWidgets.QRadioButton(self.splitter)
        self.produbanco.setObjectName("produbanco")
        self.pacifico = QtWidgets.QRadioButton(self.splitter)
        self.pacifico.setObjectName("pacifico")
        self.cfn = QtWidgets.QRadioButton(self.splitter)
        self.cfn.setObjectName("cfn")
        self.isffa = QtWidgets.QRadioButton(self.splitter)
        self.isffa.setObjectName("isffa")
        self.Seleccion.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 30, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label.setObjectName("label")
        self.ingresar = QtWidgets.QPushButton(self.frame)
        self.ingresar.setGeometry(QtCore.QRect(130, 170, 121, 41))
        self.ingresar.setObjectName("ingresar")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(70, 30, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 261, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(10, 30, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(120, 30, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.conectar = QtWidgets.QPushButton(self.frame_2)
        self.conectar.setGeometry(QtCore.QRect(160, 70, 91, 31))
        self.conectar.setObjectName("conectar")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 81, 29))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 41, 29))
        self.label_3.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.label_3.setObjectName("label_3")
        self.conectando = QtWidgets.QProgressBar(self.frame_2)
        self.conectando.setGeometry(QtCore.QRect(10, 70, 141, 23))
        self.conectando.setProperty("value", 0)
        self.conectando.setObjectName("conectando")
        AnalisysCheck.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnalisysCheck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.menuPrincipal = QtWidgets.QMenu(self.menubar)
        self.menuPrincipal.setObjectName("menuPrincipal")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        AnalisysCheck.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnalisysCheck)
        self.statusbar.setObjectName("statusbar")
        AnalisysCheck.setStatusBar(self.statusbar)
        self.actionSelecci_n = QtWidgets.QAction(AnalisysCheck)
        self.actionSelecci_n.setObjectName("actionSelecci_n")
        self.actionSalirr = QtWidgets.QAction(AnalisysCheck)
        self.actionSalirr.setObjectName("actionSalirr")
        self.actionDocumentaci_n = QtWidgets.QAction(AnalisysCheck)
        self.actionDocumentaci_n.setObjectName("actionDocumentaci_n")
        self.actionAcerca_de_Nosotros = QtWidgets.QAction(AnalisysCheck)
        self.actionAcerca_de_Nosotros.setObjectName("actionAcerca_de_Nosotros")
        self.menuPrincipal.addAction(self.actionSelecci_n)
        self.menuPrincipal.addSeparator()
        self.menuPrincipal.addAction(self.actionSalirr)
        self.menuAyuda.addAction(self.actionDocumentaci_n)
        self.menuAyuda.addAction(self.actionAcerca_de_Nosotros)
        self.menubar.addAction(self.menuPrincipal.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(AnalisysCheck)
        QtCore.QMetaObject.connectSlotsByName(AnalisysCheck)
        AnalisysCheck.setTabOrder(self.Seleccion, self.pichincha)
        AnalisysCheck.setTabOrder(self.pichincha, self.produbanco)
        AnalisysCheck.setTabOrder(self.produbanco, self.pacifico)
        AnalisysCheck.setTabOrder(self.pacifico, self.cfn)
        AnalisysCheck.setTabOrder(self.cfn, self.isffa)
        AnalisysCheck.setTabOrder(self.isffa, self.ingresar)

    def retranslateUi(self, AnalisysCheck):
        _translate = QtCore.QCoreApplication.translate
        AnalisysCheck.setWindowTitle(_translate("AnalisysCheck", "MainWindow"))
        self.pichincha.setText(_translate("AnalisysCheck", "BANCO DEL PICHINCHA"))
        self.produbanco.setText(_translate("AnalisysCheck", "BANCO PRODUBANCO"))
        self.pacifico.setText(_translate("AnalisysCheck", "BANCO DEL PACIFICO"))
        self.cfn.setText(_translate("AnalisysCheck", "CFN"))
        self.isffa.setText(_translate("AnalisysCheck", "ISSFA"))
        self.label.setText(_translate("AnalisysCheck", "Selección del Documento"))
        self.ingresar.setText(_translate("AnalisysCheck", "INGRESAR"))
        self.label_2.setText(_translate("AnalisysCheck", "Conneccion con la Base de Datos"))
        self.conectar.setText(_translate("AnalisysCheck", "Conectar"))
        self.label_4.setText(_translate("AnalisysCheck", "Desconectado"))
        self.label_3.setText(_translate("AnalisysCheck", "Estado:"))
        self.menuPrincipal.setTitle(_translate("AnalisysCheck", "Principal"))
        self.menuAyuda.setTitle(_translate("AnalisysCheck", "Ayuda"))
        self.actionSelecci_n.setText(_translate("AnalisysCheck", "Selección "))
        self.actionSalirr.setText(_translate("AnalisysCheck", "Salir"))
        self.actionDocumentaci_n.setText(_translate("AnalisysCheck", "Documentación"))
        self.actionAcerca_de_Nosotros.setText(_translate("AnalisysCheck", "Acerca de Nosotros"))
