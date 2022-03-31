# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:59:51 2022

@author: rohan
"""
######################################### TBD ##############################################


'''
FORMULATION:

STATE: Array of strings representing board state
INITAL STATE: Supplied as param
GOAL STATE: No . left on the board (We will overwrite a dot if we push the box onto it)
    

ACTIONS:
PRECOND:
    1) MoveRight -> No wall on right, no box with another box on the right, no box then wall
    2) MoveLeft -> No wall on left, no box with another box on the left, no box then wall
    3) MoveDown -> No wall on down, no box with another box on the down, no box then wall
    4) MoveUp -> No wall on up, no box with another box on the up, no box then wall
    
POSTCOND:
    1) MoveRight -> Player moves right, and takes box with him if there is one
    2) MoveLeft -> Player moves left, and takes box with him if there is one
    3) MoveDown -> Player moves down, and takes box with him if there is one
    4) MoveUp -> Player moves up, and takes box with him if there is one

    
COST: Uniform? Heuristics: Manhattan and Euclidean

'''


from AI_problem import SearchProblem
from AI_heuristics import AI_heuristics

class SokobanPuzzle (SearchProblem):
    
    def __init__(self,board):
        self.board=list(board)

    # a state is a tuple (vector, [states so far])
    def getStartState(self): return (self.board, [self.board])

############################### ONLY DONE TILL HERE #####################################

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
        def hammingDist(state): #Number of zeros in the vector
            return 4-sum(state[0])
        return [hammingDist]
