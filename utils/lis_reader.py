import sys
from autoconvert import autoconvert
import re
from collections import defaultdict
global count
def read_cc_lis_file (filename):
    ccmatrix_D = [[]] 
    ccmatrix_H = [[]]
    ccmatrix_D = ccmatrix_D[1:]
    ccmatrix_H = ccmatrix_H[1:]
    with open (filename, "r") as f:
        for line in f: 
            if line.find("|D| ") != -1:
                #count = 0 
                for skip in range(1,8):
                    next(f)
                v = next(f)
                while v.find(")")!=-1:
                    v = v.strip()
                    if v:
                        vList = [item for item in v.split () if item ]
                        vList = vList[4:]
                        tmparray = []
                        for i, item in enumerate (vList): 
                            tmparray.append((autoconvert(item)))
                        ccmatrix_D.append(tmparray)
                        #count = count + 1
                    v= next(f)
            elif line.find("|H| ") !=-1: 
                for skip in range(1,8):
                    next(f)
                v = next(f);
                while v.find(")")!=-1:
                    v = v.strip()
                    if v:
                        vList = [item for item in v.split () if item ]
                        vList = vList[4:]
                        tmparray = []
                        for i, item in enumerate (vList): 
                            tmparray.append((autoconvert(item)))
                        ccmatrix_H.append(tmparray)
                        #count = count + 1
                    v= next(f)
    
    return  ccmatrix_D, ccmatrix_H

def read_minor (filename):
    sequence = [] 
    MGW_at_diffent_levels_at_different_resid = defaultdict (list)
    with open (filename, "r") as f:
        for line in f: 
            if line.find("|K| ") != -1:
                #count = 0 
                for skip in range(1,8):
                    next(f)
                mgw_at_level = []
                start = True  
                for line in f: 
                    if re.search('[a-zA-Z]', line ): 
                        line_item = [item for item in line.strip().split() ]
                        sequence.append (line_item[0])
                        MGW_at_diffent_levels_at_different_resid[int(line_item[1])].append (line_item[3])
                    else:
                        line_item = [item for item in line.strip().split() ]
                        MGW_at_diffent_levels_at_different_resid[int(line_item[0])].append (line_item[2])
                        

    return sequence, MGW_at_diffent_levels_at_different_resid 
