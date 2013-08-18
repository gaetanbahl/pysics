#-------------------------------------------------------------------------------
# Name:        funcs.pys
# Purpose:     stocker des fonctions moches autre part que dans le code joli
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


def obool(booleen):
	
	return not booleen

def degtorad(deg):
	return 3.1415 * deg / 180

def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newseq

def isin(a,liste):
	
	for i in liste:
		if a == i:
			return True
	return False
