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
      #Agree new item
      self.ingresar.clicked.connect(self.select_file)
   #   self.btn_process.clicked.connect(self.processfile)
      # try:
      #    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\parwizforogh\Documents\pydb.accdb;'
      #    conn = pyodbc.connect(con_string)
      #    print("Connected To Database")

      # except pyodbc.Error as e:
      #    print("Error in Connection", e)
      #    #Eliminar un item
      #    #self.lenguajes.removeItem(0)
   def select_file(self):
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