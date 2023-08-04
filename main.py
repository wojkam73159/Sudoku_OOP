# This is a sample Python script.
import math
import random
from Cell import Cell
from Board import Board
from Row import Row
from Column import Column
from Section import Section


# class consists of rows, ok for dfs, row major structure
def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(9)
    solved = board.solve_sudoku_row_major()
    if solved:
        print("succcccccccccccccccces")
    else:
        print("failed")

    # board.print_rows_objects()
    board.print_rows_values()
    print(" ")
    # board.print_columns_values()
    # print(" ")
    # board.print_sections_values()
    # print(" ")
    # board.fill_rows_ascending()
    ##################################################
    # print("rows:")
    # board.print_rows_values()
    # print("columns:")
    # board.print_columns_values()
    # print("sections:")
    # board.print_sections_values()
    # print(" ")
