import sys
import os
import pandas as pd
import numpy as np
import urllib.request
from datetime import datetime

import ctypes #GetSystemMetrics
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog, QAction
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from main_window import Ui_AnalisysCheck
from pichincha import Ui_Analisys
from warning import Ui_Advertencia
from acerca import Ui_MainWindow

# Application Class
class Application(QMainWindow, Ui_AnalisysCheck):
   #Método constructor de la clase
   def __init__(self, parent = None):
      super().__init__()
      #QMainWindow Start
      QMainWindow.__init__(self)
      # Ui_AnalisysCheck.__init__(self)
      self.setupUi(self)
      
      #Charge MainWindow 
      # uic.loadUi("main.ui", self)
      #Title
      self.setWindowTitle("ANALISIS DE PERITAJE")
      # Add variables
      self.file = "None"
      self. count_process = 0
      #Agree new item
      self.ingresar.clicked.connect(self.fn_select_file)
      # self.conectar.clicked.connect(self.fn_conectar)
      self.actionSelecci_n.triggered.connect(self.fn_select)
      self.actionSalirr.triggered.connect(self.fn_exit)
      self.actionAcerca_de_Nosotros.triggered.connect(self.fn_about)

   def fn_select(self):

      self.Application = Application()        #Object Class
      self.Application.show()   
      
   def fn_exit(self):
      self.close()
          

   def fn_about(self):
      self.analisys_frame = About(None)
      self.analisys_frame.show()
   
   def fn_process_connect(self):
      for i in range(101):
         self.conectando.setValue(i)
         self.label_4.setText("Conectando...")
      self.conectando.setValue(0)

   # def fn_conectar(self):
         
      # try:
      #    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Jazmin Rodriguez/Desktop/Proyectos GitHub/PYQT-Interface-gen-access-DataBase/project/Base_Datos.accdb;'
      #    conn = pyodbc.connect(con_string)
      #    self.fn_process_connect()
      #    self.label_4.setText("Conectado")
      #    print("Connected To Database")
      #    self.pichincha.setEnabled(True)
      #    self.produbanco.setEnabled(True)
      #    self.pacifico.setEnabled(True)
      #    self.cfn.setEnabled(True)
      #    self.isffa.setEnabled(True)
      #    self.conectar.setEnabled(False)
      #    self.ingresar.setEnabled(True)

      # except pyodbc.Error as e:
      #    print("Error in Connection", e)
      #    self.fn_process_connect()
      #    self.label_4.setText("Error al conectar")

   def fn_select_file(self):
      if self.pichincha.isChecked():
         
         print("entro en pichincha")
         file = "Banco del Pichincha"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()
         self.close()
         
      elif self.produbanco.isChecked():
         print("entro en produbanco")
         file = "Banco Produbanco"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()
         self.close()

      elif self.pacifico.isChecked():
         print("entro en pacifico")
         file = "Banco del Pacifico"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()
         self.close()

      elif self.isffa.isChecked():
         print("entro en isffa")
         file = "ISFFA"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()
         self.close()

      elif self.cfn.isChecked():
         print("entro en cfn")
         file = "CFN"
         self.analisys_frame = Analisys(None,file)
         self.analisys_frame.show()
         self.close()
      else:
         self.warning_frame = WarningDialog()
         self.warning_frame.show()
         print("no ha seleccionado nada")

class WarningDialog(QDialog, Ui_Advertencia):
    
   def __init__(self, parent= None):
      #QMainWindow Start
      QDialog.__init__(self,parent)
      super().__init__()
      self.setupUi(self)
      # uic.loadUi("warning.ui", self)
      #Title
      self.setWindowTitle("Advertencia")
      print("entro al dialogo")

class About(QMainWindow, Ui_MainWindow):
   def __init__(self, parent= None):
      #QMainWindow Start
      super().__init__()
      QMainWindow.__init__(self,parent)
      #Charge MainWindow 
      self.setupUi(self)
      # uic.loadUi("acerca.ui", self)
      self.setWindowTitle("ACERCA DE NOSOTROS")
      self.aceptar.clicked.connect(self.fn_ok)

   def fn_ok(self):
      self.close()


class Analisys(QMainWindow, Ui_Analisys):
   def __init__(self, parent ,file):
      #QMainWindow Start
      super().__init__()
      QMainWindow.__init__(self,parent)
      self.setupUi(self)
      #Charge MainWindow 
      # uic.loadUi("pichincha.ui", self)
      #Title
      self.file = file
      self.type_file.setText(self.file)
      self.setWindowTitle("ANALISIS DE PERITAJE")
      self.examinar.clicked.connect(self.fn_check)
      self.analizar.clicked.connect(self.fn_analize)
      self.actionSelecci_n.triggered.connect(self.fn_select)
      self.actionSalir.triggered.connect(self.fn_exit)
      self.actionAcerca_de_Nosotros.triggered.connect(self.fn_about)
      self.abrir_csv.clicked.connect(self.fn_open_csv)
      self.abrir_excel.clicked.connect(self.fn_open_excel)

   def fn_select(self):

      self.Application = Application()        #Object Class
      self.Application.show()
      self.close()
      
   def fn_exit(self):
      self.close()
   
   def fn_about(self):
      self.analisys_frame = About(None)
      self.analisys_frame.show()
          
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

   def process_cfn(self, excel):
      print("entro a cfn")
      return excel

   def process_pichincha(self, excel):
      print("entro a pichincha")
      return excel
      
   def process_produbanco(self, excel):
      print("entro a produbanco")
      return excel
      
   def process_pacifico(self, excel):
      print("entro a pacifico")
      return excel

   def process_isffa(self, excel):
         df_one = excel['1 Datos Ubic ']
         df_dos =  excel['2 Valoración']
         # Documento uno
         self.progress.setValue(32)
         data_1 = df_one['Unnamed: 3']   
         data_1_list = data_1.to_numpy()
         data_2 = df_one['Unnamed: 33']
         data_2_list = data_2.to_numpy()
         data_3 = df_one['Unnamed: 35']
         data_3_list = data_3.to_numpy()
         data_4 = df_one['Unnamed: 55']
         data_4_list = data_4.to_numpy()
         data_5 = df_one['Unnamed: 101']
         data_5_list = data_5.to_numpy()
         data_6 = df_one['Unnamed: 14']
         data_6_list = data_6.to_numpy()
         # Documento dos 
         self.progress.setValue(45)
         data_7 = df_dos['Unnamed: 4']
         data_7_list = data_7.to_numpy()
         data_8 = df_dos['Unnamed: 6']
         data_8_list = data_8.to_numpy()
         data_9 = df_dos['Unnamed: 9']
         data_9_list = data_9.to_numpy()
         self.progress.setValue(60)
         # Valores a extraer
         nua = data_5_list[1]
         fecha = str(data_3_list[11])
         fecha_sep = fecha.split('T')
         fecha = datetime.strptime(str(fecha_sep[0]), '%Y-%m-%d')
         canton = data_1_list[31]
         provincia = data_2_list[29]
         parroquia = data_2_list[31]
         ciudad = data_4_list[29]
         sector = data_4_list[31]
         inmueble = data_6_list[43]
         regimen = data_6_list[45]
         area = data_7_list[22]
         valor = data_9_list[22]
         avaluo = data_8_list[85]
         total = data_8_list[89]
         self.progress.setValue(64)
         df = pd.read_excel('Tabla1.xlsx')
         self.progress.setValue(78)
         lenght = len(df)+1
         df.loc[lenght] = [nua, fecha,sector,parroquia,ciudad,canton, provincia,inmueble, regimen, area, valor, total, avaluo] 
         self.progress.setValue(99)
         return df
   
   def fn_analize(self):
      
      print()
      if self.archivo.text() == '':
         self.warning_frame = WarningDialog()
         self.warning_frame.show()

      else: 
         self.progress.setValue(10)
         file = open(r'Tabla1.xlsx')
         self.progress.setValue(25)
         file.close()
         if self.file == "ISFFA":
            excel = pd.read_excel(str(self.archivo.text()), sheet_name = ['1 Datos Ubic ','2 Valoración'])
            self.df = self.process_isffa(excel)

         elif self.file == "CFN":
            excel = pd.read_excel(str(self.archivo.text()))
            self.df = self.process_cfn(excel)
         
         elif self.file == "Banco del Pichincha":
            excel = pd.read_excel(str(self.archivo.text()))
            self.df = self.process_pichincha(excel)
         
         elif self.file == "Banco del Pacifico":
            excel = pd.read_excel(str(self.archivo.text()))
            self.df = self.process_pacifico(excel)
            
         elif self.file == "Banco Produbanco":
            excel = pd.read_excel(str(self.archivo.text()))
            self.df = self.process_produbanco(excel)

         else: 
            self.df = "No existe esa Tabla"
         self.lineEdit.setText("Tabla1.xlsx")
         self.df.to_excel('Tabla1.xlsx',  index=False)
         self.fileExcel, _ = QFileDialog.getSaveFileName(self.df.to_excel('Tabla1.xlsx',  index=False),"Guardar Archivo", "Tabla1","Archivos de Excel (*.xlsx);;All Files (*)", options=QFileDialog.DontUseNativeDialog)
         self.fileCSV, _ = QFileDialog.getSaveFileName(self.df.to_csv('Tabla1.csv',  index=False),"Guardar Archivo", "Tabla1","Archivos CSV (*.csv);;All Files (*)", options=QFileDialog.DontUseNativeDialog)
         self.final_file = self.lineEdit.setText(str(self.fileExcel))
         # print("file final",self.final_file)
         self.progress.setValue(0)

   def fn_open_csv(self):
      if self.lineEdit.text() == '':
         self.warning_frame = WarningDialog()
         self.warning_frame.show()
      else:
         openfile = str(self.fileCSV).split('.')
         print(str(self.fileCSV)+'.csv')
         os.startfile(openfile[0] +'.csv')
   
   def fn_open_excel(self):
      if self.lineEdit.text() == '':
         self.warning_frame = WarningDialog()
         self.warning_frame.show()
      else:
         openfile = str(self.fileExcel).split('.')
         print(str(self.fileExcel)+'.xlsx')
         os.startfile(openfile[0] +'.xlsx')
         
if __name__ == "__main__": 
   dirname = os.path.dirname(PyQt5.__file__)
   plugin_path = os.path.join(dirname, 'plugins', 'platforms')
   app = QApplication(sys.argv)        #App Inicialization
   _Application = Application()        #Object Class
   _Application.show()                 #Show Window
   app.exec_()                         #Execute Aplication

   #  if __name__ == "__main__":
   #      dirname = os.path.dirname(PyQt5.__file__)
   #  plugin_path = os.path.join(dirname, 'plugins', 'platforms')
   #  QtWidgets.QApplication.addLibraryPath(plugin_path)
   #  app =  QtWidgets.QApplication(sys.argv)
   #  window = MyApp()
   #  window.show()
   #  sys.exit(app.exec_())