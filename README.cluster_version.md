# Running Trj2Shape on cluster

Often MD simulations result in big data output, and using high-performace
computing (HPC) is a general trend in this field. We have made efforts to scale
`Trj2Shape` to run on clusters. This documentation will walk you through all
the steps involved to run it on cluster.


## MD trajectories

Please use the following script to generate snapshots from the `.xtc` file.

Few important notes: 

    - Please `cd` to the directory where you have relevant files (`.xtc`,
      `.tpr`)
    - The hpc environment may differ (depending on what cluster manager is
      running)
    - **cd** to the directory where you want to save the snapshots inside the script. Please
      customize to your needs
    - It is advisable to copy relevant scripts to the data directory. 

```bash
$ cd data
$ cp ../scripts/snapshot_generator_on_cluster.sh . 
$ ls *.xtc *.tpr
3n4m_prod01-12_every10ps_tr1.xtc  3n4m_prod05.tpr

$ qsub -v "selection=12,tpr=3n4m_prod05.tpr,xtc=3n4m_prod01-12_every10ps_tr1.xtc,skip=0" snapshot_generator_on_cluster.sh 

```
