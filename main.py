from Board import Board


if __name__ == '__main__':
    board = Board(9)
    solved = board.solve_sudoku_row_major()
    if solved:
        print("succcccccccccccccccces")
    else:
        print("failed")

    board.print_rows_values()
    print(" ")
    board.obscure_board(17)
    board.print_rows_values()
    ##################################################
    # board.fill_rows_ascending()
    # print("rows:")
    # board.print_rows_values()
    # board.print_rows_objects()
