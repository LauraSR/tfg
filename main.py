#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:40:47 2018

#this script allows to create a patient a read a tcx associated with this patient

@author: obarquero
"""

#imports

from pat_class import pat

from tcx import *


#create a pat

idf = '01'
age = 38
gender = 'M'

my_pat = pat(idf,age,gender)


#read example.tcx

t,hr = my_pat.read_txc('example.tcx')
