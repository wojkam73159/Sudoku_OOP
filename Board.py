import random
from typing import List

from Cell import Cell
from Row import Row
from Column import Column
from Section import Section
import math

from Validatable import Validatable


class Board:
    def __init__(self, size: int, start_cells: int, different_nums_for_start_cells: int):
        self.size = size

        # try generate valid board with high possibility of success
        failed = True
        while failed:
            self._data: List[List[Cell]] = []
            self._rows: List[Row] = []
            self._columns: List[Column] = []
            self._sections: List[Section] = []
            self.__fill_with_zeros()

            cell_digit_pair = self.__generate_X_different_cells_Y_different_digits(start_cells,
                                                                                   different_nums_for_start_cells)
            for cell_coordinates_flat, digit in cell_digit_pair:
                row = int(cell_coordinates_flat / size)
                index = cell_coordinates_flat % size
                cell = self._data[row][index]
                cell.value = digit
                if cell.validate():
                    failed = False
                else:
                    failed = True
                    break
        self.print_rows()

    def _fill_rows_ascending(self):
        i = 1
        for row in self._rows:
            for cel in row.cells():
                cel.value = i
                i += 1

    def __fill_with_zeros(self):
        for i in range(0, self.size):
            self._data.append([])
            self._rows.append(Row(self.size))
            self._columns.append(Column(self.size))
            self._sections.append(Section(self.size))

        row_index = 0
        column_index = 0
        section_index = 0
        finished_one_row_in_section = 0
        finished_one_row_in_sudoku = 0
        finished_one_row_of_sections = 0
        for i in range(0, self.size * self.size):
            cell = Cell(0)
            self._rows[row_index].append_cell(cell)
            self._data[row_index].append(cell)
            if (i + 1) % self.size == 0:
                row_index += 1
            column_index = i % self.size
            self._columns[column_index].append_cell(cell)

            # section filling
            self._sections[section_index].append_cell(cell)
            finished_one_row_in_section += 1
            finished_one_row_in_sudoku += 1
            finished_one_row_of_sections += 1
            if finished_one_row_in_section == math.isqrt(self.size):
                finished_one_row_in_section = 0
                section_index += 1
            if finished_one_row_in_sudoku == self.size:
                finished_one_row_in_sudoku = 0
                section_index -= math.isqrt(self.size)
            if finished_one_row_of_sections == self.size * math.isqrt(self.size):
                finished_one_row_of_sections = 0
                section_index += math.isqrt(self.size)

    def __generate_X_different_cells_Y_different_digits(
            self, how_many_numbers,
            how_many_different_digits):
        # 17 numbers 8 digits sugested by internet 0.02%chance of impossible
        # combination according to internet
        random_cells = self.__generate_X_different_cells(how_many_numbers)
        # how_many_numbers different cells chosen
        # now give them how_many_different_digits different digits range 0:8
        res = []
        for cell_number in random_cells:
            res.append([cell_number, 1])

        possible_digits = list(range(1, self.size + 1))
        count_distinct_numbers = set()
        res_index = 0

        while len(count_distinct_numbers) < how_many_different_digits:
            rand_digit = random.choice(possible_digits)
            res[res_index][1] = rand_digit
            count_distinct_numbers.add(rand_digit)
            res_index = (res_index + 1) % how_many_numbers

        return res

    def __find_empty_location(self):
        i = 0
        for row in self._rows:
            found_elem = row.get_first_empty_cell_index()
            if found_elem == -1:
                i += 1
            else:
                return True, i, found_elem
        return False, 0, 0

    def solve_sudoku_row_major(self):

        # If there is no unassigned
        # location, we are done
        is_found, row, col = self.__find_empty_location()
        if not is_found:
            return True
        cell = self._data[row][col]

        for num in range(1, self.size + 1):
            cell.value = num  # make assumption
            if cell.validate():
                if self.solve_sudoku_row_major():
                    return True
            else:
                cell.value = 0
        return False

    @staticmethod
    def _print_cells(structure: List[Validatable]):
        for elem in structure:
            print(elem)

    def print_rows(self):
        self._print_cells(self._rows)

    def print_columns(self):
        self._print_cells(self._columns)

    def print_sections(self):
        for sec in self._sections:
            res = map(str, sec.cells)
            print(list(res))

    def __str__(self):
        pass

    def __generate_X_different_cells(self, how_many_numbers):
        random_cells = set()
        possible_cells = list(range(0, self.size * self.size))

        while len(random_cells) != how_many_numbers:
            test_elem = random.choices(possible_cells)
            if test_elem[0] not in random_cells:
                random_cells.add(test_elem[0])
        return list(random_cells)

    def obscure_board(self, number_of_obscured_cells):

        indexes = self.__generate_X_different_cells(number_of_obscured_cells)
        for cell_coordinates_flat in indexes:
            row = int(cell_coordinates_flat / self.size)
            index = cell_coordinates_flat % self.size
            cell = self._data[row][index]
            cell.value = 'X'
