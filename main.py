# This is a sample Python script.
import math
import random


# class consists of rows, ok for dfs, row major structure
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
        self.fill_with_minus_ones()
        cell_digit_pair = self.generate_17_different_cells_8_different_digits()
        for cell, digit in cell_digit_pair:
            row = int(cell / size)
            index = cell % size
            self.rows[row].get_data_at(index).set_value(digit)

    def fill_rows_ascending(self):
        i = 1
        for row in self.rows:
            for cel in row.get_data():
                cel.set_value(i)
                i += 1

    def fill_with_minus_ones(self):
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
            cell = Cell(-1)
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

    def generate_17_different_cells_8_different_digits(
            self):  # 0.02%chance of impossible combination according to internet
        random_cells = set()
        possible_cells = list(range(0, self.size * self.size))

        while len(random_cells) != 17:
            test_elem = random.choices(possible_cells)
            if test_elem[0] not in random_cells:
                random_cells.add(test_elem[0])
        # 17 different cells chosen
        # now give them 8 different digits range 1:9
        res = []
        for cell_number in random_cells:
            res.append([cell_number, 1])

        possible_digits = list(range(1, self.size + 1))
        count_distinct_numbers = set()
        res_index = 0

        while len(count_distinct_numbers) < 8:
            rand_digit = random.choice(possible_digits)
            res[res_index][1] = rand_digit
            count_distinct_numbers.add(rand_digit)
            res_index = (res_index + 1) % 17

        return res

    # zamien to na zwykly solver
    def solve_sudoku_row_major(self):
        # visited=0
        # to_visit=0
        row_index = 0
        col_index = 0
        for row in self.rows:
            row.possible_vals = list(range(0, self.size + 1))

        while row_index < self.size:
            row = self.rows[row_index]

            while col_index < self.size:

                current_cell = row.get_data_at(col_index)
                # solve based on random generation
                rand_index = random.choice(range(0,
                                                 len(row.possible_vals)))  # random index from possible values // get rid of possible values, solve based on random generation
                choice = row.get_data_at(rand_index)
                current_cell.set_value(choice)

                if current_cell.validate():
                    col_index += 1
                else:
                    pass  # backtrack

            row_index += 1

    def __backtrack(self, row_index: int, col_index: int, depth: int):
        pass

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
    def __init__(self, size: int, data_structure: list):  # nie da sie zrobic seta , musi byc lista
        self.size = size
        self.data_structure = data_structure

    def is_valid(self):
        raise NotImplementedError

    def get_data(self):
        return self.data_structure

    def get_data_at(self, index: int):
        return self.data_structure[index]


class Row(Validatable):
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)
        self.possible_vals = None

    def __str__(self):
        return str(self.data_structure)

    def is_valid(self):
        for i in range(0, self.size + 1):
            how_many = self.data_structure.count(i)
            if how_many > 1:
                return False
        return True


class Section(Validatable):  # section to sekcja ktora jest wyprasowana(flatten)
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)

    def __str__(self):
        return str(self.data_structure)

    def is_valid(self):
        for i in range(0, self.size + 1):
            how_many = self.data_structure.count(i)
            if how_many > 1:
                return False
        return True


class Column(Validatable):
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)

    def __str__(self):
        return str(self.data_structure)

    def is_valid(self):
        for i in range(0, self.size + 1):
            how_many = self.data_structure.count(i)
            if how_many > 1:
                return False
        return True


class Cell:  # todo: Cell powinien miec wskazniki, na wiersz, kolumne i sekcje w jakiej jest, zeby przyspieszyc
    # ulatwic wywolywanie is valid
    def __init__(self, value: int, ):
        self.value = value  # unknown=-1 else [0,size]
        # zeby zrobic decoupling mozna uzyc patternu observer ale nie jest tutaj potrzebny, bo nie potrzebuje
        # dowiazywac obserwatorów podczas runtime,
        self.my_row = None
        self.my_column = None
        self.my_section = None

    def __str__(self):
        return '{}'.format(self.value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_row(self, row: Row):
        self.my_row = row

    def set_column(self, column: Column):
        self.my_column = column

    def set_section(self, section: Section):
        self.my_section = section

    def get_row(self):
        return self.my_row

    def get_column(self):
        return self.my_column

    def get_section(self):
        return self.my_section

    def validate(self):  # tutaj moze byc visitor moze byc tez parralel, albo async await
        if self.my_row.is_valid():
            return True
        elif self.my_column.is_valid():
            return True
        elif self.my_section.is_valid():
            return True
        else:
            return False


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
