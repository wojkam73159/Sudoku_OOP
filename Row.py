from Validatable import Validatable


class Row(Validatable):

    def append_cell(self, cell):
        self.cells.append(cell)
        cell.set_row(self)

    def get_first_empty_cell_index(self):
        list_of_empty = list(filter(lambda x: x[1].get_value() == 0, enumerate(self.cells)))
        if len(list_of_empty) == 0:
            return -1
        else:  # len(found_list) > 0:
            return list_of_empty[0][0]
