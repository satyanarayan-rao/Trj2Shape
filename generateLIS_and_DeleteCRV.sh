# Once you generate the crv file (see generateCRVforPDB.sh), you can actually run Curves program on pdbs
# 
if [ $# -lt 1 ]
then
    echo -e "\n\tUsage: $0 <pdbList>"
    echo -e "\t\t<pdbList>: list of pdbs in a file for which you have to generate the lis files"
    echo -e "\n\texiting ..."
    exit 
fi 

pdbList=$1
CRV_BIN="`pwd`/Cruve/Cur5"
for pdb in `cat $pdbList`
do
    name=`basename $pdb .pdb`
    crvfile="$name".crv
    sed  "s:common:$name:g" common.crv > $crvfile  && \
    sed -i 's:DA: A:;s:DC: C:;s:DG: G:;s:DT: T:g' $pdb  && \
    $CRV_BIN < $crvfile && rm $crvfile
done
