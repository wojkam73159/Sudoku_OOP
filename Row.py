from Validatable import Validatable


class Row(Validatable):
    def __init__(self, size, data_structure):
        super().__init__(size, data_structure)
        self.possible_vals = None

    def __str__(self):
        return str(self.data_structure)


'''    def is_valid(self):
        for i in range(0, self.size ):
            how_many = self.data_structure.count(i)
            if how_many > 1:
                return False
        return True'''
