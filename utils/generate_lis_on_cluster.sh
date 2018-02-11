#PBS -S /bin/sh
#PBS -l mem=2500mb
#PBS -l pmem=200mb
#PBS -l vmem=2000mb
#PBS -l walltime=10:00:00
#PBS -l nodes=1:nx360m5:ppn=4
#PBS -q cmb

cd $dir 
sh generate_lis_and_delete_crv.sh $pdbList $CRV_BIN
