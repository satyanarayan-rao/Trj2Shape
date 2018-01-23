# 

if [ $# -lt 1 ]
then
	echo -e "\n\tUsage: $0 <pdbList>"
	echo -e "\t\t<pdbList>: list of pdbs in a file for which you have to generate the crv files"
	echo -e "\n\texiting ..."
	exit 
fi 

pdbList=$1

for pdb in `cat $pdbList`
do
	name=`basename $pdb .pdb`
	sed  "s:common:$name:g" common.crv > $name.crv 
done
