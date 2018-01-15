# Trj2Shape: DNA shape analyses of MD trajectories

Local deformations in DNA often play important roles in protein-DNA
recognition/interaction. To gain a better insight in the dynamics of
interaction, researchers use Molecular Dynamics (MD) simulations followed by
the trajectory analyses. `Trj2Shape` is designed to analyze the DNA shape
profiles that helps make better conclusions about the interaction mechanism.

`Trj2Shape` currently analyzes four DNA shape features- Minor Groove Width
(MGW), Propeller Twist (ProT), Helix Twist (HelT) and Roll angle (Roll). 

The documentation elaborates on the steps involved in getting to DNA shape data
from MD trajectories.

## MD trajectories

The general practice in MD simulation of a given system is that we do
progressive (in time) production runs. A given production run starts with the
trajectory of previous one. We end up getting a trajectory file that we analyze
using this tool (a lot of details are being skipped here).

With [Gromacs](http://www.gromacs.org/) as a MD simulator, we get trajectory
files with extension `.xtc`.

From the `.xtc` files we can get snapshot of DNA part of the complex in a
periodic manner. The following command shows how to retrieve the snapshots.

```bash  
# Location: /home/rcf-40/satyanar/projects/cofactor_HTH-EXD-HOX/snapshots/500ns_data/4cyc_all_fixed 
trjconv_mpi -s 4cyc_pr9.tpr -sep -f 4cyc_all_fixed.xtc -o .pdb -skip 5 
... 
Select a group: 12 <choose the one says DNA>
```

Few important points for the above commmand: 

----- 

- irrespective of the tpr file number (4cyc_pr9.tpr, or 4cyc_pr8.tpr) you are
  going to get same output 
- `-skip 5` is telling to skip 5 frames, in turn we are skipping `5ps`. So if
  you have `500 ns` data then you are going to get  500ns / 5ps =
  10<sup>5</sup> `pdb` files.







