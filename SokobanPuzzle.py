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
    1) MoveRight -> No wall on right, box must have empty cell on its right
    2) MoveLeft -> No wall on left, box must have empty cell on its left
    3) MoveDown -> No wall on down, box must have empty cell below
    4) MoveUp -> No wall on up, box must have empty cell above
    
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
    def getStartState(self): 
        playerpos=[-1,-1]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]=='@':
                    playerpos=[i,j]      #[x,y]
                
        return (self.board, playerpos,[])

    # the goal state is defined if there are no '.' on the board:
    def isGoalState(self, state):
        grid, player, path = state
        isGoal=True
        for line in grid:
            if '.' in line:
                isGoal=False
                break
        return isGoal

    def getSuccessors(self, state):
        moves = []
        grid, player, path = state
        
        #Make respective post conditions:
        def generateMove(player, action, pushBox=False):
            pathCopy = list(path)
            pathCopy.append(action) # For printing purposes
            gridCopy = list(grid)
            #Make change to gridCopy:
            if action=='R':
                if pushBox:
                    gridCopy[player[0]+2][player[1]]='$' #Move box right
                gridCopy[player[0]+1][player[1]]='@' #Move player right
            elif action=='L':
                if pushBox:
                    gridCopy[player[0]-2][player[1]]='$' #Move box left
                gridCopy[player[0]-1][player[1]]='@' #Move player left
            elif action=='U':
                if pushBox:
                    gridCopy[player[0]][player[1]+2]='$' #Move box up
                gridCopy[player[0]][player[1]+1]='@' #Move player up
            elif action=='D':
                if pushBox:
                    gridCopy[player[0]][player[1]-2]='$' #Move box down
                gridCopy[player[0]][player[1]-1]='@' #Move player down
            
            gridCopy[player[0]][player[1]]=' ' #Old player location is empty now
            moves.append((gridCopy,pathCopy))

        #Preconditions:
        #MoveRight
        if player[0]<len(grid)-1: #IF there is space on the right:
            if (grid[player[0]+1,player[1]]==" "):#IF empty space on right:
                generateMove(player,'R')
            elif (grid[player[0]+1][player[1]]=="$"): #IF theres a box on the right:
                if (player[0]+1<len(grid)-1) and grid[player[0]+2][player[1]]==' ': #IF there is space after the box, and its empty:
                    generateMove(player,'R',True)
                    
        #MoveLeft
        if player[0]>0: #IF there is space on the left:
            if (grid[player[0]-1,player[1]]==" "):#IF empty space on left:
                generateMove(player,'L')
            elif (grid[player[0]-1][player[1]]=="$"): #IF theres a box on the left:
                if (player[0]>1) and grid[player[0]-2][player[1]]==' ': #IF there is space after the box, and its empty:
                    generateMove(player,'L',True)
        
        #MoveDown
        if player[1]<len(grid)-1: #IF there is space below:
            if (grid[player[0],player[1]+1]==" "):#IF empty space below:
                generateMove(player,'D')
            elif (grid[player[0]][player[1]+1]=="$"): #IF theres a box below:
                if (player[1]+1<len(grid)-1) and grid[player[0]][player[1]+2]==' ': #IF there is space after the box, and its empty:
                    generateMove(player,'D',True)
        
        #MoveUp
        if player[1]>0: #IF there is space above:
            if (grid[player[0],player[1]-1]==" "):#IF empty space above:
                generateMove(player,'U')
            elif (grid[player[0]][player[1]-1]=="$"): #IF theres a box below:
                if (player[1]>1) and grid[player[0]][player[1]-2]==' ': #IF there is space after the box, and its empty:
                    generateMove(player,'U',True)
        
        return moves

############################### ONLY DONE TILL HERE #####################################

#IDEAS FOR HEURISTICS: 1) Manhattans of each stone with each goal 2) Euclideans of each stone with each goal

    def getHeuristics(self):
        def manhattanDist(state): 
            return 4-sum(state[0])
        return [manhattanDist]
