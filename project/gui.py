import sys
import pandas as pd
import numpy as np
import pyodbc
import urllib.request
import ctypes #GetSystemMetrics
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog, QAction
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from main_window import Ui_AnalisysCheck
from pichincha import Ui_MainWindow
from warning import Ui_Advertencia

# Application Class
class Application(QMainWindow):
   #Método constructor de la clase
   def __init__(self, parent = None):
      #QMainWindow Start
      QMainWindow.__init__(self,parent)
      #Charge MainWindow 
      uic.loadUi("main.ui", self)
      #Title
      self.setWindowTitle("ANALISIS DE PERITAJE")
      # Add variables
      self.file = "None"
      self. count_process = 0
      #Agree new item
      self.ingresar.clicked.connect(self.fn_select_file)
      self.conectar.clicked.connect(self.fn_conectar)
      self.actionSelecci_n.triggered.connect(self.fn_select)
      self.actionSalirr.triggered.connect(self.fn_exit)
      self.actionDocumentaci_n.triggered.connect(self.fn_documentation)
      self.actionAcerca_de_Nosotros.triggered.connect(self.fn_about)

   def fn_select(self):

      self.Application = Application()        #Object Class
      self.Application.show()   
      
   def fn_exit(self):
      self.close()
          
   def fn_documentation(self):
      self.contents = urllib.request.urlopen(
         "https://github.com/FreakJazz/").read()
   # "https://github.com/FreakJazz/PYQT-Interface-gen-access-DataBase"
   def fn_about(self):
      print("aqui va lo del about")
   
   def fn_process_connect(self):
      for i in range(101):
         self.conectando.setValue(i)
         self.label_4.setText("Conectando...")
      self.conectando.setValue(0)

   def fn_conectar(self):
         
      try:
         con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Jazmin Rodriguez/Desktop/Proyectos GitHub/PYQT-Interface-gen-access-DataBase/project/Base_Datos.accdb;'
         conn = pyodbc.connect(con_string)
         self.fn_process_connect()
         self.label_4.setText("Conectado")
         print("Connected To Database")
         self.pichincha.setEnabled(True)
         self.produbanco.setEnabled(True)
         self.pacifico.setEnabled(True)
         self.cfn.setEnabled(True)
         self.isffa.setEnabled(True)
         self.conectar.setEnabled(False)
         self.ingresar.setEnabled(True)

      except pyodbc.Error as e:
         print("Error in Connection", e)
         self.fn_process_connect()
         self.label_4.setText("Error al conectar")

   def fn_select_file(self):
      if self.pichincha.isChecked():
         
         print("entro en pichincha")
         file = "Banco del Pichincha"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()
         
      elif self.produbanco.isChecked():
         print("entro en produbanco")
         file = "Banco Produbanco"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()

      elif self.pacifico.isChecked():
         print("entro en pacifico")
         file = "Banco del Pacifico"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()

      elif self.isffa.isChecked():
         print("entro en isffa")
         file = "ISFFA"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()

      elif self.cfn.isChecked():
         print("entro en cfn")
         file = "CFN"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()

      else:
         self.warning_frame = WarningDialog()
         self.warning_frame.show()
         print("no ha seleccionado nada")

class WarningDialog(QDialog):
    
   def __init__(self, parent = None):
      #QMainWindow Start
      QDialog.__init__(self,parent)
      uic.loadUi("warning.ui", self)
      #Title
      self.setWindowTitle("Advertencia")
      print("entro al dialogo")

class Analisys(QMainWindow):
   def __init__(self, parent ,file):
      #QMainWindow Start
      QMainWindow.__init__(self,parent)
      #Charge MainWindow 
      uic.loadUi("pichincha.ui", self)
      #Title
      self.file = file
      self.type_file.setText(self.file)
      self.setWindowTitle("ANALISIS DE PERITAJE")
      self.examinar.clicked.connect(self.fn_check)
      self.analizar.clicked.connect(self.fn_analize)
      # self.eliminar.clicked.connect(self.fn_delete)
      # self.abrir.clicked.connect(self.fn_open)


   def fn_process_analisys(self):
      for i in range(101):
         self.progress.setValue(i)
      self.progress.setValue(0)

   def fn_check(self):
      self.options = QFileDialog.Options()
      self.fileName, _ = QFileDialog.getOpenFileName(self,"Abrir Archivo", "","Archivos de Excel (*.xlsx);;All Files (*)", options=self.options)
      print(self.fileName)
      self.direccion.setText(str(self.fileName))
      self.archivo.setText(str(self.fileName))
   
   def fn_analize(self):
      self.df = pd.read_excel('users.xlsx', sheet_name = [0,1,2])
      print(self.df)


if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())