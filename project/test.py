import csv
import pandas as pd
import numpy as np
import sys
import pyodbc

class aplication():
    
    def __init__(self, name):
        self.name = name
        self.read_excel()

    def read_excel (self):
        file = open(r'Tabla1.xlsx')
        file.close()
        excel = pd.read_excel('issf.xlsx', sheet_name = ['1 Datos Ubic ','2 Valoración'])
        print(excel)
        df_one = excel['1 Datos Ubic ']
        # df_one.dropna(inplace=True)
        df_dos =  excel['2 Valoración']
        print("shape",df_one.shape,df_dos.shape)
        # df_one[~df_one.isin([np.nan, np.inf, -np.inf]).any(1)]
        # Documento uno
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
        print( data_1_list, data_2_list, data_3_list,data_4_list, data_5_list)
        # Valores a extraer
        nua = data_5_list[1]
        fecha = data_3_list[11]
        canton = data_1_list[31]
        provincia = data_2_list[29]
        parroquia = data_2_list[31]
        ciudad = data_4_list[29]
        sector = data_4_list[31]
        inmueble = data_6_list[43]
        regimen = data_6_list[45]

        # Documento dos 
        data_7 = df_dos['Unnamed: 4']
        data_7_list = data_7.to_numpy()
        data_8 = df_dos['Unnamed: 6']
        data_8_list = data_8.to_numpy()
        data_9 = df_dos['Unnamed: 9']
        data_9_list = data_9.to_numpy()

        area = data_7_list[22]
        valor = data_9_list[22]
        avaluo = data_8_list[85]
        total = data_8_list[89]
        df = pd.read_excel('Tabla1.xlsx')
        lenght = len(df)+1
        lista = []
        for x in range(lenght):
            lista.append(x)
        print(df)
        row_to_add = pd.DataFrame({
                            'NUA':[nua], 
                            'FECHA':[fecha],
                            'SECTOR':[sector],
                            'PARROQUIA':[parroquia], 
                            'CIUDAD':[ciudad],
                            'CANTON':[canton],
                            'PROVINCIA':[provincia], 
                            'INMUEBLE':[inmueble],
                            'REGIMEN DE PROPIEDAD':[regimen],
                            'AREA TERRENO':[area],
                            'VALOR UNITARIO x M2':[valor],
                            'VALOR DE LA REALIZACION':[total],
                            'AVALUO TOTAL':[avaluo],
                        }) 
        df.append(row_to_add)
        df.loc[lenght] = [lenght,lenght,nua, fecha,sector,parroquia,ciudad,canton, provincia,inmueble, regimen, area, valor, total, avaluo] 
        df.to_excel('Tabla1.xlsx')
        df.to_csv('Tabla1.csv', index=True,sep=',')
        print(nua, fecha,sector,parroquia,ciudad,canton, provincia,inmueble, regimen, area, valor, avaluo, total)
        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Jazmin Rodriguez/Desktop/Proyectos GitHub/PYQT-Interface-gen-access-DataBase/project/Base_Datos.accdb;'
            conn = pyodbc.connect(con_string)
            print("Connected To Database")
            cursor = conn.cursor()
            cursor.execute('select * from Tabla1')
            for row in cursor.fetchall():
                print (row)
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Jazmin Rodriguez/Desktop/Proyectos GitHub/PYQT-Interface-gen-access-DataBase/project/Base_Datos.accdb;'
            conn = pyodbc.connect(con_string)
            print("Connected To Database")
            # cursor.execute('''INSERT INTO Tabla1 (NUA, FECHA, SECTOR) 
            # VALUES(nua, fecha, sector)''')
            cursor.execute('''
            INSERT INTO Tabla1 (NUA, FECHA, SECTOR, PARROQUIA, CIUDAD, CANTON,PROVINCIA, INMUEBLE, REGIMEN DE PROPIEDAD, AREA TERRENO, VALOR UNITARIO x M2, VALOR DE LA REALIZACION,AVALUO TOTAL,) 
            VALUES(nua, fecha, sector, parroquia, ciudad, canton,provincia, inmueble, regimen, area, valor, total, avaluo)
            ''')
            conn.commit()
            conn.close()
            cursor.close()
        except pyodbc.Error as e:
            print("Error in Connection", e)
        # finally/:
            
        
        df_one.to_csv('one.csv', index=True,sep=',')
        df_dos.to_csv('dos.csv', index=True,sep=',')





if __name__ == "__main__": 

    app = aplication("Jazz")