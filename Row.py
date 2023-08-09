from Validatable import Validatable


class Row(Validatable):

    def append_cell(self, cell):
        self._cells.append(cell)
        cell.my_row = self
        # cell.my_row(self)

    def get_first_empty_cell_index(self):
        list_of_empty = list(filter(lambda x: x[1].value == 0, enumerate(self._cells)))
        if len(list_of_empty) == 0:
            return -1
        else:
            return list_of_empty[0][0]
