from creational.factory_method.animals import IAnimal, Shark, Dog, Penguin


class AnimalFactory:
    @staticmethod
    def get_animal_from_name(name: str) -> IAnimal:
        if name == "Shark":
            return Shark()
        if name == "Dog":
            return Dog()
        if name == "Penguin":
            return Penguin()
        raise Exception(f"Invalid animal name passed, {name} not present in factory")
