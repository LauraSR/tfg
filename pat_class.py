# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:02:46 2016

@author: Rebeca Goya Esteban
         Óscar Barquero Pérez
         Laura Sanz Ruano
"""
from tcx import parsetcx, get_hr_time


class pat():
    """
    Class that model a patient.
    """

    def __init__(self,ident,edad,sexo):
        self.id = ident
        self.age = edad
        self.sex = sexo
        self.record = {'date':None}
        self.tcx_recording =  [] #attribute with points
        
    def read_txc(self,tcx_fname):
        """
        Function that reads tcx file
        """
        #parsetcx reciev an xlm istream
        
        istream = open(tcx_fname,'r')
        #ostream = sys.stdout

        # read xml contents
        xml = istream.read()
    
        #calling parsetcx, which returns points
        self.tcx_recording = parsetcx(xml)
        
        t,hr = get_hr_time(self.tcx_recording)

        #TO_DO How to manage the information of this recording:
        # (1) save into the pat
        # (2) just return t and hr

        return t, hr