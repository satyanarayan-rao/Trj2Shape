
if [ $# -lt 1 ]
then
    echo -e "\n\tUsage: $0 <./listOfpdbList> <CRV_BIN>" 
    echo -e "\n\t<./listOfpdbList>: seperate pdbList in k partions using split command and put them in a list"
    echo -e "\t\t<CRV_BIN>: absolute path of Curves binary (Cur5)"
    echo -e "\n\texiting ..."
    exit 
fi 

listOfpdbList=$1
CRV_BIN=$2
for i in `cat $listOfpdbList`
do
    dir=`pwd`
    qsub -v "dir=$dir,pdbList=$i,CRV_BIN=${CRV_BIN}"  generate_lis_on_cluster.sh
done 
