import sys 
from lis_reader import read_cc_lis_file
from lis_reader import read_minor
from collections import defaultdict
from math import sqrt
from optparse import OptionParser
from isfloat import isfloat
import math

parser = OptionParser()
parser.add_option("-i", "--in", dest="filename",
                  help="input file containing the list of nonartifact files with start and end position:" \
                       "so every line will have three columns, <filename > <start pos> < end pos> : <start pos> position 5'"\
                       "side you want start considering to use in building querytable, <end pos> position from last (3') you"\
                       "want to stop considering to use in query table. Generally start and end pos values are 4 and 4, because"\
                       "we run MC simulations with CGCG flanks (4bps), and we do not include these in counting.(for example nonartifact.txt) ", metavar="FILE")
#parser.add_option("-o", "--offset", dest="offset",
#                 help="Number of nucleotides to be ignored from both ends of a sequence", metavar="NUM")
parser.add_option("-w", "--write", dest="outfile",
                  help="output file name for querytable", metavar="FILE")


(options, args) = parser.parse_args()
if len(sys.argv) == 1:
	parser.print_help()
	exit(1)

filename = options.filename
output_file = options.outfile

minor_file_list = []
major_file_list = []
cc_file_list = []
seq_file_list = []
count_lines = 0 
start_pos_list= list ()
stop_pos_list = list ()

MGW_out = open (output_file+".MGW", "w")
ProT_out =open (output_file+".ProT", "w") 
Roll_out =open (output_file+".Roll", "w") 
HelT_out =open (output_file+".HelT", "w") 
artifact = open (output_file + ".artifact", "w" ) 


with open (filename, "r") as f:
    for line in f: 
        line = line.strip()
        file_and_offsets = [ item for item in line.split()]
        minor_file_name = file_and_offsets[0]
        start_pos_list.append(int(file_and_offsets[1]))
        stop_pos_list.append(int(file_and_offsets[2]))
        basename = minor_file_name[:-4]
        cc_file_name = basename + ".lis"
        minor_file_list.append(cc_file_name)
        cc_file_list.append(cc_file_name)
        count_lines = count_lines + 1 

count = 0 

for  minor_file in minor_file_list:
    is_artifact = False 
    sequence, ccmatrix_K = read_minor (minor_file)
    MGW_profile = []
    for i in ccmatrix_K.keys():
        if i > 1 and len (ccmatrix_K[i-1]) > 1  and len (ccmatrix_K[i]) > 1 :  
            if isfloat (ccmatrix_K[i-1][-1]) and isfloat (ccmatrix_K[i][0]) and isfloat(ccmatrix_K[i][1]): 
                Ave_MGW = ( float (ccmatrix_K[i-1][-1]) + float (ccmatrix_K[i][0]) + float (ccmatrix_K[i][1]) ) /3
                if Ave_MGW > 12 or Ave_MGW < 1.5: 
                    #MGW_profile.append ('-1')
                    MGW_profile.append ('NA')
                    is_artifact = True

                else: 
                    MGW_profile.append (str (round ( Ave_MGW,3))) 
            else: 
                #MGW_profile.append ('-1')
                MGW_profile.append ('NA')

        else:
            #MGW_profile.append ('-1')
            MGW_profile.append ('NA')
    out = "\t".join (MGW_profile)
    MGW_out.write (minor_file+"\t" + out +"\n")
    if is_artifact == True: 
        artifact.write (minor_file+"\n")

count = 0 


for cc_file in cc_file_list:
    
    ccmatrix_D = [[]]
    ccmatrix_H = [[]]
    ccmatrix_D, ccmatrix_H = read_cc_lis_file(cc_file)	
    rows_D = len (ccmatrix_D)
    rows_H = len (ccmatrix_H) 
    Roll_at_bp_steps = ""
    HelT_at_bp_steps = ""
    ProT_at_bp_steps = ""
    for idx in range (0,rows_H): 
    	Roll_at_bp_steps += str (ccmatrix_H[idx][4]) + "\t"
    	HelT_at_bp_steps += str (ccmatrix_H[idx][5]) + "\t"
    for idx in range (0,rows_D):
    	ProT_at_bp_steps += str (ccmatrix_D[idx][4]) + "\t"
    Roll_at_bp_steps.strip ()
    HelT_at_bp_steps.strip ()
    ProT_at_bp_steps.strip ()
    
    Roll_out.write (cc_file+"\t" + Roll_at_bp_steps +"\n")
    HelT_out.write (cc_file+"\t" + HelT_at_bp_steps +"\n")
    ProT_out.write (cc_file+"\t" + ProT_at_bp_steps +"\n")
