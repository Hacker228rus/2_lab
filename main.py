from task_1 import Book, Car, Tree # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.
    book = Book("Преступление  и наказание", "Достоевский", 290)
    car = Car("Renault", "Logan", 2015)
    tree = Tree("Береза", 32.5, 80)

    try:
        # Вызываем метод read_chapter с некорректным количеством страниц
        bad_book = book  # Больше чем предполагается страниц по умолчанию
    except ValueError as e:
        print(f"Ошибка при чтении главы: {e}")

    try:
        bad_car = Car("Ford", "Mustang", 2025)  # Год в будущем
    except ValueError as e:
        print(f"Ошибка: неправильные данные")


    try:
        bad_tree = Tree("Дуб", -1, 70)  # Отрицательная высота
    except ValueError as e:
        print(f"Ошибка: неправильные данные")
