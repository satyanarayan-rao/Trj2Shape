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

This documentation assumes **${Trj2Shape}** shell variable as github cloned path.
Its preferred to use `Trj2Shape` scripts in existing data directories. It saves
data I/O operations.

## MD trajectories

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
trjconv_mpi -s 4cyc_pr9.tpr -sep -f 4cyc_all_fixed.xtc -o .pdb -skip 5 
... 
Select a group: 12 <choose the one says DNA>
```

Few important points for the above command: 

----- 

- irrespective of the tpr file number (4cyc_pr9.tpr, or 4cyc_pr8.tpr) you are
  going to get same output 
- `-skip 5` is telling to skip 5 frames, in turn we are skipping `5ps`. So if
  you have `500 ns` data then you are going to get  500ns / 5ps =
  10<sup>5</sup> `pdb` files.

The above command will take a **while** to finish (depending on the `.txc` file
size)!

## Running Curves

(Curves)[https://bisi.ibcp.fr/tools/curves_plus/]  is an algorithm for
calculating the helical parameter description of any irregular nucleic acid
segment with respect to its optimal, global helical axis (taken verbatim for
[here](http://www.csb.yale.edu/userguides/datamanip/curves/doc.html)). We use
the version 5.3, and the [source code](./Curves/Curves5.3.tar)/binary is
included here (see [Curves](./Curves)). Instructions to install are as follows: 

```bash
$ cd Curves
$ tar -xvf Curves5.3.tar
$ make 
$ 
```
You should see a binary file named `Cur5`. We'll using this for downstream
analyses.

### Pre-processing MD snapshots
Unfortunately, Curves program only recognizes letter {'A', 'C', 'G', 'T'} as
DNA alphabet. And most of the time we see the nucleotides as {'DA', 'DC', 'DG',
'DT'} in PDB files. To comply with Curves format, we have to pre-process the
snapshots. 

Since we are dealing with a lot of snapshots (pdbs) here, its preferable to write
shell scripts/one-liners.

```
# list all the pdbs in numerical order

$ ls -v *.pdb > pdbList 
$ nohup sh rename-nuc.sh pdbList &
```
Again, this command will take a while to finish!

## Curves input

Since `Curves` is a legacy program, input format for this is quite different
than current practices. Here I show an example: 
```bash
$ cat common.crv
 &inp file=common.pdb,dinu=.t.,comb=.t.,fit=.t.,
 lis=common,pdb=,grv=.t., &end
2  13 -13 0 0
1 2 3  4 5 6 7 8 9 10 11 12 13
26 25 24 23 22 21 20 19 18 17 16 15 14
0. 0. 0. 0.
```
**2 13 -13 0 0**: This line indicates that your DNA is a duplex helix (2) of
length 13. -13 indicated the reverse strand.

The two lines (numbered `1-13` and `26-14`) are the base to base pairing. Here
are some important notes for writing these two lines:

+ Check the PDB file

    - It helps to open the file in Pymol or other similar program and check one
      of two bases on forward strand and their paring on the other strand

    - Your first residue may have the id number not starting at 1 (can start
      from 3, 4 or any other number, sometimes negative numbers). But Curves
      (at least the version I am discussing here) only takes ids starting from
      1. So you have to do the mapping.

```bash
$ sh generateCRVforPDB.sh pdbList

```

The above script makes generate `.crv` file for each snapshot.
