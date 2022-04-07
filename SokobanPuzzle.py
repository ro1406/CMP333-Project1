# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:59:51 2022

@author: rohan
"""


'''
FORMULATION:

STATE: 2D array of characters representing board state
INITAL STATE: Supplied as param
GOAL STATE: Each $ assigned to exactly one .

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
from copy import deepcopy

def getSokobanBoard(filename):
    with open(filename,'r') as f:
        return [line.strip() for line in f.readlines()]

class SokobanPuzzle (SearchProblem):
    
    def __init__(self,board):
        self.board=[[char for char in board[i]] for i in range(len(board))]
        for x in self.board:
            print(x)

    # a state is a tuple (vector, [states so far])
    def getStartState(self): 
        playerpos=[-1,-1]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]=='@':
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
            mapping={'U':'D','D':'U','L':'R','R':'L'}
            pathCopy = deepcopy(path)
            pathCopy.append(action) # For printing purposes
            gridCopy = deepcopy(grid)
            playerCopy=deepcopy(player)
            #Make change to gridCopy:
            if action=='D':
                if pushBox:
                    gridCopy[player[0]+2][player[1]]='$' #Move box right
                gridCopy[player[0]+1][player[1]]='@' #Move player right
                playerCopy[0],playerCopy[1]=player[0]+1,player[1]
                
            elif action=='U':
                if pushBox:
                    gridCopy[player[0]-2][player[1]]='$' #Move box left
                gridCopy[player[0]-1][player[1]]='@' #Move player left
                playerCopy[0],playerCopy[1]=player[0]-1,player[1]
                
            elif action=='L':
                if pushBox:
                    gridCopy[player[0]][player[1]-2]='$' #Move box up
                gridCopy[player[0]][player[1]-1]='@' #Move player up
                playerCopy[0],playerCopy[1]=player[0],player[1]-1
                
            elif action=='R':
                if pushBox:
                    gridCopy[player[0]][player[1]+2]='$' #Move box down
                gridCopy[player[0]][player[1]+1]='@' #Move player down
                playerCopy[0],playerCopy[1]=player[0],player[1]+1                
            
            gridCopy[player[0]][player[1]]=' ' #Old player location is empty now
            
            if pathCopy[-1]!=mapping[action]: #Dont go back pruning
                moves.append((gridCopy,playerCopy,pathCopy))

        #Preconditions:
        #MoveDown
        if player[0]<len(grid)-1: #IF there is space below:
            if (grid[player[0]+1][player[1]]==" "):#IF empty space below:
                generateMove(player,'D')
            elif (grid[player[0]+1][player[1]]=="$"): #IF theres a box below:
                if (player[0]+1<len(grid)-1) and (grid[player[0]+2][player[1]]==' ' or grid[player[0]+2][player[1]]=='.'): #IF there is space after the box, and its empty:
                    generateMove(player,'D',True)
                    
        #MoveUp
        if player[0]>0: #IF there is space above:
            if (grid[player[0]-1][player[1]]==" "):#IF empty space above:
                generateMove(player,'U')
            elif (grid[player[0]-1][player[1]]=="$"): #IF theres a box above:
                if (player[0]>1) and (grid[player[0]-2][player[1]]==' ' or grid[player[0]-2][player[1]]=='.'): #IF there is space after the box, and its empty:
                    generateMove(player,'U',True)
        
        #MoveRight
        if player[1]<len(grid)-1: #IF there is space on right:
            if (grid[player[0]][player[1]+1]==" "):#IF empty space on right:
                generateMove(player,'R')
            elif (grid[player[0]][player[1]+1]=="$"): #IF theres a box on right:
                if (player[1]+1<len(grid)-1) and (grid[player[0]][player[1]+2]==' ' or grid[player[0]][player[1]+2]=='.'): #IF there is space after the box, and its empty:
                    generateMove(player,'R',True)
        
        #MoveLeft
        if player[1]>0: #IF there is space on left:
            if (grid[player[0]][player[1]-1]==" "):#IF empty space on left:
                generateMove(player,'L')
            elif (grid[player[0]][player[1]-1]=="$"): #IF theres a box on left:
                if (player[1]>1) and (grid[player[0]][player[1]-2]==' ' or grid[player[0]][player[1]-2]=='.'): #IF there is space after the box, and its empty:
                    generateMove(player,'L',True)
        
        return moves

#IDEAS FOR HEURISTICS: 1) Manhattans of each stone with each goal 2) Euclideans of each stone with each goal
#                     Both Heuristics also add the distance between each box and the player (Avoids the player unecessarily going away from any of the boxes)

    def getHeuristics(self):
        def manhattanDist(state): 
            board,player,_=state
            goals=[]
            boxes=[]
            for i in range(len(board)):
                if '.' in board[i]:
                    goals.append([i,board[i].index('.')])
                if '$' in board[i]:
                    boxes.append([i,board[i].index('$')])
            total=0.
            for goal in goals:
                for box in boxes:
                    total+=abs(box[0]-goal[0])+abs(box[1]-goal[1])
                    
            for box in boxes:
                total+=abs(box[0]-player[0])+abs(box[1]-player[1])
            return total
        
        def euclideanDist(state):
            board,player,_ =state
            goals=[]
            boxes=[]
            for i in range(len(board)):
                if '.' in board[i]:
                    goals.append([i,board[i].index('.')])
                if '$' in board[i]:
                    boxes.append([i,board[i].index('$')])
            total=0.
            for goal in goals:
                for box in boxes:
                    total+=((box[0]-goal[0])**2+(box[1]-goal[1])**2)**0.5
            for box in boxes:
                total+=((box[0]-player[0])**2+(box[1]-player[1])**2)**0.5
            return total
        
        return [manhattanDist,euclideanDist]
