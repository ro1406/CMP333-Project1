##############################################################################
###
###   CMP 333 PROJECT 1 -- SEARCH
###
###   AI SEARCH ALGORITHMS AND SUPPORTING DATA STRUCTURES for the frontier
###   General Search and BFS, DFS, IDA, UFS, A*, and Greedy search;
###   Stack, Queue, and Priority Queue.
###
###   Michel Pasquier 2019, adapted from the code @
###   https://kartikkukreja.wordpress.com/2015/06/14/heuristics-in-ai-search/
###


class Stack:
    def __init__(self): self.items = []

    def push(self, item): self.items.append(item)

    def pop(self): return self.items.pop()

    def empty(self): return not self.items

from collections import deque
class Queue:
    def __init__(self): self.items = deque()

    def push(self, item): self.items.append(item)

    def pop(self): return self.items.popleft()

    def empty(self): return not self.items

import heapq
class PriorityQueue:
    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, (self.priorityFunction(item), item))

    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        return item

    def empty(self): return not self.heap


def generalSearch(problem, strategy):
    strategy.push(problem.getStartState())
    # added counters to keep track of the number of nodes expanded/generated
    num_nodes_exp = 0
    num_nodes_gen = 1
    while not strategy.empty():
        num_nodes_exp += 1
        #> uncomment below to print the priority queue at each iteration
        #print(strategy.heap)
        node = strategy.pop()

        #> uncomment below to print the node being expanded
        #print(node)
        if problem.isGoalState(node):
            return (node, num_nodes_exp, num_nodes_gen)

        for move in problem.getSuccessors(node):
            strategy.push(move)
            num_nodes_gen += 1
        #> uncomment to print num of nodes generated after each node expansion
        #print(num_nodes_gen)
    return None

def breadthFirstSearch(problem): return generalSearch(problem, Queue())

def depthFirstSearch(problem): return generalSearch(problem, Stack())

def iterativeDeepeningSearch(problem):
    num_nodes_exp = 0
    num_nodes_gen = 1
    def depthLimitedDFS(problem, state, depth):
        nonlocal num_nodes_gen, num_nodes_exp
        num_nodes_exp += 1
        if problem.isGoalState(state): return state
        if depth <= 0: return None
        for move in problem.getSuccessors(state):
            num_nodes_gen += 1
            solution = depthLimitedDFS(problem, move, depth-1)
            if solution is not None: return solution
        return None

    depth = 1
    while True:
        solution = depthLimitedDFS(problem, problem.getStartState(), depth)
        if solution is not None:
            return (solution, num_nodes_exp, num_nodes_gen)
        depth += 1

def uniformCostSearch(problem):
    return generalSearch(problem, PriorityQueue(lambda state: (sum(state[3]) if len(state) > 3 else len(state[-1]))))

def greedySearch(problem, heuristic):
    return generalSearch(problem, PriorityQueue(heuristic))

def astarSearch(problem, heuristic):
    # the given function uses the number of steps as g-cost (uniform cost)
    # the number of elements in a state changes for different problems, hence
    # the following checks
    totalCost = lambda state: (sum(state[3]) if len(state) > 3 else len(state[-1])) + heuristic(state)
    return generalSearch(problem, PriorityQueue(totalCost))


###