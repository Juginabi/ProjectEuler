#!/usr/bin/python
# Filename: Problem015.py
# Grid path. How many paths are there in X * X grid from top left corner to bottom right corner.
# Combination mathematics: Distance to goal = X*2. Directions: Two groups of 20 each. 
# Formula: Distance_to_goal! / (GroupSize! * (Distance_to_goal - GroupSize)!)

import math

#side = input('Side length of the grid?: ')
side = 20
distance = side * 2
paths = math.factorial(distance) / (math.factorial(side)*math.factorial(distance-side))

print 'Unique paths in {0}x{0} grid: {1}'.format(side,paths)

