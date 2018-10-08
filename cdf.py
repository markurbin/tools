# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 11:44:41 2014

@author: urbinmar
"""
#**************************************************************
#
#  cdf.py
#  Python 2.7
#
#  Version 1.0
#
#  January 2014
#  Mark Urbin
#
#  Check a directory & create it if it doesn't exist 
#
#**************************************************************

import os
import os.path

def check_dir(path):
    'Check if directory exists, if not create it.'

    #print 'path = ', path
    if not os.path.isdir(path):
        os.makedirs(path)
    if os.path.isdir(path):
        return True
    else:
        return False
#end of check_dir()