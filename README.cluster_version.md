# Running Trj2Shape on cluster

Often MD simulations result in big data output, and using high-performace
computing (HPC) is a general trend in this field. We have made efforts to scale
`Trj2Shape` to run on clusters. This documentation will walk you through all
the steps involved to run it on cluster.


## Generating snapshots from MD trajectories

Please use the following script to generate snapshots from the `.xtc` file.

Few important notes: 

- Please `cd` to the directory where you have relevant files (`.xtc`,`.tpr`)
- The hpc environment may differ (depending on what cluster manager is running)
- **cd** to the directory where you want to save the snapshots inside the
  script. Please customize to your needs
- It is advisable to copy relevant scripts to the data directory. 

```bash
$ cd ${Trj2Shape}/data # change to the data directory 
$ cp ${Trj2Shape}/scripts/snapshot_generator_on_cluster.sh .
$ ls *.xtc *.tpr
3n4m_prod01-12_every10ps_tr1.xtc  3n4m_prod05.tpr

$ qsub -v "selection=12,tpr=3n4m_prod05.tpr,xtc=3n4m_prod01-12_every10ps_tr1.xtc,skip=0" snapshot_generator_on_cluster.sh 
```

## Generating LIS files for snapshots

We run Curves to get `lis` file for each snapshot. To know the preprocessing
and related concepts, please see [here](./Curves.processing.md).

```{bash}
$ cd ${Trj2Shape}/data # change to the data directory 
$ cp ${Trj2Shape}/utils/run_lis_generation_in_batches.sh . # copy relevant scripts to the data directory 
$ cp ${Trj2Shape}/utils/generate_lis_on_cluster.sh .
$ cp ${Trj2Shape}/utils/generate_lis_and_delete_crv.sh . 
$ ls -v *.pdb > pdbList
$ split -l10000 pdbList pdbList -d 
$ ls -v pdbList?* > listOfpdbList
$ sh run_lis_generation_in_batches.sh listOfpdbList /panfs/cmb-panasas2/satyanar/workplace/tools/Curve/Cur5

```
For 30K snapshots with DNA of 20bp length, it took around **30 minutes** to get all the snapshots. 

