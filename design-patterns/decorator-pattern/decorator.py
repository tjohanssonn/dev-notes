from abc import ABC, abstractmethod


# Superclass to be used by conrete pizza classes and decorators/toppings
class Pizza(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Unknown pizza"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        raise NotImplementedError


# Concrete pizza class
class ThinCrustPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Thin Crust Pizza"
        self.price = 80

    def cost(self):
        return self.price


# Concrete pizza class
class ThickCrustPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Thick Crust Pizza"
        self.price = 75

    def cost(self):
        return self.price


# Decorator/topping parent class (abstract)
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza) -> None:
        super().__init__()
        self.pizza = pizza

    @abstractmethod
    def get_description(self):
        raise NotImplementedError


# Concrete topping class
class Cheese(ToppingDecorator):
    def __init__(self, pizza: Pizza) -> None:
        super().__init__(pizza)
        self.description = "Cheese"
        self.price = 10

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def cost(self):
        return self.pizza.cost() + self.price


# Concrete topping class
class Olives(ToppingDecorator):
    def __init__(self, pizza: Pizza) -> None:
        super().__init__(pizza)
        self.description = "Olives"
        self.price = 15

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def cost(self):
        return self.pizza.cost() + self.price


# Concrete topping class
class Peppers(ToppingDecorator):
    def __init__(self, pizza: Pizza) -> None:
        super().__init__(pizza)
        self.description = "Peppers"
        self.price = 12

    def get_description(self):
        return f"{self.pizza.get_description()}, {self.description}"

    def cost(self):
        return self.pizza.cost() + self.price


def main():
    pizza = ThinCrustPizza()
    pizza = Cheese(pizza)
    print(f"{pizza.get_description()} - SEK{pizza.cost()}")
    pizza = Olives(pizza)
    print(f"{pizza.get_description()} - SEK{pizza.cost()}")
    pizza = Peppers(pizza)
    print(f"{pizza.get_description()} - SEK{pizza.cost()}")
    pizza = ThickCrustPizza()
    pizza = Cheese(pizza)
    print(f"{pizza.get_description()} - SEK{pizza.cost()}")
    pizza = Olives(pizza)
    print(f"{pizza.get_description()} - SEK{pizza.cost()}")
    pizza = Peppers(pizza)
    print(f"{pizza.get_description()} - SEK{pizza.cost()}")


if __name__ == "__main__":
    main()