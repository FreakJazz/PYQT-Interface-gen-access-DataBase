import csv          
import pandas as pd
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from main_window import Ui_AnalisysCheck
from pichincha import Ui_MainWindow
from warning import Ui_Advertencia
import ctypes #GetSystemMetrics
import pyodbc

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
   
   def fn_process_connect(self):
      for i in range(101):
         self.conectando.setValue(i)
         self.label_4.setText("Conectando...")
      self.conectando.setValue(0)

   def fn_process_analisys(self):
      for i in range(101):
         self.progress.setValue(i)
         self.progress.setValue(0)

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
         self.file = "Pichincha"
         uic.loadUi("pichincha.ui", self)
         #Title
         self.setWindowTitle("ANALISIS DE PERITAJE")
      elif self.produbanco.isChecked():
         print("entro en produbanco")
         self.file = "Produbanco"
         uic.loadUi("pichincha.ui", self)
         #Title
         self.setWindowTitle("ANALISIS DE PERITAJE")
      elif self.pacifico.isChecked():
         print("entro en pacifico")
         self.file = "Pacifico"
         uic.loadUi("pichincha.ui", self)
         #Title
         self.setWindowTitle("ANALISIS DE PERITAJE")
      elif self.isffa.isChecked():
         print("entro en isffa")
         self.file = "Isffa"
         uic.loadUi("pichincha.ui", self)
         #Title
         self.setWindowTitle("ANALISIS DE PERITAJE")
      elif self.cfn.isChecked():
         print("entro en cfn")
         self.file = "CFN"
         uic.loadUi("pichincha.ui", self)
         #Title
         self.setWindowTitle("ANALISIS DE PERITAJE")
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

if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())