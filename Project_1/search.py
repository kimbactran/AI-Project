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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """Ví dụ thuật toán bfs:
    def bfs(start, goal, graph):
  #start: điểm bắt đầu
  #goal: điểm kết thúc
  #graph: đồ thị
  visited = set() #Lưu trữ các node đã được duyệt
  queue = deque([(start, [start])]) # Hàng đợi chưa các node chưa duyệt và đường đi từ start đến node đó,
  #Giá trị khởi tạo là nút đầu tiên

  while queue: #Duyệt phần tử trong hàng đọi
    #In ra hàng đợi mỗi lần duyệt, câu lệnh này chủ yếu để xem hàng đợi, không ảnh hưởng tới thuật toán
    print("Current Queue:", queue)  # In giá trị của queue
    node, path = queue.popleft() #lấy phần tử đầu hàng đợi
    # nếu node bằng goal (đích) thì trả về đường đi
    if node == goal:
      return path
    #nếu node chưa được duyệt => không nằm trong visited, thêm node vào hàng đợi
    if node not in visited:
      visited.add(node)

      # Thêm các nút kề vào hàng đợi
      for neighbor in graph[node]:
        # Nếu nút kề chưa được duyệt
        if neighbor not in visited:
          queue.append((neighbor, path + [neighbor])) # Thêm nốt vào hàng đợi
  return None # Nếu không tìm được đường đi trả về None
    """
    #Hàm truyền vào tham số problem: vấn đề phải tìm kiếm với các hàm được tích hợp sẵn
    #problem.getStartState(): trả về trạng thái điểm bắt đầu
    #problem.isGoalState(problem.getStartState()): Kiểm tra xem trạng thái bắt đầu có phải là đích không
    #problem.getSuccessors(problem.getStartState()): Các trạng thái không gian của trạng thái bắt đầu có dạng
    #(trạng thái tiếp theo, hành động, chi phí)
    visited = {} #Khởi tạo một biến lưu trữ các node đã được duyệt
    queue = util.Queue() #Khởi tạo một hàng đợi chứa các node chưa được duyệt
    start_node = problem.getStartState()
    action = []
    cost = 0
    queue.push((start_node, action, cost))
    #Khởi tạo trạng thái ban đầu có trạng thái bằng trạng thái ban đầu, hành động tiếp theo là tạp rỗng và có chi phí bằng 0
    # Vòng lặp
    while not queue.isEmpty():
        node = queue.pop() # Lấy ra node ở đầu hàng đợi
        #Kiểm tra xem node ban đầu có phải là đích hay không
        if problem.isGoalState(node[0]):
            return node[1] #trả về hành động tiếp theo của node
        # Nếu node chưa được thăm => Thêm node vào mảng chứa các node đã duyệt
        if node[0] not in visited:
            visited[node[0]] = True
            #Thêm các nút kề vào queue
            for next, action, cost in problem.getSuccessors(node[0]):
                # Kiểm tra nút này đã được duyệt chưa
                if next and next not in visited:
                    
                    #Thêm node vào hàng đợi
                    queue.push((next, node[1] + [action], node[2] + cost))   
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # problem: vấn đề tìm kiếm
    # SearchProblem: đây là loại đối số mong đọi cho biến problem.
    # heuristic: Hàm heuristic (ở bài này đã được cho sẵn): manhattanHeuristic dòng 257 file searchAgents.py
    # Thuật toán A* là kết hợp giữa tìm kiếm BFS và tìm kiếm chi phí
    priorityQueue = util.PriorityQueue() # Khởi tạo 1 hàng đợi ưu tiên
    start_node = problem.getStartState()
    action =[]
    cost = 0
    priorityQueue.push((start_node, action, cost), cost)
    # Khởi tạo node đầu tiên với điểm bắt đầu hành động rỗng và chi phí bằng 0
    # Thuật toán A* xét tới chi phí nên thêm 1 biến nữa là cost

    visited = {} # Lưu trữ các node đã duyệt
    while not priorityQueue.isEmpty():
        node = priorityQueue.pop() # Lấy node có ưu tiên cao nhất ra khỏi hàng đợi ưu tiên
        # Kiểm tra xem node đầu tiên có trùng với điểm đích không nếu có trả về action
        if problem.isGoalState(node[0]):
            return node[1]#trả về hành động tiếp theo của node
        # Nếu node chưa được thăm => Thêm node vào mảng chứa các node đã duyệt
        if node[0] not in visited:
            visited[node[0]] = True
            #Thêm các nút kề vào queue
            for next, action, cost in problem.getSuccessors(node[0]):
                # Kiểm tra nút này đã được duyệt chưa
                if next and next not in visited:    
                    #Thêm node vào hàng đợi ưu tiên
                    priorityQueue.push((next, node[1] + [action], node[2] + cost), heuristic(next, problem) + cost) 
            
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
