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
        self.posInitial = posInitial
        self.citiesVisited = [posInitial]
        

    def getStartState(self): return (self.citiesVisited,self.posInitial,[],[0])

    def isGoalState(self, state):
        return len(state[0]) == len(self.grid)
    
    def getSuccessors(self, state):
        progress = []
        citiesVisited, posInitial, path, costs = state
        
        def madeProgress(count, moves):
            nonlocal posInitial
            pathTemp = list(path)
            cVTemp = list(citiesVisited)
            costsTemp = list(costs)
            
            pathTemp.append(moves)
            cVTemp.append(count)
            costsTemp.append(self.grid[posInitial][costs])
            progress.append(cVTemp, count, pathTemp, costsTemp)
            
        for i in range(len(self.grid)):
            if i not in citiesVisited:
                madeProgress(i, f'{posInitial}->{i}')
                return moves
            
    def getHeuristics(self):
        def closestNeighbour(grid):
            grid = grid[-1]
            return grid[-1]
        return [closestNeighbour]
        





