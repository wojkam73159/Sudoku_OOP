from Validatable import Validatable


class Section(Validatable):

    def append_cell(self, cell):
        self.cells.append(cell)
        cell.set_section(self)
