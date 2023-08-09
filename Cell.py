from Validatable import Validatable


class Cell:  # ma wskazniki, na wiersz, kolumne i sekcje w jakiej jest, zeby przyspieszyc
    # ulatwic wywolywanie is valid
    def __init__(self, value: int):
        self.value = value  # unknown=-1 else [0,size]
        # zeby zrobic decoupling mozna uzyc patternu observer ale nie jest tutaj potrzebny,
        # bo nie potrzebujeskomplikowanego mechanizmu zeby
        # tylko dodanie observera tylko zagmatwało by logikę
        # dowiazywac obserwatorów podczas runtime, wiec nie jestem pewien ze jest potrzebny
        self.my_row: Validatable = None
        self.my_column: Validatable = None
        self.my_section: Validatable = None

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_row(self, row: Validatable):
        self.my_row = row

    def set_column(self, column: Validatable):
        self.my_column = column

    def set_section(self, section: Validatable):
        self.my_section = section

    def get_row(self):
        return self.my_row

    def get_column(self):
        return self.my_column

    def get_section(self):
        return self.my_section

    def validate(self):  # tutaj moze byc visitor moze byc tez parralel, albo async await
        return all(x.is_valid() for x in (self.my_row, self.my_column, self.my_section))
