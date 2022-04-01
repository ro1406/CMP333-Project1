# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from AI_problem import SearchProblem
from AI_heuristics import AI_heuristics 

class TSPProblem (SearchProblem):
    
    # TSP defined as a set of cities
    # Set being empty is the initial state
    # cities = {A, B, C, D}
    # the way i understand it, is we have two sets and move the cities from the full set into the empty set
    
    def __init__(self):
        self.cities={"A", "B", "C", "D"} # 4 cities A,B,C,D
        self.orderedCities = {} # empty set for ordered cities
        
    # the start states are just the cities set and the empty orderedCities set
    def getStartState(self): return (self.cities, self.orderedCities)

    # goal state is an ordered list of 4 cities
    def isGoalState(self, state):
        return len(orderedCities) == 4





