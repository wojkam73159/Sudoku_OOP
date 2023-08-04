from Validatable import Validatable


class Section(Validatable):  # section to sekcja ktora jest wyprasowana(flatten)
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)

    def __str__(self):
        return str(self.data_structure)


