class Validatable:
    def __init__(self, size: int, data_structure: list):  # nie da sie zrobic seta , musi byc lista
        self.size = size
        self.data_structure = data_structure

    def get_data(self):
        return self.data_structure

    def get_data_at(self, index: int):
        return self.data_structure[index]

    def is_valid(self):  # todo check
        #
        # len(filter(lambda y: y > 2, self.data_structure))
        section_numbers = list(map(lambda y: y.get_value(), self.data_structure))
        dup_size = len(list(filter(lambda y: section_numbers.count(y) > 1, list(range(1, self.size + 1)))))
        if dup_size > 0:
            return False
        else:
            return True
        # for i in range(0, self.size ):
        #    how_many = self.data_structure.count(i)
        #    if how_many > 1:
        #        return False
        # return True

    # def is_valid(self):
    #    raise NotImplementedError
