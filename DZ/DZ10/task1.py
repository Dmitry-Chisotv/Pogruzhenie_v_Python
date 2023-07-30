"""Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики."""


class AnimalFactory:

    def create_animal(animal_type, name, *args):
        if animal_type == 'Fish':
            return Fish(name, *args)
        elif animal_type == 'Bird':
            return Bird(name, *args)
        else:
            raise ValueError("Неподдерживаемый тип животного.")


class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
        pass


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        super().__init__(name)
        self.long = long

    def show_spec(self):
        if self.long <= self.LITTLE:
            return "Мелководная рыба"
        elif self.long <= self.HIGHT:
            return "Средне-глубоководная рыба"
        else:
            return "Глубоководная рыба"


class Bird(Animal):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length = length

    def show_spec(self):
        return self.length * 2



if __name__ == '__main__':
    fish1 = AnimalFactory.create_animal('Fish', 'Окунь', 5)
    fish2 = AnimalFactory.create_animal('Fish', 'Акула', 110)
    fish3 = AnimalFactory.create_animal('Fish', 'Камбала', 35)
    bird1 = AnimalFactory.create_animal('Bird', 'Ласточка', 15)

    animal_list = [fish3, fish2, fish1, bird1]
    for animal in animal_list:
        print(animal.show_spec())
