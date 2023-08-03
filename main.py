# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# class consists of rows, ok for dfs, row major stracture
def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


class Board:
    def __init__(self, size: int):
        self.size = size
        # if is_square(size):
        #    section_size=math.isqrt(size)
        # else:
        #    raise Exception('bad size of board!')

        self.rows = []
        self.columns = []
        self.sections = []
        for i in range(0, size):
            temp_row = Row(size, [])
            self.rows.append(temp_row)
            temp_column = Column(size, [])
            self.columns.append(temp_column)

            temp_section = Section(size, [])
            self.sections.append(temp_section)

        row_index = 0
        column_index = 0
        section_index = 0
        section_count1 = 0  # math.isqrt(size)
        section_count2 = 0  # size
        section_count3 = 0  # size *math.isqrt(size)
        for i in range(0, size * size):
            cell = Cell(-1)
            # for testing fill with i
            if (i + 1) % size != 0:
                self.rows[row_index].data_stracture.append(cell)
            else:
                self.rows[row_index].data_stracture.append(cell)
                row_index += 1
            column_index = i % size
            self.columns[column_index].data_stracture.append(cell)
            # section filling
            if section_count1 == math.isqrt(size):
                section_count1 = 0
                section_index += 1
            if section_count2 == size:
                section_count2 = 0
                section_index -= math.isqrt(size)
            if section_count3 == size * math.isqrt(size):
                section_count3 = 0
                section_index += math.isqrt(size)

            section_count1 += 1
            section_count2 += 1
            section_count3 += 1
            self.sections[section_index].data_stracture.append(cell)

    def fill_rows_ascending(self):
        i = 1
        for row in self.rows:
            for cel in row.get_data():
                cel.set(i)
                i += 1

    def solve_sudoku_row_major(self):
        # visited=0
        # to_visit=0
        row_index = 0
        col_index = 0

        while row_index < self.size:
            # self.rows[row_index].possible_vals=
            possible_vals = list(range(0, self.size + 1))
            row = self.rows[row_index].get_data()
            while col_index < self.size:
                pass

            row_index += 1

    def coherence_check(self):
        # sprawdz czy Cell jest dobrze wspoldzielony przez wiersze, kolumny, sekcje
        pass

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


class Validatable:
    def __init__(self, size: int, data_structure: list):  # nie da sie zrobic seta, xd , musi byc lista
        self.size = size
        self.data_stracture = data_structure

    def is_valid(self):
        raise NotImplementedError

    def get_data(self):
        return self.data_stracture


class Row(Validatable):
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)

    def __str__(self):
        return str(self.data_stracture)

    def is_valid(self):
        for i in range(0, self.size + 1):
            how_many = self.data_stracture.count(i)
            if how_many > 1:
                return False
        return True


class Section(Validatable):  # section to sekcja ktora jest wyprasowana(flatten)
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)

    def __str__(self):
        return str(self.data_stracture)

    def is_valid(self):
        for i in range(0, self.size + 1):
            how_many = self.data_stracture.count(i)
            if how_many > 1:
                return False
        return True


class Column(Validatable):
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)

    def __str__(self):
        return str(self.data_stracture)

    def is_valid(self):
        for i in range(0, self.size + 1):
            how_many = self.data_stracture.count(i)
            if how_many > 1:
                return False
        return True


class Cell:  # todo: Cell powinien miec wskazniki, na wiersz, kolumne i sekcje w jakiej jest, zeby przyspieszyc ulatwic wywolywanie is valid
    def __init__(self, value: int):
        self.value = value  # unknown=-1 else [0,size]
        # zeby zrobic decoupling mozna uzyc patternu observer ale nie jest tutaj potrzebny, bo nie potrzebuje
        # dowiazywac obserwatorów podczas runtime,
        #my_row
        #my_column
        #my_section

    def __str__(self):
        return '{}'.format(self.value)

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board(9)
    # board.print_rows_objects()
    board.print_rows_values()
    print(" ")
    board.print_columns_values()
    print(" ")
    board.print_sections_values()
    print(" ")
    board.fill_rows_ascending()
    ##################################################
    print("rows:")
    board.print_rows_values()
    print("columns:")
    board.print_columns_values()
    print("sections:")
    board.print_sections_values()
    print(" ")
