from Validatable import Validatable


class Column(Validatable):

    def append_cell(self, cell):
        self.cells.append(cell)
        cell.set_column(self)
