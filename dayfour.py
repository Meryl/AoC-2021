class Board:
    def __init__(self, boardNum, input):
        self.boardNum = None
        self.numbers = [[], [], [], [], []]
        self.drawn = 0
        self.marked = {
            "rows": [0,0,0,0,0],
            "cols": [0,0,0,0,0],
        }

        self.boardNum = boardNum
        lines = [line.strip() for line in input.split("\n")]
        self.parse(lines)

    def parse(self, lines):
        for i, line in enumerate(lines):
            self.numbers[i] = line.strip().split()

    def mark(self, number):
        for row, rowData in enumerate(self.numbers):
            for col, nr in enumerate(rowData):
                if number == nr:
                    self.drawn += int(nr)
                    self.marked["cols"][col] += 1
                    self.marked["rows"][row] += 1

    def check(self):
        for row in self.marked["rows"]:
            if row > 4:
                return True

        for col in self.marked["cols"]:
            if col > 4:
                return True
        return False

    def print(self):
        for row in self.numbers:
            for col, nr in enumerate(row):
                print(str(nr).rjust(2), end = ' ')
            print()
        print()

    def getScore(self, number):
        score = 0
        for row in self.numbers:
            for col in row:
                score += int(col)

        score -= self.drawn
            
        return score * int(number)

def parseInput():
    with open('input/dayfour.txt', 'r') as inputFile:
        draw = []
        boards = []
        inputParts = inputFile.read().split("\n\n")

        for i, inputPart in enumerate(inputParts):
            if i == 0:
                for number in inputPart.split(","):
                    draw.append(number)
            else:
                board = Board(i, inputPart.strip())
                boards.append(board)

    return draw, boards

def partOne():
    draw, boards = parseInput()

    for number in draw:
        for i, board in enumerate(boards):
            board.mark(number)
            if board.check():
                score = board.getScore(number)
                print("Board {} won, score was {}".format(board.boardNum, score))
                break
        else:
            continue
        break

def partTwo():
    draw, boards = parseInput()

    lastboard = False
    lastscore = 0

    for number in draw:
        for i, board in enumerate(boards):
            if not board.check():
                board.mark(number)
                if board.check():
                    lastboard = board.boardNum
                    lastscore = board.getScore(number)
        else:
            continue
        break

    print("Board {} won last, score was {}".format(lastboard, lastscore))

partOne()
partTwo()