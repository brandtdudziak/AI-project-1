# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    node = Node(None, None, problem.getStartState())
    if problem.isGoalState(node.state):
         return node.getActionList()

    frontier = util.Stack()
    frontier.push(node)
    explored = {}

    while not frontier.isEmpty():
        node = frontier.pop()
        # Check goal state
        if problem.isGoalState(node.state):
            return node.getActionList()

        if explored.get(node.state) is None:
            # Update explored
            explored.update({node.state : True})

            # Expand children
            for action in problem.getSuccessors(node.state):
                child = Node(node, action[1], action[0])
                frontier.push(child)

    return None
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    node = Node(None, None, problem.getStartState())
    if problem.isGoalState(node.state):
         return node.getActionList()

    frontier = util.Queue()
    frontier.push(node)
    explored = {}

    while not frontier.isEmpty():
        node = frontier.pop()
        # Check goal state
        if problem.isGoalState(node.state):
            return node.getActionList()

        if explored.get(node.state) is None:
            # Update explored
            explored.update({node.state : True})

            # Expand children
            for action in problem.getSuccessors(node.state):
                child = Node(node, action[1], action[0])
                frontier.push(child)

    return None
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    node = Node(None, None, problem.getStartState())
    if problem.isGoalState(node.state):
         return node.getActionList()

    frontier = util.PriorityQueue()
    frontier.push(node, problem.getCostOfActions(node.getActionList()))
    explored = {}

    while not frontier.isEmpty():
        node = frontier.pop()
        # Check goal state
        if problem.isGoalState(node.state):
            return node.getActionList()

        if explored.get(node.state) is None:
            # Update explored
            explored.update({node.state : True})

            # Expand children
            for action in problem.getSuccessors(node.state):
                child = Node(node, action[1], action[0])
                frontier.push(child, problem.getCostOfActions(child.getActionList()))

    return None
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    node = Node(None, None, problem.getStartState())
    if problem.isGoalState(node.state):
         return node.getActionList()

    frontier = util.PriorityQueue()
    f = problem.getCostOfActions(node.getActionList()) + heuristic(node.state, problem)
    frontier.push(node, f)
    explored = {}

    while not frontier.isEmpty():
        node = frontier.pop()
        # Check goal state
        if problem.isGoalState(node.state):
            return node.getActionList()

        if explored.get(node.state) is None:
            # Update explored
            explored.update({node.state : True})

            # Expand children
            for action in problem.getSuccessors(node.state):
                child = Node(node, action[1], action[0])
                f = problem.getCostOfActions(child.getActionList()) + heuristic(child.state, problem)
                frontier.push(child, f)

    return None
    util.raiseNotDefined()


class Node:
    def __init__(self, parent, action, state):
        self.parent = parent
        self.action = action
        self.state = state

    def getActionList(self):
        actions = [self.action]
        parentNode = self.parent
        # Need to switch this back. Doesnt work if the solution is the first node
        while parentNode!= None:
            actions.append(parentNode.action)
            parentNode = parentNode.parent
        actions = actions[:-1]
        actions.reverse()
        return actions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
