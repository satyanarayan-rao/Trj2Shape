#!/bin/bash
#PBS -l nodes=4:ppn=16:gpus=1
#PBS -l walltime=24:00:00
#PBS -N snapshot-gen 
#PBS -j oe
##PBS -q cmb

source /usr/usc/intel/default/setup.sh
source /usr/usc/openmpi/1.8.7/setup.sh.intel
source /usr/usc/gromacs/5.0.4/cpu/setup.sh

cd /home/rcf-40/satyanar/panfs/workplace/projects/Trj2Shape/data
#sh snapshot_generator.sh $selection $dir $tpr $xtc $skip 
command="trjconv_mpi -s $tpr -sep -f $xtc -skip $skip"
echo $command > sample.cmd
if [ $skip -ne 0 ]
then
    echo $selection | trjconv_mpi -s $tpr -sep -f $xtc -o .pdb -skip $skip
else
    echo $selection | trjconv_mpi -s $tpr -sep -f $xtc -o .pdb 
fi
