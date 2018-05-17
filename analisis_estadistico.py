# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:26:30 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
#from qrs_detector import *
from HRV import HRV
from HRV_Entropy import HRV_entropy
from pat_class import pat
from tcx import *
from easygui import *
import os
import glob
from qrs_detector import *

    
def create_HRV_variables():
    """
    Function that create a np with the HRV variables
    """    
    
    os.chdir('/home/user/Documentos/TFG/tfg/Pacientes_HRV')
    
    #AVNN
    avnn_reposo_bit = []
    avnn_activo_bit = []
    avnn_reposo_polar = []
    avnn_activo_polar = []
    #SDNN
    sdnn_reposo_bit = []
    sdnn_activo_bit = []
    sdnn_reposo_polar = []
    sdnn_activo_polar = []
    #RMSSd
    rmssd_reposo_bit = []
    rmssd_activo_bit = []
    rmssd_reposo_polar = []
    rmssd_activo_polar = []
    #HRVtriag
    hrvtriag_reposo_bit = []
    hrvtriag_activo_bit = []
    hrvtriag_reposo_polar = []
    hrvtriag_activo_polar = []
    #SampEn
    sampen_reposo_bit = []
    sampen_activo_bit = []
    sampen_reposo_polar = []
    sampen_activo_polar = []
        
    # for over folder
    for folder in glob.iglob('./*'):
        os.chdir(folder)

        kind_test = os.path.basename(folder) #indicate which  kind

    #Recorrerme los archivos sacando cada variable 
    
        for files in glob.iglob('./*'):
        
            hrv_dic = np.load(files)
            hrv_dic = hrv_dic.item()
            
            if kind_test == 'bitalino_reposo':
                avnn_reposo_bit.append(hrv_dic['AVNN'])
                sdnn_reposo_bit.append(hrv_dic['SDNN'])
                rmssd_reposo_bit.append(hrv_dic['RMSSD'])
                hrvtriag_reposo_bit.append(hrv_dic['HRVTriangIndex'])
                sampen_reposo_bit.append(hrv_dic['sampen'])
                
            elif kind_test == 'bitalino_activo':
                avnn_activo_bit.append(hrv_dic['AVNN'])
                sdnn_activo_bit.append(hrv_dic['SDNN'])
                rmssd_activo_bit.append(hrv_dic['RMSSD'])
                hrvtriag_activo_bit.append(hrv_dic['HRVTriangIndex'])
                sampen_activo_bit.append(hrv_dic['sampen'])
                
            elif kind_test == 'polar_activo':
                avnn_activo_polar.append(hrv_dic['AVNN'])
                sdnn_activo_polar.append(hrv_dic['SDNN'])
                rmssd_activo_polar.append(hrv_dic['RMSSD'])
                hrvtriag_activo_polar.append(hrv_dic['HRVTriangIndex'])
                sampen_activo_polar.append(hrv_dic['sampen'])
                
            elif kind_test == 'polar_reposo':
                avnn_reposo_polar.append(hrv_dic['AVNN'])
                sdnn_reposo_polar.append(hrv_dic['SDNN'])
                rmssd_reposo_polar.append(hrv_dic['RMSSD'])
                hrvtriag_reposo_polar.append(hrv_dic['HRVTriangIndex'])
                sampen_reposo_polar.append(hrv_dic['sampen'])
                
        os.chdir("..")
    return np.array(sampen_reposo_bit),np.array(sampen_activo_bit),np.array(sampen_reposo_polar),np.array(sampen_activo_polar)
    #np.array(avnn_reposo_bit),np.array(avnn_activo_bit),np.array(avnn_reposo_polar),np.array(avnn_activo_polar),np.array(sdnn_reposo_bit),np.array(sdnn_activo_bit),np.array(sdnn_reposo_polar),np.array(sdnn_activo_polar),np.array(rmssd_reposo_bit),np.array(rmssd_activo_bit),np.array(rmssd_reposo_polar),np.array(rmssd_activo_polar),np.array(hrvtriag_reposo_bit),np.array(hrvtriag_activo_bit),np.array(hrvtriag_reposo_polar),np.array(hrvtriag_activo_polar),np.array(sampen_reposo_bit),np.array(sampen_activo_bit),np.array(sampen_reposo_polar),np.array(sampen_activo_polar)

'''  
"""
AVNN
"""    
avnn_reposo_bit,avnn_activo_bit,avnn_reposo_polar,avnn_activo_polar = create_HRV_variables()


"""
    AVNN ACTIVO
"""  
plt.close('all')
avnn_activo = np.vstack((avnn_activo_bit,avnn_activo_polar))

plt.figure()
plt.title("Boxplot AVNN activo")
plt.boxplot(avnn_activo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/AVNN_boxplot.png')

plt.figure()
plt.suptitle("Histograma AVNN activo", size=14)
plt.subplot(2,1,1)
plt.hist(avnn_activo_bit)
plt.subplot(2,1,2)
plt.hist(avnn_activo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/AVNN_histograma.png')

plt.figure()
plt.title("Grafico de dispersion AVNN activo")
plt.plot(avnn_activo_bit,avnn_activo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/AVNN_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
    AVNN REPOSO
"""  

plt.close('all')
avnn_reposo = np.vstack((avnn_reposo_bit,avnn_reposo_polar))

plt.figure()
plt.title("Boxplot AVNN reposo")
plt.boxplot(avnn_reposo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/AVNN_boxplot.png')

plt.figure()
plt.suptitle("Histograma AVNN reposo", size=14)
plt.subplot(2,1,1)
plt.hist(avnn_reposo_bit)
plt.subplot(2,1,2)
plt.hist(avnn_reposo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/AVNN_histograma.png')

plt.figure()
plt.title("Grafico de dispersion AVNN reposo")
plt.plot(avnn_reposo_bit,avnn_reposo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/AVNN_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
SDNN
"""    
sdnn_reposo_bit,sdnn_activo_bit,sdnn_reposo_polar,sdnn_activo_polar = create_HRV_variables()


"""
    SDNN ACTIVO
"""  
plt.close('all')
sdnn_activo = np.vstack((sdnn_activo_bit,sdnn_activo_polar))

plt.figure()
plt.title("Boxplot SDNN activo")
plt.boxplot(sdnn_activo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/SDNN_boxplot.png')

plt.figure()
plt.suptitle("Histograma SDNN activo", size=14)
plt.subplot(2,1,1)
plt.hist(sdnn_activo_bit)
plt.subplot(2,1,2)
plt.hist(sdnn_activo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/SDNN_histograma.png')

plt.figure()
plt.title("Grafico de dispersion AVNN activo")
plt.plot(sdnn_activo_bit,sdnn_activo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/SDNN_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
    SDNN REPOSO
"""  

plt.close('all')
sdnn_reposo = np.vstack((sdnn_reposo_bit,sdnn_reposo_polar))

plt.figure()
plt.title("Boxplot SDNN reposo")
plt.boxplot(sdnn_reposo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/SDNN_boxplot.png')

plt.figure()
plt.suptitle("Histograma SDNN reposo", size=14)
plt.subplot(2,1,1)
plt.hist(sdnn_reposo_bit)
plt.subplot(2,1,2)
plt.hist(sdnn_reposo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/SDNN_histograma.png')

plt.figure()
plt.title("Grafico de dispersion SDNN reposo")
plt.plot(sdnn_reposo_bit,sdnn_reposo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/SDNN_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
RMSSD
"""    
rmssd_reposo_bit,rmssd_activo_bit,rmssd_reposo_polar,rmssd_activo_polar = create_HRV_variables()


"""
    RMSSD ACTIVO
"""  
plt.close('all')
rmssd_activo = np.vstack((rmssd_activo_bit,rmssd_activo_polar))

plt.figure()
plt.title("Boxplot RMSSD activo")
plt.boxplot(rmssd_activo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/RMSSD_boxplot.png')

plt.figure()
plt.suptitle("Histograma RMSSD activo", size=14)
plt.subplot(2,1,1)
plt.hist(rmssd_activo_bit)
plt.subplot(2,1,2)
plt.hist(rmssd_activo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/RMSSD_histograma.png')

plt.figure()
plt.title("Grafico de dispersion RMSSD activo")
plt.plot(rmssd_activo_bit,rmssd_activo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/RMSSD_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
    RMSSD REPOSO
"""  

plt.close('all')
rmssd_reposo = np.vstack((rmssd_reposo_bit,rmssd_reposo_polar))

plt.figure()
plt.title("Boxplot RMSSD reposo")
plt.boxplot(rmssd_reposo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/RMSSD_boxplot.png')

plt.figure()
plt.suptitle("Histograma RMSSD reposo", size=14)
plt.subplot(2,1,1)
plt.hist(rmssd_reposo_bit)
plt.subplot(2,1,2)
plt.hist(rmssd_reposo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/RMSSD_histograma.png')

plt.figure()
plt.title("Grafico de dispersion RMSSD reposo")
plt.plot(rmssd_reposo_bit,rmssd_reposo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/RMSSD_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])



"""
HRVTriangIndex
"""    
hrvtriag_reposo_bit,hrvtriag_activo_bit,hrvtriag_reposo_polar,hrvtriag_activo_polar = create_HRV_variables()


"""
    HRVTriangIndex ACTIVO
"""  
plt.close('all')
hrvtriag_activo = np.vstack((hrvtriag_activo_bit,hrvtriag_activo_polar))

plt.figure()
plt.title("Boxplot HRVTriangIndex activo")
plt.boxplot(hrvtriag_activo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/HRVTriangIndex_boxplot.png')

plt.figure()
plt.suptitle("Histograma HRVTriangIndex activo", size=14)
plt.subplot(2,1,1)
plt.hist(hrvtriag_activo_bit)
plt.subplot(2,1,2)
plt.hist(hrvtriag_activo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/HRVTriangIndex_histograma.png')

plt.figure()
plt.title("Grafico de dispersion HRVTriangIndex activo")
plt.plot(hrvtriag_activo_bit,hrvtriag_activo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/HRVTriangIndex_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
    HRVTriangIndex REPOSO
"""  

plt.close('all')
hrvtriag_reposo = np.vstack((hrvtriag_reposo_bit,hrvtriag_reposo_polar))

plt.figure()
plt.title("Boxplot HRVTriangIndex reposo")
plt.boxplot(hrvtriag_reposo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/HRVTriangIndex_boxplot.png')

plt.figure()
plt.suptitle("Histograma HRVTriangIndex reposo", size=14)
plt.subplot(2,1,1)
plt.hist(hrvtriag_reposo_bit)
plt.subplot(2,1,2)
plt.hist(hrvtriag_reposo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/HRVTriangIndex_histograma.png')

plt.figure()
plt.title("Grafico de dispersion HRVTriangIndex reposo")
plt.plot(hrvtriag_reposo_bit,hrvtriag_reposo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/HRVTriangIndex_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])

'''

"""
sampen
"""    
sampen_reposo_bit,sampen_activo_bit,sampen_reposo_polar,sampen_activo_polar = create_HRV_variables()


"""
    sampen ACTIVO
"""  
plt.close('all')
sampen_activo = np.vstack((sampen_activo_bit,sampen_activo_polar))

plt.figure()
plt.title("Boxplot sampen activo")
plt.boxplot(sampen_activo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/sampen_boxplot.png')

plt.figure()
plt.suptitle("Histograma sampen activo", size=14)
plt.subplot(2,1,1)
plt.hist(sampen_activo_bit)
plt.subplot(2,1,2)
plt.hist(sampen_activo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/sampen_histograma.png')

plt.figure()
plt.title("Grafico de dispersion sampen activo")
plt.plot(sampen_activo_bit,sampen_activo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Activo/sampen_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])


"""
    sampen REPOSO
"""  

plt.close('all')
sampen_reposo = np.vstack((sampen_reposo_bit,sampen_reposo_polar))

plt.figure()
plt.title("Boxplot sampen reposo")
plt.boxplot(sampen_reposo.T)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/sampen_boxplot.png')

plt.figure()
plt.suptitle("Histograma sampen reposo", size=14)
plt.subplot(2,1,1)
plt.hist(sampen_reposo_bit)
plt.subplot(2,1,2)
plt.hist(sampen_reposo_polar)
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/sampen_histograma.png')

plt.figure()
plt.title("Grafico de dispersion sampen reposo")
plt.plot(sampen_reposo_bit,sampen_reposo_polar,'o')
plt.savefig('/home/user/Documentos/TFG/tfg/Graficas/Reposo/sampen_scatterplot.png')

ax = plt.axis()
ax_min = np.min(ax)
ax_max = np.max(ax)
plt.axis([ax_min,ax_max,ax_min,ax_max])
