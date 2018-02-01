
if [ $# -lt 1 ]
then
    echo -e "\n\tUsage: $0 <./listOfpdbList>" 
    echo -e "\n\t<./listOfpdbList>: seperate pdbList in k partions using split command and put them in a list"
    echo -e "\n\texiting ..."
    exit 
fi 

for i in `cat $1`
do
    dir=`pwd`
    qsub -v "dir=$dir,pdbList=$i" generateLIS_using_cluster.sh 
done 
