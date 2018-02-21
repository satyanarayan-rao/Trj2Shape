
import os
import sys 
import pandas as pd
import numpy as np 
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--in", dest="input_file", 
                  help="file containing shape feature values for each MD snapshots",
                  metavar="FILE")

parser.add_option("-o", "--out", dest="output_file", 
                  help="to store the average shape feature value profile",
                  metavar="FILE")

(options, args) = parser.parse_args() 
if len (sys.argv) == 1: 
    parser.print_help() 
    exit (1)

input_file = options.input_file
output_file = options.output_file 

CurvesShapeData = pd.read_csv(input_file, 
                              header = None,
                              sep = '\s+',
                              comment = '#') 

rows, cols = CurvesShapeData.shape 
Occurances = CurvesShapeData.count () 
Missings = rows - Occurances 
Mean = CurvesShapeData.mean ()
Std = CurvesShapeData.std () 
result = pd.concat ([Mean, Std, Occurances, Missings], axis = 1 ) 
result.columns = ['Mean', 'Std', 'Occurances', 'Missings']
result.drop(result.head(1).index, inplace=True)

ResId = list (range(1,cols)) 
result['ResId'] = ResId  

column_list = result.columns.tolist() 
column_list = column_list [-1:] + column_list [:-1]
result = result[column_list]
result.to_csv(output_file, 
              sep = '\t', 
              index=False, 
              na_rep='NaN', 
              float_format="%.3f")  
# 1st column contains names of `lis` flies

