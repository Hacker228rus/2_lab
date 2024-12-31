class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Конструктор для инициализации атрибутов транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.__brand = brand  # Инкапсуляция, чтобы предотвратить прямое изменение марки
        self.__model = model  # Инкапсуляция, чтобы предотвратить прямое изменение модели
        self.__year = year    # Инкапсуляция, чтобы предотвратить прямое изменение года выпуска

    def get_info(self) -> str:
        """
        Получить информацию о транспортном средстве.

        :return: Строка с информацией о транспортном средстве.
        """
        return f"{self.__brand} {self.__model}, {self.__year}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с информацией о транспортном средстве.
        """
        return self.get_info()

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Строка с информацией о транспортном средстве.
        """
        return f"Vehicle(brand='{self.__brand}', model='{self.__model}', year={self.__year})"


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Конструктор для инициализации атрибутов легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self._Vehicle__year = None
        self._Vehicle__model = None
        self._Vehicle__brand = None
        self.__doors = doors  # Инкапсуляция, чтобы предотвратить прямое изменение количества дверей

    def get_info(self) -> str:
        """
        Получить информацию о легковом автомобиле.

        :return: Строка с информацией о легковом автомобиле.
        """
        return f"{super().get_info()}, Doors: {self.__doors}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта легкового автомобиля.

        :return: Строка с информацией о легковом автомобиле.
        """
        return f"Car: {self.get_info()}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта легкового автомобиля.

        :return: Строка с информацией о легковом автомобиле.
        """
        return (f"Car(brand='{self._Vehicle__brand}', model='{self._Vehicle__model}', "
                f"year={self._Vehicle__year}, doors={self.__doors})")

if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2020, 4)
    print(my_car)  # Выводит: Car: Toyota Camry, 2020, Doors: 4
    print(repr(my_car))  # Выводит: Car(brand='Toyota', model='Camry', year=2020, doors=4)
