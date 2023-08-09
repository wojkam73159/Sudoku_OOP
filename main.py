from Board import Board

if __name__ == '__main__':
    board = Board(16, 1, 1)
    solved = board.solve_sudoku_row_major()
    if solved:
        print("succcccccccccccccccces")
    else:
        print("failed")

    board.print_rows()
    print(" ")
    board.obscure_board(1)
