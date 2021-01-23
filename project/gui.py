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
      self.count_conn = 0
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
         self.ingresar.setEnabled(True)
         self.pichincha.setEnabled(True)
         self.produbanco.setEnabled(True)
         self.pacifico.setEnabled(True)
         self.cfn.setEnabled(True)
         self.isffa.setEnabled(True)
         self.conectar.setEnabled(False)

      except pyodbc.Error as e:
         print("Error in Connection", e)
         self.fn_process_connect()
         self.label_4.setText("Error al conectar")

         #Eliminar un item
         #self.lenguajes.removeItem(0)

   def fn_select_file(self):
      if self.pichincha.setChecked(True):
         print("entro en pichincha")
         uic.loadUi("pichincha.ui", self)
         #Title
         self.setWindowTitle("ANALISIS DE PERITAJE (BANCO DEL PICHINCHA)")
         
      elif self.produbanco.setChecked(True):
         print("entro en produbanco")

if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())