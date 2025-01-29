# TODO: Подробно описать три произвольных класса


class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги (строка).
        :param author: Автор книги (строка).
        :param pages: Количество страниц (целое число, больше 0).

        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0.")

        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self) -> str:
        """
        Получить краткое содержание книги.

        :return: Строка с названием и автором книги.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_summary()
        '1984 by George Orwell'
        """
        return f"{self.title} by {self.author}"

    def read_pages(self, pages_read: int) -> str:
        """
        Прочитать указанное количество страниц.

        :param pages_read: Количество страниц для чтения (целое число, больше 0).

        :raises ValueError: Если pages_read меньше или равно 0.

        :return: Строка с сообщением о прочитанных страницах.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_pages(50)
        'Вы прочитали 50 страниц из 328.'
        """
        if pages_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть больше 0.")

        return f"Вы прочитали {pages_read} страниц из {self.pages}."


class Car:
    """Класс, описывающий автомобиль."""

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация автомобиля.

        :param make: Производитель автомобиля (строка).
        :param model: Модель автомобиля (строка).
        :param year: Год выпуска (целое число, больше или равно 1886).

        :raises ValueError: Если год выпуска меньше 1886.
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")

        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запустить двигатель автомобиля.

        :return: Строка с сообщением о запуске двигателя.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.start_engine()
        'Двигатель Toyota Corolla запущен.'
        """
        return f"Двигатель {self.make} {self.model} запущен."

    def description(self, include_year: bool = True) -> str:
        """
        Получить описание автомобиля.

        :param include_year: Указывать год выпуска в описании (по умолчанию True).

        :return: Строка с описанием автомобиля.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.description()
        'Toyota Corolla (2020)'
        >>> car.description(include_year=False)
        'Toyota Corolla'
        """
        if include_year:
            return f"{self.make} {self.model} ({self.year})"
        return f"{self.make} {self.model}"


class Tree:
    """Класс, описывающий дерево."""

    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация дерева.

        :param species: Вид дерева (строка).
        :param height: Высота дерева (число, больше 0).
        :param age: Возраст дерева (целое число, неотрицательное).

        :raises ValueError: Если высота меньше или равна 0 или возраст отрицательный.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, additional_height: float) -> None:
        """
        Увеличить высоту дерева.

        :param additional_height: Дополнительная высота (число, больше 0).

        :raises ValueError: Если дополнительная высота меньше или равна 0.

        >>> tree = Tree("Oak", 5.0, 5)
        >>> tree.grow(1.5)
        >>> tree.height
        6.5
        """
        if additional_height <= 0:
            raise ValueError("Дополнительная высота должна быть больше 0.")

        self.height += additional_height

    def age_description(self) -> str:
        """
        Получить описание возраста дерева.

        :return: Строка с информацией о возрасте дерева.

        >>> tree = Tree("Oak", 5.0, 5)
        >>> tree.age_description()
        'Это дерево вида Oak, возрастом 5 лет.'
        """
        return f"Это дерево вида {self.species}, возрастом {self.age} лет."

    def change_age(self, years: int) -> None:
        """
        Изменить возраст дерева.

        :param years: Количество лет для изменения возраста (целое число).

        :raises ValueError: Если years отрицательное.

        >>> tree = Tree("Oak", 5.0, 5)
        >>> tree.change_age(3)
        >>> tree.age
        8
        """
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")

        self.age += years
