##############################################################################
###
###   CMP 333 PROJECT 1 -- SEARCH
###
###   HEURISTIC FUNCTIONS for the 8-puzzle problem used by search algorithms
###   to be amended/expanded for other problems defined via the Problem class

###   Michel Pasquier 2019, adapted from the code @
###   https://kartikkukreja.wordpress.com/2015/06/14/heuristics-in-ai-search/
###


class AI_heuristics:

    def hammingDistance(grid):
        # a state is a tuple of the form (grid, pos0, path)
        grid = grid[0]
        return len([i for i in range(len(grid)) if grid[i] != 0 and grid[i] != i+1])

    # e.g. print(hammingDistance(([2,1,3,4,5,6,7,8,0], 8, [])))

    def manhattanDistance(grid):
        grid = grid[0]
        def distance(i):
            return 0 if grid[i] == 0 else abs(((grid[i]-1) / 3) - (i / 3)) + abs(((grid[i]-1) % 3) - (i % 3))
        return sum(distance(i) for i in range(len(grid)))


###