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

    def check_neighbors_and_apply(self, color, position: pawn.Position):
        """
        if the player wants to place a pawn color at given position, checks if it is possible
        """
        opponent_color = color.opponent_color()
        good_neighbors = []
        good_direction = []
        will_make_oppponent_pawn_flip = False
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
                will_make_oppponent_pawn_flip = True
                filtered_direction, final_position = for_change
                self.apply_changes(
                    color, position, filtered_direction, final_position
                )  # maybe just note the changes to be applied in lists
        return will_make_oppponent_pawn_flip

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
            and board[attempted_position] == opponent_color
        ):
            attempted_position += direction
        if attempted_position.valid_position() and board[attempted_position] == color:
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
            board[next_position] = color
            next_position += direction

    def draw(self):
        print(self.array)


if __name__ == "__main__":
    board = Board()
    board.check_neighbors_and_apply(pawn.Pawn.BLACK, pawn.Position(3, 2))
