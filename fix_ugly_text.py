# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:16:32 2017

@author: Rafael Chunga Quispe


"""

import goslate

# read text
fh = open("Uglytext", "r")
uglyText = fh.read()
fh.close()

# fix text
fixText1 = uglyText.replace("   ","")
fixText2 = fixText1.replace("\n"," ")

# consult google
gs = goslate.Goslate()
fixText3 = gs.translate(fixText2, 'es')

# write traduction
fh = open("FixedText", "w")
fh.write(fixText2)
fh.write("\n---------------Traduccion----------------\n")
fh.write(fixText3)
fh.close()
