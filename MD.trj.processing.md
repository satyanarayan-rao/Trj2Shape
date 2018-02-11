# Getting snapshots from MD trajectories

The general practice in MD simulation of a given system is that we do
progressive (in time) production runs. A given production run starts with the
trajectory of previous one. We end up getting a trajectory file that we analyze
using this tool (a lot of details are being skipped here).

With [Gromacs](http://www.gromacs.org/) as a MD simulator, we get trajectory
files with extension `.xtc`.

From the `.xtc` files we can get snapshots of DNA part of the complex in a
periodic manner. The following command shows how to retrieve the snapshots.

```bash  
# Location: /home/rcf-40/satyanar/projects/cofactor_HTH-EXD-HOX/snapshots/500ns_data/4cyc_all_fixed 
$ trjconv_mpi -s 4cyc_pr9.tpr -sep -f 4cyc_all_fixed.xtc -o .pdb -skip 5 
... 
Select a group: 12 <choose the one says DNA>


You can get around with not inputting `12`after the `trjconv_mpi` command by using the following alternate version
$ echo 12 | trjconv_mpi -s 4cyc_pr9.tpr -sep -f 4cyc_all_fixed.xtc -o .pdb -skip 5

```

Few important points for the above command: 

----- 

- irrespective of the tpr file number (4cyc_pr9.tpr, or 4cyc_pr8.tpr) you are
  going to get same output 
- `-skip 5` is telling to skip 5 frames, in turn we are skipping `5ps`. So if
  you have `500 ns` data then you are going to get  500ns / 5ps =
  10<sup>5</sup> `pdb` files.

The above command will take a **while** to finish (depending on the `.xtc` file
size)!
