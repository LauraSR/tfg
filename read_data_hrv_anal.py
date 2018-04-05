#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:57:24 2017

@author: Rebeca
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






def get_folder():
    """
    Functions tha opens a dialog box to select a folder
    """
    dir_path = diropenbox(title="Choose A Subject folder with subfolders andando and sentado ", default = './')
    
    return dir_path


def folder_processing():
    """
    Function that process folder for a given subject in order to read the 
    hr files
    """
    
    dir_path = get_folder()
    os.chdir(dir_path)

    #run over folders
    for folder in glob.iglob('./*'):
        os.chdir(folder)
        
        kind_test = os.path.basename(folder) #indicate which  kind
        
        #get tcx
        tcx_file = os.path.basename(glob.glob('./*.tcx')[0])
        
        #HRV analysis tcx
        pat_tcx_hrv_dict = HRV_analysis_tcx(tcx_file)
        
        np.save(kind_test+'_'+pat_tcx_hrv_dict['id']+'_tcx',pat_tcx_hrv_dict)
        #get txt
        txt_file = os.path.basename(glob.glob('./*.txt')[0])
        
        #HRV analysis bitalino
        pat_bitalino_hrv_dict,ecginf = HRV_analysis_bitalino(txt_file)
        np.save(kind_test+'_'+pat_bitalino_hrv_dict['id']+'_bitalino',pat_bitalino_hrv_dict)
        
        os.chdir("..")
        
        
        return tcx_file,ecginf
    

def get_pat_data():
    
    msg = "Enter subject information"
    title = "Run app"
    fieldNames = ["Pat_Id", "Gender", "Age"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title, fieldNames)
    
    return fieldValues
        
def HRV_analysis_tcx(fname):
    """
    Function that performs HRV analysis on tcx (polar signal)
    """
    
    #get data pat
    
    fields = get_pat_data()
    
    idf = fields[0]
    gender = fields[1]
    age = fields[2]
    
    my_pat = pat(idf,age,gender)
    
    #read example.tcx
    
    t,hr = my_pat.read_txc(fname)
    hr = np.array(hr)
    
    is_bpm = True #boolean falg to convert bpm heart rate signal (from Polar)
    #HRV Analysis
    if is_bpm:
        rr = 60. * 1000/(hr) #rr intervals
        
    labels=['N']*len(rr)
    hrv_anal = HRV()
    prct = 0.2
    ind_not_N_beats=hrv_anal.artifact_ectopic_detection(rr, labels, prct, numBeatsAfterV = 4)
    valid = hrv_anal.is_valid(ind_not_N_beats,perct_valid = 0.2)
    #if every beat is Normal (sum(ind_not_N_beats) == 0), then no correction
    if ind_not_N_beats.sum() > 0:
        rr_corrected = hrv_anal.artifact_ectopic_correction(rr, ind_not_N_beats, method='linear')
    else:
        rr_corrected = rr.copy()
        
    #plt.figure()
    
   # plt.plot(rr_corrected)
    
    #plt.figure()
    #plt.plot(hr)
    hrv_pat = hrv_anal.load_HRV_variables(rr_corrected)
    
    
    r = np.std(rr_corrected)*0.2
    hrv_en = HRV_entropy()
    hrv_pat['sampen'] = hrv_en.SampEn(rr_corrected,m = 2,r=r,kernel = 'Heaviside')
    hrv_pat['id'] = idf
    hrv_pat['gender'] = gender
    hrv_pat['age'] = age    
    return hrv_pat
    
    #pat()
    
def HRV_analysis_bitalino(fname):
    """
    Function that performs HRV analysis on tcx (polar signal)
    """
    
    #get data pat
    
    f = np.loadtxt(fname)
    
    fields = get_pat_data()
    
    idf = fields[0]
    gender = fields[1]
    age = fields[2]
    
    my_pat = pat(idf,age,gender)
    
    
    #read bitalino file
    ecg = f[:,7] #verify the channel with ECG 
    #plt.plot(ecg)
    # get rr from ecg
    fs=1000.;
    ecg_d,t = detrendSpline(ecg,fs,l_w = 1.2)
    ecg_filtered = bandpass_qrs_filter(ecg_d, fs, fc1 = 12,fc2 = 20)
    beat, th, qrs_index= exp_beat_detection(ecg_filtered,fs,Tr = .200,a = .8,b = 0.999)
    r_peak, rr = r_peak_detection(ecg_filtered,ecg,fs,beat,th,qrs_index,Tr = .180)

    t = np.arange(0,len(ecg))/fs
    plt.close('all')
    plt.plot(t,ecg_filtered)
    plt.plot(t,th)
    plt.plot(t[r_peak],ecg_filtered[r_peak],'r*')
    
    labels=['N']*len(rr)
    hrv_anal = HRV()
    prct = 0.2
    ind_not_N_beats=hrv_anal.artifact_ectopic_detection(rr, labels, prct, numBeatsAfterV = 4)
    valid = hrv_anal.is_valid(ind_not_N_beats,perct_valid = 0.2)
    
    #if every beat is Normal (sum(ind_not_N_beats) == 0), then no correction
    if ind_not_N_beats.sum() > 0:
        rr_corrected = hrv_anal.artifact_ectopic_correction(rr, ind_not_N_beats, method='linear')
        rr_corrected = rr.copy()
    else:
        rr_corrected = rr.copy()
        
    #plt.figure()
    
    #plt.plot(rr_corrected)
    
    #plt.figure()
    #plt.plot(rr_corrected)
    hrv_pat = hrv_anal.load_HRV_variables(rr_corrected)
    
    
    r = np.std(rr_corrected)*0.2
    hrv_en = HRV_entropy()
    hrv_pat['sampen'] = hrv_en.SampEn(rr_corrected,m = 2,r=r,kernel = 'Heaviside')
    hrv_pat['id'] = idf
    hrv_pat['gender'] = gender
    hrv_pat['age'] = age

    ecginf = {'ecg':ecg,'r':r_peak}    
    return hrv_pat,ecginf
    
    #pat()
    
    
foo,ecginfo = folder_processing() #Hay que elegir la carpeta de paciente, que contiene las subcarpetas
#andando y sentado
    
"""
f = np.loadtxt("sigs/opensignals_201607181603_2018-01-09_13-14-55.txt")
#f = np.loadtxt("opensignals_Oscar_2017-10-17_12-27-32.txt")

ecg=f[:,6];
#eda=f[:,6];
#marcas=f[:,1];

fs=1000;
ecg_d,t = detrendSpline(ecg,fs,l_w = 1.2)
ecg_filtered = bandpass_qrs_filter(ecg_d, fs, fc1 = 5,fc2 = 15)
beat, th, qrs_index= exp_beat_detection(ecg_filtered,fs,Tr = .180,a = .7,b = 0.999)
r_peak, rr = r_peak_detection(ecg_filtered,ecg,fs,beat,th,qrs_index,Tr = .100)

t=np.arange(0,len(ecg_d))*fs
plt.figure(), plt.plot(t,ecg_d)
plt.figure(), plt.plot(rr)

#t_eda=np.arange(0,len(eda))*fs
#plt.figure(), plt.plot(t_eda,eda)
"""

"""
Analysis with polar
"""

#create a pat


"""
idf = '01'
age = 38
gender = 'M'

my_pat = pat(idf,age,gender)

#read example.tcx

t,hr = my_pat.read_txc('example.tcx')
hr = np.array(hr)

is_bpm = True #boolean falg to convert bpm heart rate signal (from Polar)
#HRV Analysis
if is_bpm:
    rr = 60. * 1000/(hr) #rr intervals
    
labels=['N']*len(rr)
hrv_anal = HRV()
prct = 0.2
ind_not_N_beats=hrv_anal.artifact_ectopic_detection(rr, labels, prct, numBeatsAfterV = 4)
valid = hrv_anal.is_valid(ind_not_N_beats,perct_valid = 0.2)
#if every beat is Normal (sum(ind_not_N_beats) == 0), then no correction
if ind_not_N_beats.sum() > 0:
    rr_corrected = hrv_anal.artifact_ectopic_correction(rr, ind_not_N_beats, method='linear')
else:
    rr_corrected = rr.copy()
    
plt.figure()
plt.plot(rr_corrected)
hrv_pat = hrv_anal.load_HRV_variables(rr_corrected)


r = np.std(rr_corrected)*0.2
hrv_en = HRV_entropy()
hrv_pat['sampen'] = hrv_en.SampEn(rr_corrected,m = 2,r=r,kernel = 'Heaviside')
#hrv_pat['ti']=hrv_en.TimeIrreversibility(rr_corrected,tau=1)
"""



