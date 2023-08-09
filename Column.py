from Validatable import Validatable


class Column(Validatable):

    def append_cell(self, cell):
        self._cells.append(cell)
        cell.my_column = self
