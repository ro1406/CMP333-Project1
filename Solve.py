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

def solve(problem, search_algorithms):

    def print_info(solution,timetaken):
        if not solution:
            print("No solution!")
            return
        state, num_nodes_exp, num_nodes_gen = solution
        if isinstance(problem, EightPuzzleProblem):
            finalstate,_,steps = state
            cost = len(steps)
        else:
            finalstate, steps = state
            cost = len(steps)
        print(f"Final state: {finalstate}")
        print(f"Solution: {steps}")
        print(f"Cost: {cost}")
        print(f"Number of nodes expanded: {num_nodes_exp}")
        print(f"Number of nodes generated: {num_nodes_gen}")
        print("Total Time Taken: %0.4f seconds"%timetaken)
        print("="*80+"\n")
        

    print(problem.__class__.__name__)

    for algo in search_algorithms:
        if algo.__name__ in ["greedySearch", "astarSearch"]: # heuristic search
            for heuristic in problem.getHeuristics():
              print(f"Algorithm used: {algo.__name__}")
              print(f"Heuristic used: {heuristic.__name__}")
#! Adding timer to time our algorithms        
              t0=time()
              solution = algo(problem, heuristic)
              print_info(solution,time()-t0)
        else:
            print(f"Algorithm used: {algo.__name__}")
            t0=time()
            solution = algo(problem)
            print_info(solution,time()-t0)

puzzle = [1,8,0,
          4,3,2,
          5,7,6]

puzzle2=[1,6,5,
         4,0,2,
         7,3,8]
#solve(EightPuzzleProblem(puzzle2), [breadthFirstSearch, iterativeDeepeningSearch,uniformCostSearch, astarSearch])
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


solve(FarmerPuzzleProblem(),[astarSearch])


###