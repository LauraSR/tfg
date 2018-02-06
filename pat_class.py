# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:02:46 2016

@author: Rebeca Goya Esteban
         Óscar Barquero Pérez
         Luaura Ruano
"""

class pat(Object):
    """
    Class that model a patient.
    """

    def __init__(self,ident):
       
        self.id = ident
		self.age
		self.sex
		self.record = {'date':}
		self.tcx_recording =  #attribute with points

	
	def read_txc(self,tcx_fname):
		"""
		Function that reads tcx file
		"""
		tcx_r = tcx_reader()

		self.txc_recording = tcx_r.parsetcx(xml)

