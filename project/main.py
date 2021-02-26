import sys
import os
import pandas as pd
from datetime import datetime
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
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
      #Title
      self.file = file
      self.type_file.setText(self.file)
      self.setWindowTitle("ANALISIS DE PERITAJE")
      self.examinar.clicked.connect(self.fn_check)
      self.examinar_2.clicked.connect(self.fn_check_2)
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
      self.fileNames, _ = QFileDialog.getOpenFileNames(self,"Abrir Archivo", "","Cargar Tabla de Excel (*.xlsx);;All Files (*)", options=self.options)
      if self.fileNames:
         self.lenght = len(self.fileNames)-1
         while self.lenght >= 0:
            self.listWidget.addItem(self.fileNames[self.lenght])
            self.lenght -=1
   
   def fn_check_2(self):
      self.options = QFileDialog.Options()
      self.file_db, _ = QFileDialog.getOpenFileName(self,"Abrir Archivo", "","Cargar Tabla de Excel (*.xlsx);;All Files (*)", options=self.options)
      self.archivo.setText(str(self.file_db))

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
      try:
         df_one = excel['1 Datos Ubic ']
         df_dos =  excel['2 Valoración']
         print(df_one, df_dos)
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
         self.progress.setValue(78)
         res_list = [nua, fecha,sector,parroquia,ciudad,canton, provincia,inmueble, regimen, area, valor, total, avaluo]
         self.progress.setValue(99)
         return res_list
      except ValueError:
         self.warning_frame = WarningDialog()
         self.warning_frame.show()
          
   
   def fn_analize(self):
      
      print()
      if self.archivo.text() == '':
         self.warning_frame = WarningDialog()
         self.warning_frame.show()

      elif self.listWidget.count() == 0:
         self.warning_frame = WarningDialog()
         self.warning_frame.show()
      else: 
         self.progress.setValue(10)
         self.progress.setValue(25)
         if self.file == "ISFFA":
            try:
               if self.fileNames:
                  self.lenght = len(self.fileNames)-1
                  self.df = pd.read_excel(str(self.file_db))
                  while self.lenght >= 0:
                     excel = pd.read_excel(str(self.fileNames[self.lenght]), sheet_name = ['1 Datos Ubic ','2 Valoración'])
                     self.res_list = self.process_isffa(excel)
                     lenght = len(self.df)+1
                     self.df.loc[lenght] = self.res_list
                     self.lenght -=1
                  
            except KeyError:
               self.warning_frame = WarningDialog()
               self.warning_frame.show()

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
         try:
            self.df.to_excel('Tabla1.xlsx',  index=False)
            self.fileExcel, _ = QFileDialog.getSaveFileName(self.df.to_excel('Tabla1.xlsx',  index=False),"Guardar Archivo", "Tabla1","Archivos de Excel (*.xlsx);;All Files (*)", options=QFileDialog.DontUseNativeDialog)
            self.fileCSV, _ = QFileDialog.getSaveFileName(self.df.to_csv('Tabla1.csv',  index=False),"Guardar Archivo", "Tabla1","Archivos CSV (*.csv);;All Files (*)", options=QFileDialog.DontUseNativeDialog)
            self.final_file = self.lineEdit.setText(str(self.fileExcel))
         except AttributeError as e:
            # self.listWidget.count() = 0
            self.archivo.setText('')
            print(e)
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
