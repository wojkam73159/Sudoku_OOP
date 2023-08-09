from abc import abstractmethod


class Validatable:
    def __init__(self, size: int):
        self._size = size
        self._cells = []

    @property
    def cells(self):
        return self._cells

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self._size = value

    #@abstractmethod
    #def append_cell(self, cell):
    #    pass

    # def get_data_at(self, index: int):
    #    return self._cells[index]

    def is_valid(self):
        section_numbers = list(map(lambda y: y.value, self._cells))
        dup_size = len(list(filter(lambda y: section_numbers.count(y) > 1, list(range(1, self._size + 1)))))
        if dup_size > 0:
            return False
        else:
            return True

    def __str__(self):
        return ", ".join(map(str, self._cells))
