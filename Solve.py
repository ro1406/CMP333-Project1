##############################################################################
###
###   CMP 333 PROJECT 1 -- SEARCH
###
###   SOLV FUNCTION used to solve various AI search problems
###
###   Michel Pasquier 2019, to be adapted/expanded as necessary
###

from time import time
from AI_search import generalSearch, breadthFirstSearch, depthFirstSearch, \
    iterativeDeepeningSearch, uniformCostSearch, greedySearch,astarSearch, \
    Stack, Queue, PriorityQueue
from EightPuzzleProblem import EightPuzzleProblem
from PacmanProblem import PacmanProblem
from FarmerPuzzleProblem import FarmerPuzzleProblem
from SokobanPuzzle import SokobanPuzzle
from StonePuzzleProblem import StonePuzzleProblem
from tsp import TSPProblem

def solve(problem, search_algorithms):

    def print_info(solution,timetaken):
        if not solution:
            print("No solution!")
            return
        state, num_nodes_exp, num_nodes_gen = solution
        if isinstance(problem, EightPuzzleProblem) or isinstance(problem,StonePuzzleProblem) or isinstance(problem,SokobanPuzzle):
            finalstate,_,steps = state
            cost = len(steps)
        elif isinstance(problem,TSPProblem):
            finalstate,_,steps,costs = state
            cost = sum(costs)
        else:
            finalstate, steps = state
            cost = len(steps)
        print(f"Final state: {finalstate}")
        print(f"Solution: {steps}")
        print(f"Cost: {cost}")
        print(f"Number of nodes expanded: {num_nodes_exp}")
        print(f"Number of nodes generated: {num_nodes_gen}")
        print("Total Time Taken: %0.12f seconds"%timetaken)
        print("="*80+"\n")
        
    isSokoban=isinstance(problem,SokobanPuzzle)
    print(problem.__class__.__name__)

    for algo in search_algorithms:
        if algo.__name__ in ["greedySearch", "astarSearch"]: # heuristic search
            for heuristic in problem.getHeuristics():
              print(f"Algorithm used: {algo.__name__}")
              print(f"Heuristic used: {heuristic.__name__}")
#! Adding timer to time our algorithms        
              t0=time()
              solution = algo(problem, heuristic,isSokoban)
              print_info(solution,time()-t0)
        else:
            print(f"Algorithm used: {algo.__name__}")
            t0=time()
            solution = algo(problem,isSokoban)
            print_info(solution,time()-t0)

#! Main section calling the solve function for different puzzles:
    
puzzle = [1,8,0,
          4,3,2,
          5,7,6]

puzzle2=[1,6,5,
         4,0,2,
         7,3,8]

#solve(EightPuzzleProblem(puzzle), [breadthFirstSearch, iterativeDeepeningSearch,uniformCostSearch, astarSearch])
#solve(EightPuzzleProblem(puzzle2),[astarSearch])

pacmap = ["P---------",
          "%%-%%-%-%%",
          "---%--%---",
          "-%%%-%%%-%",
          "---%%%-.-%",
          "-%------%%"]

pacmap2=[ "P--------%",
          "%-%%%-%%-%",
          "%---%----%",
          "%-%-%%%-%%",
          "%-%------%",
          "%----%%%--",
          "%----%---."]

#solve(PacmanProblem(pacmap2, (0,0), (6,9)),[breadthFirstSearch, iterativeDeepeningSearch,uniformCostSearch, astarSearch])
#solve(FarmerPuzzleProblem(),[breadthFirstSearch,iterativeDeepeningSearch,uniformCostSearch,greedySearch,astarSearch])
#solve(StonePuzzleProblem(),[breadthFirstSearch,depthFirstSearch,iterativeDeepeningSearch,uniformCostSearch,greedySearch,astarSearch])

grid=[[0,20,42,35],
      [20,0,30,34],
      [42,30,0,12],
      [35,34,12,0] ]

#solve(TSPProblem(grid),[breadthFirstSearch,depthFirstSearch,iterativeDeepeningSearch,uniformCostSearch,greedySearch,astarSearch])


board="./Sokoban_boards/01_easy.txt"
solve(SokobanPuzzle(board),[iterativeDeepeningSearch,uniformCostSearch,greedySearch,astarSearch])
#solve(SokobanPuzzle(board),[depthFirstSearch])
