"""
@author: Prem
"""

from AI_problem import SearchProblem

class StonePuzzleProblem(SearchProblem):
    def __init__(self, grid = ['o','o','_','x','x']):
        self.tiles = grid
        self.emptyCell = self.tiles.index('_')
    
    def getStartState(self):
        return (self.tiles, self.emptyCell, [])
    
    def isGoalState(self, state):
        return ''.join(state[0]) == 'xx_oo'

    def getSuccessors(self, state):
        movesList = []
        tiles, emptyCell, path = state
        
        def generateMove(i, move):
            pathList = list(path)
            pathList.append(move)
            tilesList = list(tiles)
            tilesList[emptyCell], tilesList[emptyCell+i] = tilesList[emptyCell+i], tilesList[emptyCell]
            movesList.append((tilesList, emptyCell+i, pathList))
        
        l = len(tiles)
        if emptyCell < l-1 and tiles[emptyCell+1] == 'x': # _x -> x_
            generateMove(1, 'R')
        if emptyCell > 0 and tiles[emptyCell-1] == 'o': #o_ -> _o 
            generateMove(-1, 'L')
        if emptyCell < l-2 and tiles[emptyCell+2] == 'x' and tiles[emptyCell+1] == 'o': #_ox -> xo_
            generateMove(2, 'JR') #_ox -> xo_
        if emptyCell > 1 and tiles[emptyCell-2] == 'o' and tiles[emptyCell-1] == 'x': #ox_ -> _xo
            generateMove(-2, 'JL')
        
        return movesList

    def getHeuristics(self):
        def hammingDistance(tiles):
            tiles = tiles[0]
            dist = len([i for i in range(len(tiles)) if tiles[i]=='o' and i not in [3,4] or tiles[i]=='x' and i not in [0,1]])
            return dist
        return [hammingDistance]