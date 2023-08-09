from Validatable import Validatable


class Cell:  # ma wskazniki, na wiersz, kolumne i sekcje w jakiej jest, zeby przyspieszyc
    # ulatwic wywolywanie is valid
    def __init__(self, value: int):
        self._value = value  # unknown=-1 else [0,size]
        # zeby zrobic decoupling mozna uzyc patternu observer ale nie jest tutaj potrzebny,
        # bo nie potrzebujeskomplikowanego mechanizmu zeby
        # tylko dodanie observera tylko zagmatwało by logikę
        # dowiazywac obserwatorów podczas runtime, wiec nie jestem pewien ze jest potrzebny
        self._my_row: Validatable = None
        self._my_column: Validatable = None
        self._my_section: Validatable = None

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def my_row(self):
        return self._my_row

    @my_row.setter
    def my_row(self, row: Validatable):
        self._my_row = row

    @property
    def my_column(self):
        return self._my_column

    @my_column.setter
    def my_column(self, column: Validatable):
        self._my_column = column

    @property
    def my_section(self):
        return self._my_section

    @my_section.setter
    def my_section(self, section: Validatable):
        self._my_section = section

    def validate(self):
        return all(x.is_valid() for x in (self._my_row, self._my_column, self._my_section))
