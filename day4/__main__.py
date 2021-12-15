filename = 'data.txt'

class BingoBoard:
    def __init__(self, rows):
        self.rows = rows
        self.columns = list(map(list, zip(*rows))) # Transpose rows

    def check_board(self, drawn):
        return self.__check_rows(drawn) or self.__check_columns(drawn)

    def get_score(self, drawn):
        sum = 0

        for row in self.rows:
            for value in row:
                if value not in drawn:
                    sum += value

        return sum * drawn[-1]


    def __check_columns(self, drawn):
        for column in self.columns:
            if self.__check_column(column, drawn) is True:
                return True
        return False

    def __check_column(self, column, drawn):
        return self.__check_row(column, drawn)

    def __check_rows(self, drawn):
        for row in self.rows:
            if self.__check_row(row, drawn) is True:
                return True
        return False

    def __check_row(self, row: list, drawn):
        for value in row:
            if value not in drawn:
                return False
        return True


def string_rows_to_int_lists(rows):
    result = []

    for row in rows:
        int_row = []
        index = 0

        while(index < len(row)):
            try:
                number = int(row[index:index+2])
                int_row.append(number)
            except:
                number = int(row[index+1])
                int_row.append(number)
            index += 3
        result.append(int_row)
    return result


def create_boards_from_file(lines):
    boards = []
    index = 0

    while(index < len(lines)):
        rows = string_rows_to_int_lists(lines[index:index+5])
        board = BingoBoard(rows)
        boards.append(board)
        index += 6

    return boards


def get_score_of_winning_board(boards, instructions):
    for i in range(len(instructions)):
        for board in boards:
            result = board.check_board(instructions[0:i+1])

            if result is True:
                score = board.get_score(instructions[0:i+1])
                return score


with open(filename) as file:
    lines = file.readlines()
    instructions = list(map(int, lines[0].split(',')))
    boards = create_boards_from_file(lines[2:])
    score = get_score_of_winning_board(boards, instructions)
    print(score)


