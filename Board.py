import random

from Row import Row
from Column import Column
from Section import Section
from Cell import Cell
import math


class Board:
    def __init__(self, size: int):
        self.size = size
        # if is_square(size):
        #    section_size=math.isqrt(size)
        # else:
        #    raise Exception('bad size of board!')

        # try generate valid board with high possibility of success
        failed = True
        while failed:

            self.rows = []
            self.columns = []
            self.sections = []
            self.__fill_with_zeros()

            cell_digit_pair = self.__generate_X_different_cells_Y_different_digits(5, 4)
            for cell_coordinates_flat, digit in cell_digit_pair:
                row = int(cell_coordinates_flat / size)
                index = cell_coordinates_flat % size
                cell_actual = self.rows[row].get_data_at(index)
                cell_actual.set_value(digit)
            self.print_rows_values()
            print("failed to generate")
            for row in self.rows:
                for cell in row.get_data():
                    if cell.validate():
                        failed = False
                        continue
                    else:
                        failed = True
                        break

    def fill_rows_ascending(self):
        i = 1
        for row in self.rows:
            for cel in row.get_data():
                cel.set_value(i)
                i += 1

    def __fill_with_zeros(self):
        for i in range(0, self.size):
            temp_row = Row(self.size, [])
            self.rows.append(temp_row)
            temp_column = Column(self.size, [])
            self.columns.append(temp_column)

            temp_section = Section(self.size, [])
            self.sections.append(temp_section)

        row_index = 0
        column_index = 0
        section_index = 0
        section_count1 = 0  # math.isqrt(size)
        section_count2 = 0  # size
        section_count3 = 0  # size *math.isqrt(size)
        for i in range(0, self.size * self.size):
            cell = Cell(0)
            # for testing fill with i
            if (i + 1) % self.size != 0:
                cell.set_row(self.rows[row_index])
                self.rows[row_index].data_structure.append(cell)
            else:
                cell.set_row(self.rows[row_index])
                self.rows[row_index].data_structure.append(cell)
                row_index += 1
            column_index = i % self.size
            self.columns[column_index].data_structure.append(cell)
            cell.set_column(self.columns[column_index])
            # section filling
            if section_count1 == math.isqrt(self.size):
                section_count1 = 0
                section_index += 1
            if section_count2 == self.size:
                section_count2 = 0
                section_index -= math.isqrt(self.size)
            if section_count3 == self.size * math.isqrt(self.size):
                section_count3 = 0
                section_index += math.isqrt(self.size)

            section_count1 += 1
            section_count2 += 1
            section_count3 += 1
            self.sections[section_index].data_structure.append(cell)
            cell.set_section(self.sections[section_index])

    def __generate_X_different_cells_Y_different_digits(
            self, how_many_numbers,
            how_many_different_digits):  # 17 numbers 8 digits sugested by internet 0.02%chance of impossible combination according to internet
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

    def __find_empty_location(
            self):  # przekazywanie argumentow do funkcji w naglowku? czy lepiej zwracac tuple i rozpakowywac
        i = 0
        for row in self.rows:  # ask question how to hint that there is type Row here
            found_list = list(filter(lambda x: x[1].get_value() == 0, enumerate(row.get_data())))
            if len(found_list) == 0:
                i += 1
                continue
            else:  # len(found_list) > 0:
                return True, i, found_list[0][0]

        return False, 0, 0

    def solve_sudoku_row_major(self):

        # If there is no unassigned
        # location, we are done
        is_found, row, col = self.__find_empty_location()
        if not is_found:
            return True

        cell = self.rows[row].get_data_at(col)
        # ciezkie wywolywanie tego w pythonie z duck typingiem i bez type hint , da sie to jakos ulatwic?

        for num in range(1, self.size + 1):

            cell.set_value(num)  # make assumption

            self.print_rows_values()
            print(" ")

            if cell.validate():
                if self.solve_sudoku_row_major():
                    return True
            else:
                cell.set_value(0)
        return False

    def print_rows_values(self):
        for row in self.rows:
            # print(row)
            res = map(str, row.get_data())
            print(list(res))

    def print_columns_values(self):
        for col in self.columns:
            res = map(str, col.get_data())
            print(list(res))

    def print_sections_values(self):
        for sec in self.sections:
            res = map(str, sec.get_data())
            print(list(res))

    def print_rows_objects(self):
        for row in self.rows:
            print(row)

    def print_columns_objects(self):
        for col in self.columns:
            res = map(str, col.get_data())
            print(list(res))

    def print_sections_objects(self):
        for sec in self.sections:
            res = map(str, sec.get_data())
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
            cell=self.rows[row].get_data_at(index)
            cell.set_value('X')

