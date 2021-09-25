# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains search functions.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (alpha, beta, gamma) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs)
# You may need to slight change your previous search functions in MP1 since this is 3-d maze

from collections import deque
from heapq import heappop, heappush

def search(maze, searchMethod):
    return {
        "bfs": bfs,
    }.get(searchMethod, [])(maze)

def bfs(maze, ispart1=False):
    ispart1 = True
    # Write your code here
    """
    This function returns optimal path in a list, which contains start and objective.
    If no path found, return None. 

    

    Args:
        maze: Maze instance from maze.py
        ispart1: pass this variable when you use functions such as getNeighbors and isObjective. DO NOT MODIFY THIS
    """

    # Create a visited, queue and path for BFS
    queue = []
    path = []
    visited = {}

    # Mark start as visited and enqueue it
    queue.append(maze.getStart())
    visited[maze.getStart()] = "start"
    to_add = maze.getStart()

    while queue:
        # Dequeue a vertex from queue and add to path
        curr = queue[0]
        queue.pop(0)

        # Get all neighbours of the dequeued current. If a neighbour point
        # has not been visited, then mark it as visited and enqueue it
        for neighbor in maze.getNeighbors(curr[0], curr[1], curr[2], ispart1):
            if visited.get(neighbor) == None:
                visited[neighbor] = curr
                queue.append(neighbor)
                if maze.isObjective(neighbor[0], neighbor[1], neighbor[2], ispart1):
                    to_add = neighbor
                    print("reached")
                    print(maze.getStart())
                    print(neighbor)
                    print(visited.get(to_add))
                    break

    # add points to path from waypoint to start
    if (not maze.isObjective(to_add[0], to_add[1], to_add[2], ispart1)) :
        return None

    while to_add != "start":
        path.insert(0, to_add)
        to_add = visited.get(to_add)

    return path