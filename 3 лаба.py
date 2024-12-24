class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Инициализируем через свойство

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()}, Страниц: {self.pages}"


class AudioBook(Book):
    """ Класс для аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Инициализируем через свойство

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = float(value)

    def __str__(self) -> str:
        return f"{super().__str__()}, Продолжительность: {self.duration:.2f} часов"


# Пример использования классов
if __name__ == "__main__":
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("Гарри Поттер и философский камень", "Джоан Роулинг", 8.5)

    print(paper_book)
    print(audio_book)

    print(repr(paper_book))
    print(repr(audio_book))
