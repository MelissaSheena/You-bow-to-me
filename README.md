# Task: 

## The world
- must have a temporal dimension (time goes by in rounds)
- one round of day is followed by
- one round of night
- amount of rounds can be configured (0 – ∞)
- must have 2 spatial dimensions (X/Y axis)
- size of the world (length of Y/X axis) must be configurable
## There should be events:
- every day the sun is randomly shining in some places (cells) (based on a configurable probability between 100-0)
- every day it rains in some random places (cells)
  - based on a configurable probability between 100-0
  - however when the sun is shining its x percent less likely that it rains
  - x is configurable
  - since the cells get wet, they stay wet over night and are only considered dried when the next day starts
- for every cell/place on the grid at any moment we should be able to know about:
  -  that might be there,
  - sun that might be shining,
  - which cells are neighbors to it (left, right, top, bottom)
