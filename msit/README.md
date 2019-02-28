NOTE

Certain parameters of this task can be altered according to the experimenter's wishes.

These parameters and their defaults are described in lines 73-94 of the script (see below). 







# set number of blocks in experiment (default = 4)
# NOTE: one block = rest + incongruent + rest + congruent
numBlocks = 2

# set duration for incongruent/congruent blocks (default is 60s)
# must be divisible by 10
blockLength = 30

# set duration for rest periods (default = 10)
# note this will be padded with a few varying seconds
# must be divisible by 10
restDuration = 10

# set how many stimuli are in a trial (3 or 4)
# PIP used 3, NOAH plans to use 4
# this will change the appearance of trial and feedback
# NOTE: currently only set for 4
numStims = 4