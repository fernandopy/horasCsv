'''
Created on 04/10/2016

@author: fer
'''
from dateutil.parser import parse
import time
from datetime import datetime
import pandas as pd

formato1 = "%Y-%m-%d %H:%M:%S.%f"  # Asigna un formato de la fecha
valores = pd.read_csv("04-12-15_nuevo.csv")#lee el archivo 
arr = []
for i in range(0,24):
    cad = "2015-12-04 "+str(i)+":00:00.100000"#se genera el time stamp entre 00 y las 23 horas
    cadena1 = datetime.strptime(cad,formato1)
    aux = str(int(time.mktime(cadena1.timetuple()))) + str((cadena1.microsecond / 1000))
    arr.append(int(aux))##losvalores enteros se agregan a un arreglo

for i in range(0,len(arr)):#se recorre el arreglo de las horas en formato timestamp para hacer el filtrado de el csv
    if i == 23:#cuando es la hora 23 se hace el filtrdo apartir del 23 hasta las 00 horas del día siguiente 1449295200100
        dat_filter = valores[(valores['pubmillis'] >= arr[i]) & (valores['pubmillis'] < 1449295200100)]
        nombre_arch = "04-12-15_"+str(i)+".csv"
        dat_filter.to_csv(nombre_arch)#"""
    else:    
        dat_filter = valores[(valores['pubmillis'] >= arr[i]) & (valores['pubmillis'] < arr[i+1])]#se hace el filtrado sobre el dataframe
        nombre_arch = "04-12-15_"+str(i)+"-"+str(i+1)+".csv" #es el nombre del archivo 
        dat_filter.to_csv(nombre_arch)#se genera el archivo 

