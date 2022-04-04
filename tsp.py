# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from AI_problem import SearchProblem
from AI_heuristics import AI_heuristics 

class TSPProblem (SearchProblem):

    def __init__(self, grid, posInitial=0):
        self.grid = grid
        self.currPos = posInitial
        self.citiesVisited = {posInitial}
        
    def getStartState(self): return (self.citiesVisited,self.currPos,[],[0])#State,position,path so far, cost so far

    def isGoalState(self, state):
        return len(state[0]) == len(self.grid)
    
    def getSuccessors(self, state):
        moves = []
        citiesVisited, position, path, costs = state
        
        def generateMove(newpos, movemade): #new position, move in human readable format
            pathCopy = list(path)
            cVCopy = set(citiesVisited)
            costsCopy = list(costs)
            
            pathCopy.append(movemade)
            cVCopy.add(newpos)
            costsCopy.append(self.grid[position][newpos])
            moves.append((cVCopy, newpos, pathCopy, costsCopy))
            
        for i in range(len(self.grid)):
            if i not in citiesVisited:
                generateMove(i, str(position)+"->"+str(i))
        return moves
            
    def getHeuristics(self):
        def closestNeighbour(grid):
            grid = grid[-1]
            return grid[-1]
        return [closestNeighbour]
        





