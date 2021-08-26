from abc import ABC, abstractmethod

# Aggregate
class Menu(ABC):
    @abstractmethod
    def create_iterator(self):
        raise NotImplementedError


# Iterator
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        raise NotImplementedError

    @abstractmethod
    def next(self):
        raise NotImplementedError


# Concrete aggregate
class DinerMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.menu_items = ["Beef Jerky", "Hamburgers", "Fish n' Chips"]

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)


# Concrete iterator
class DinerMenuIterator(Iterator):
    def __init__(self, menu_items) -> None:
        super().__init__()
        self.position = 0
        self.menu_items = menu_items

    def next(self):
        self.position += 1
        return self.menu_items[self.position - 1]

    def has_next(self):
        return self.position < len(self.menu_items)


class Cafe:
    def __init__(self, diner_menu) -> None:
        self.diner_menu = diner_menu

    def print_menu(self, iterator: Iterator):
        while iterator.has_next():
            print(iterator.next())


def main():
    diner_menu = DinerMenu()
    diner_menu_iterator = diner_menu.create_iterator()
    cafe = Cafe(diner_menu)
    cafe.print_menu(diner_menu_iterator)


if __name__ == "__main__":
    main()