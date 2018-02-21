# Running Curves

[Curves](https://bisi.ibcp.fr/tools/curves_plus/)  is an algorithm for
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

## Pre-processing MD snapshots
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
2  20 -20 0 0
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 
0. 0. 0. 0.
```
**2 20 -20 0 0**: This line indicates that DNA is a duplex helix (2) and number
of nucleotides considered here for the analyses is 20. –13 indicated the
reverse strand.

The two lines (numbered `1-20` and `44-25`) are the base to base pairing. Here
are some important notes for writing these two lines:

+ Check the PDB file

    - It helps to open the file in Pymol or other similar program and check one
      of two bases on forward strand and their paring on the other strand

    - Your first residue may have the id number not starting at 1 (can start
      from 3, 4 or any other number, sometimes negative numbers). But Curves
      (at least the version I am discussing here) only takes ids starting from
      `1`. So you have to do the mapping.

```bash
$ sh generateCRVforPDB.sh pdbList

```

The above script makes generate `.crv` file for each snapshot.

