# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:08:14 2022

@author: rohan
"""


from AI_problem import SearchProblem
from AI_heuristics import AI_heuristics

class FarmerPuzzleProblem (SearchProblem):
    # Boolean vector of (F,W,S,C) Locations
    # True -> They crossed the river to the other side
    # False -> They did NOT cross the river to the other side
    def __init__(self):
        self.vector=[False for i in range(4)]#Initially all on this side of river

    # a state is a tuple (vector, [states so far])
    def getStartState(self): return (self.vector, [self.vector])

    # the goal state is defined as [True,True,True,True]
    def isGoalState(self, state):
        vec, path = state
        return sum(vec)==4

    def getSuccessors(self, state):
        moves = []
        vec, path = state
        
        def generateMove(idxs, action): #List of all indices to flip, Human interpretable action
            pathCopy = list(path)
            pathCopy.append(action) # For printing purposes
            vecCopy = list(vec)
            for i in idxs:
                vecCopy[i]= not vecCopy[i]
            moves.append((vecCopy,pathCopy))


        if vec[2]!=vec[1] and vec[2]!=vec[3]: #Sheep not on the same side as wolf or cabbage
            generateMove([0],"F<-" if vec[0] else "F->") #Farmer only
        if vec[0]==vec[2]: #Farmer and sheep same side
            generateMove([0,2],"FS<-" if vec[0] and vec[2] else "FS->") #Farmer+Sheep
        if vec[0]==vec[1] and vec[2]!=vec[3]:#Farmer wolf same side, but sheep and cabbage diff side
            generateMove([0,1],"FW<-" if vec[0] and vec[1] else "FW->") #Farmer+Wolf
        if vec[0]==vec[3] and vec[2]!=vec[1]:#Farmer and cabbage same side, but sheep and wolf diff side
            generateMove([0,3],"FC<-" if vec[0] and vec[3] else "FC->") #Farmer+Cabbage
        

        return moves

    def getHeuristics(self):
        def hammingDist(state): #Number of ones in the grid
            return sum(state[0])
        return [hammingDist]

###