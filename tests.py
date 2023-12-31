import math
import unittest

from Board import Board


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(9, 1, 1)

    def test_check_cells_being_shared_properly_between_rows_columns(self):
        # how to write test to test class private methods

        # test rows and columns correct

        for i in range(0, self.board.size):
            for j in range(0, self.board.size):
                self.assertEqual(self.board._rows[i]._cells[j], self.board._columns[j]._cells[i])

        # Board.

    def test_check_cells_being_shared_properly_betweeen_section_and_rest(self):
        new_rows = []
        for i in range(0, self.board.size):
            new_rows.append([])

        section_index1 = 0
        section_count1 = 0
        section_count2 = 0
        section_count3 = 0

        section2_count1 = 0
        section_index2 = 0
        for i in range(0, self.board.size * self.board.size):
            if section_count1 == math.isqrt(self.board.size):
                section_count1 = 0
                section_index1 += 1
            if section_count2 == self.board.size:
                section_count2 = 0
                section_index1 -= math.isqrt(self.board.size)
            if section_count3 == self.board.size * math.isqrt(self.board.size):
                section_count3 = 0
                section_index1 += math.isqrt(self.board.size)
            section_count1 += 1
            section_count2 += 1
            section_count3 += 1
            add = 0
            if (i % math.isqrt(self.board.size)) == 0:
                section_index2 = 0
                if not (i == 0):
                    section2_count1 += 1
                add = int(section2_count1 / (math.isqrt(self.board.size)))
                add = add % int((math.isqrt(self.board.size)))
            section_index2 += int((add * math.isqrt(self.board.size)))

            row = int(i / self.board.size)
            column = i % self.board.size
            self.assertEqual(self.board._data[row][column],
                             self.board._sections[section_index1]._cells[section_index2])
            section_index2 += 1
            section_index2 = section_index2 % self.board.size

    def test_board4(self):
        board = Board(4, 1, 1)
        solved = board.solve_sudoku_row_major()
        if solved:
            print("succcccccccccccccccces")
        else:
            print("failed")
        board.print_rows()

    def test_board9(self):
        board = Board(9, 1, 1)
        solved = board.solve_sudoku_row_major()
        if solved:
            print("succcccccccccccccccces")
        else:
            print("failed")
        board.print_rows()

    def test_board16(self):
        board = Board(16, 1, 1)
        solved = board.solve_sudoku_row_major()
        if solved:
            print("succcccccccccccccccces")
        else:
            print("failed")
        board.print_rows()

    @unittest.SkipTest
    def test_board25(self):
        board = Board(25, 1, 1)
        solved = board.solve_sudoku_row_major()
        if solved:
            print("succcccccccccccccccces")
        else:
            print("failed")
        board.print_rows()


if __name__ == '__main__':
    unittest.main()
