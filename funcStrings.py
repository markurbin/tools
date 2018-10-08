# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 14:17:51 2017

@author: murbin
"""

def get_extension(fName):
    return fName.split('.')[-1].lower()

def get_name(fName):
    ext = get_extension(fName)
    extLen = len(ext)
    return(fName[:-extLen - 1])
    