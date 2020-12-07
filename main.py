def printArray(array):
    for i in range(ROW):
        for j in range(COL):
            print(array[i][j], end=' ')
        print()


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Node:
    def __init__(self):
        self.f = float("inf")
        self.h = float("inf")
        self.g = float("inf")
        self.parent_i = -1
        self.parent_j = -1

    def __str__(self):
        return f'f: %s , h: %s ,g: %s', {self.f, self.h, self.g}


class setItem:
    def __init__(self, f, i, j):
        self.f = f
        self.i = i
        self.j = j

    def __str__(self):
        return f'f: %s , i: %s ,j: %s', {self.f, self.i, self.j}


def tracePath(cellDetails, goal):
    row = goal.i
    col = goal.j
    path = []
    while not (cellDetails[row][col].parent_i == row and cellDetails[row][col].parent_j == col):
        path.append(Cell(row, col))

        tempRow = cellDetails[row][col].parent_i
        tempCol = cellDetails[row][col].parent_j
        row = tempRow
        col = tempCol
        pass
    path.append(Cell(row, col))

    while len(path) != 0:
        x = path.pop()
        print("-> ({i},{j})".format(i=str(x.i), j=str(x.j)))


def checkBlock(array, row, col):
    return array[row][col] == "0"


def checkValid(row, col):
    return 0 <= row < ROW and 0 <= col < COL


def calculateHeuristic(i, j, goal):
    h = abs(i - goal.i) + abs(j - goal.j)
    return h


def isGoal(i, j, goal):
    return i == goal.i and j == goal.j


def aStar(matrix, source, goal):
    closedList = [[False for j in range(10)] for i in range(10)]
    cellDetails = []
    for i in range(ROW):
        cellDetails.append([])
        for j in range(COL):
            cellDetails[i].append(Node())
    i = source.i
    j = source.j
    cellDetails[i][j].f = 0.0
    cellDetails[i][j].h = 0.0
    cellDetails[i][j].g = 0.0
    cellDetails[i][j].parent_i = i
    cellDetails[i][j].parent_j = j
    openList = set()
    openList.add(setItem(0.0, i, j))

    foundDest = False
    while len(openList) > 0:
        p = openList.pop()
        i = p.i
        j = p.j
        closedList[i][j] = True
        # North
        if checkValid(i - 1, j):
            if isGoal(i - 1, j, goal):

                cellDetails[i - 1][j].parent_i = i
                cellDetails[i - 1][j].parent_j = j
                foundDest = True
                tracePath(cellDetails, goal)
                return ("we foun the goal")
            elif not (closedList[i - 1][j]) and \
                    checkBlock(matrix, i - 1, j):
                newG = cellDetails[i][j].g + 1.0
                newH = calculateHeuristic(i - 1, j, goal)
                newF = newG + newH
                if cellDetails[i - 1][j].f == float("inf") or \
                        cellDetails[i - 1][j].f > newF:
                    openList.add(setItem(newF, i - 1, j))

                    cellDetails[i - 1][j].f = newF
                    cellDetails[i - 1][j].g = newG
                    cellDetails[i - 1][j].h = newG
                    cellDetails[i - 1][j].parent_i = i
                    cellDetails[i - 1][j].parent_j = j
        #             End North
        #   South
        if checkValid(i + 1, j):
            if isGoal(i + 1, j, goal):
                cellDetails[i + 1][j].parent_i = i
                cellDetails[i + 1][j].parent_j = j
                tracePath(cellDetails, goal)
                foundDest = True
                return "we foun the goal"
            elif i <= 8 and not closedList[i + 1][j] and \
                    checkBlock(matrix, i + 1, j):
                newG = cellDetails[i][j].g + 1
                newH = calculateHeuristic(i + 1, j, goal)
                newF = newG + newH
                if cellDetails[i + 1][j].f == float("inf") or \
                        cellDetails[i + 1][j].f > newF:
                    openList.add(setItem(newF, i + 1, j))

                    cellDetails[i + 1][j].f = newF
                    cellDetails[i + 1][j].g = newG
                    cellDetails[i + 1][j].h = newG
                    cellDetails[i + 1][j].parent_i = i
                    cellDetails[i + 1][j].parent_j = j
            #           EndSouth

        #              East
        if checkValid(i, j + 1):
            if isGoal(i, j + 1, goal):
                cellDetails[i][j + 1].parent_i = i
                cellDetails[i][j + 1].parent_j = j
                foundDest = True
                tracePath(cellDetails, goal)
                return ("we foun the goal")
            elif not closedList[i][j + 1] and checkBlock(matrix, i, j + 1):
                newG = cellDetails[i][j].g + 1
                newH = calculateHeuristic(i, j + 1, goal)
                newF = newG + newH
                if cellDetails[i][j + 1].f == float("inf") or \
                        cellDetails[i][j + 1].f > newF:
                    openList.add(setItem(newF, i, j + 1))

                    cellDetails[i][j + 1].f = newF
                    cellDetails[i][j + 1].g = newG
                    cellDetails[i][j + 1].h = newG
                    cellDetails[i][j + 1].parent_i = i
                    cellDetails[i][j + 1].parent_j = j
        #             End East
        #   west
        if checkValid(i, j - 1):
            if isGoal(i, j - 1, goal):
                cellDetails[i][j - 1].parent_i = i
                cellDetails[i][j - 1].parent_j = j
                foundDest = True
                tracePath(cellDetails, goal)
                return "we foun the goal"
            elif not closedList[i][j - 1] and checkBlock(matrix, i, j - 1):

                newG = cellDetails[i][j].g + 1
                newH = calculateHeuristic(i, j - 1, goal)
                newF = newG + newH
                if cellDetails[i][j - 1].f == float("inf") or cellDetails[i][j - 1].f > newF:
                    openList.add(setItem(newF, i, j - 1))
                    cellDetails[i][j - 1].f = newF
                    cellDetails[i][j - 1].g = newG
                    cellDetails[i][j - 1].h = newG
                    cellDetails[i][j - 1].parent_i = i
                    cellDetails[i][j - 1].parent_j = j
            #             End west

    pass


ROW = 10
COL = 10
f = open('./matrix.txt')
matrix = []
for i in range(ROW):
    matrix.append(f.readline().rstrip().split(" "))
for i in range(ROW):
    for j in range(COL):
        if matrix[i][j] == 'G':
            goal = Cell(i, j)
        if matrix[i][j] == 'P':
            start = Cell(i, j)

print(aStar(matrix, start, goal))
