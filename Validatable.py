class Validatable:
    def __init__(self, size: int):
        self.size = size
        self.cells = []

    def get_data(self):
        return self.cells

    def set_data(self, cells):
        self.cells = cells

    def append_cell(self, cell):  # moja klasa to obudowa struktury danych jakiejs
        # wiec powinien byc getter i setter do nich
        # usage w klasie board
        self.cells.append(cell)

    def get_data_at(self, index: int):
        return self.cells[index]

    def is_valid(self):
        section_numbers = list(map(lambda y: y.get_value(), self.cells))
        dup_size = len(list(filter(lambda y: section_numbers.count(y) > 1, list(range(1, self.size + 1)))))
        if dup_size > 0:
            return False
        else:
            return True

    def __str__(self):
        return ", ".join(map(str, self.cells))
