import pawn


class Board:
    def __init__(self) -> None:
        self.array = [[pawn.Pawn.EMPTY for _ in range(8)] for _ in range(8)]
        self.array[3][3] = pawn.Pawn.WHITE
        self.array[3][4] = pawn.Pawn.BLACK
        self.array[4][3] = pawn.Pawn.BLACK
        self.array[4][4] = pawn.Pawn.WHITE

    def is_move_valid(self, position: pawn.Position):
        return True

    def __add__(self, color, position):
        self.array[position.row][position.col] = color
        return self

    def __getitem__(self, index: tuple):
        i, j = index
        return self.array[i][j]

    def __getitem__(self, position: pawn.Position):
        i, j = position.row, position.col
        return self.array[i][j]

    def __setitem__(self, position: pawn.Position, color):
        self.array[position.row][position.col] = color

    def __iter__(self):
        for i, row in enumerate(self.array):
            for j, element in enumerate(row):
                yield (i, j, element)

    def check_can_play(self, color, position: pawn.Position):
        """
        if the player wants to place a pawn color at given position, checks if it is possible
        """
        allowed_position = False
        if self[position] != pawn.Pawn.EMPTY:
            return None
        opponent_color = color.opponent_color()
        good_neighbors = []
        good_direction = []
        list_of_changes = []
        for index in {
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        }:
            attempted_position = position + index
            if (
                attempted_position.valid_position()
                and self[attempted_position] == opponent_color
            ):
                # we filter the position shift that are on the board
                # we keep the neighbors that have a different color
                good_neighbors.append(attempted_position)
                good_direction.append(
                    index
                )  # direction to investigate, to see if this leads to a change of colors of pawn in that direction
        for direction in good_direction:
            # now we have directions with an opponent color, check if the opponent is framed by two pawns of you color
            for_change = self.check_imply_changing_colors(color, position, direction)
            if for_change:
                allowed_position = True
                filtered_direction, final_position = for_change
                list_of_changes.append(
                    (color, position, filtered_direction, final_position)
                )
                # attention si encore là -> buggggg
                # self.apply_changes(
                #     color, position, filtered_direction, final_position
                # )  # maybe just note the changes to be applied in lists
        return list_of_changes

    def check_imply_changing_colors(
        self, color, position: pawn.Position, direction: tuple
    ):
        """
        warning direction is a valid direction from check neighbors
        """
        opponent_color = color.opponent_color()

        attempted_position = position + direction
        while (
            attempted_position.valid_position()
            and self[attempted_position] == opponent_color
        ):
            attempted_position += direction
        if attempted_position.valid_position() and self[attempted_position] == color:
            return direction, attempted_position

        return None

    def apply_changes(
        self,
        color,
        position_initial: pawn.Position,
        direction: tuple,
        position_final: pawn.Position,
    ):
        next_position = position_initial + direction
        while next_position != position_final:
            self[next_position] = color
            next_position += direction

    def apply_list_of_changes(self, list_of_changes):
        for change in list_of_changes:
            color, position_initial, direction, position_final = change
            self.apply_changes(color, position_initial, direction, position_final)
        self[position_initial] = color

    def draw(self):
        print("    A  ", " B  ", " C  ", " D  ", " E  ", " F  ", " G  ", " H  ", sep="")
        for row in range(8):
            print("  ", "-" * 33, sep="")
            print(row + 1, "| ", end="")
            for col in range(8):
                if self.array[row][col] == pawn.Pawn.EMPTY:
                    print("  | ", end="")
                elif self.array[row][col] == pawn.Pawn.WHITE:
                    print("O | ", end="")
                elif self.array[row][col] == pawn.Pawn.BLACK:
                    print("X | ", end="")
                else:
                    print("? | ", end="")
            print("  ", " " * 33, sep="")
        print("  ", "-" * 33, sep="")


if __name__ == "__main__":
    board = Board()
    # board.check_neighbors(pawn.Pawn.BLACK, pawn.Position(3, 2))
    print(board.array)
    nb_black = 0
    nb_white = 0
    nb_empty = 0
    for row in range(8):
        for col in range(8):
            if board.array[row][col] == pawn.Pawn.BLACK:
                nb_black = nb_black + 1
            elif board.array[row][col] == pawn.Pawn.WHITE:
                nb_white = nb_white + 1
            elif board.array[row][col] == pawn.Pawn.EMPTY:
                nb_empty = nb_empty + 1
    print(nb_black, nb_white, nb_empty)
