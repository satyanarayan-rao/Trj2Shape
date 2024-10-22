#!/bin/bash
if [ $# -lt 1 ]
then
    echo -e "\tUsage: sh $0 <pdbList>\n"
    echo -e "\t\t<pdbList>: a file containing pdb names"
    echo -e "\t\tDescription: rename nucleotides in the PDB file, for exmaple, 'DA' to ' A' (Note the space)"
    echo -e "\texiting ..."
    exit 
fi

pdbList=$1

for i in `cat $pdbList`
do 
    sed -i 's:DA: A:;s:DC: C:;s:DG: G:;s:DT: T:g' $i 
    # one can add more commands here to apply changes to each pdb in the list
done 

