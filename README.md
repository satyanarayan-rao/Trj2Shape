# Trj2Shape: DNA shape analyses of MD trajectories

Local deformations in DNA often play important roles in protein-DNA
recognition/interaction. To gain a better insight in the dynamics of
interaction, researchers use Molecular Dynamics (MD) simulations followed by
the trajectory analyses. `Trj2Shape` is designed to analyze the DNA shape
profiles that helps make better conclusions about the interaction mechanism.

`Trj2Shape` currently analyzes four DNA shape features— Minor Groove Width
(MGW), Propeller Twist (ProT), Helix Twist (HelT) and Roll angle (Roll). 

The documentation elaborates on the steps involved in getting to DNA shape data
from MD trajectories.

If you want to run `Trj2Shape` in high-throughput manner, please follow
[this](./README.cluster_version.md) documentation. 

This documentation assumes **${Trj2Shape}** shell variable as github cloned path.
Its preferred to use `Trj2Shape` scripts in existing data directories. It saves
data I/O operations.

Documentation about generating snapshots from a given production stage
trajectory file can be found [here](./MD.trj.processing.md).

Documentation about insight to data processing by Curves can be found
[here](./Curves.processing.md).


The goal for this work to come up with shape profiles like the following (shown
here for MGW).

![alt_text][avg_MGW]{:height="50%" width="50%"}

[avg_MGW]: ./visualization/avg_MGW_3n4m.MGW.png
