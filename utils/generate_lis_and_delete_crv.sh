#!/bin/bash
# Once you generate the crv file (see generateCRVforPDB.sh), you can actually run Curves program on pdbs
# 
if [ $# -lt 1 ]
then
    echo -e "\n\tUsage: $0 <pdbList> <CRV_BIN>"
    echo -e "\t\t<pdbList>: list of pdbs in a file for which you have to generate the lis files"
    echo -e "\t\t<CRV_BIN>: absolute path of Curves bininary (Cur5)"
    echo -e "\n\texiting ..."
    exit 
fi 

pdbList=$1
CRV_BIN=$2

if [ ! -f common.crv ]
then
    cat <<-___HERE
    
    Please be advised that you have to have a file named 'common.crv' with
    appropriate details to run this script. See here https://github.com/satyausc/Trj2Shape#curves-input

    exiting ...
___HERE

    exit 
fi

for pdb in `cat $pdbList`
do
    name=`basename $pdb .pdb`
    crvfile="$name".crv
    sed  "s:common:$name:g" common.crv > $crvfile  && \
    sed -i 's:DA: A:;s:DC: C:;s:DG: G:;s:DT: T:g' $pdb  && \
    $CRV_BIN < $crvfile && rm $crvfile
done
