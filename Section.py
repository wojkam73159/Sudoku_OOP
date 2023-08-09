from Validatable import Validatable


class Section(Validatable):

    def append_cell(self, cell):
        self._cells.append(cell)
        cell.my_section = self
