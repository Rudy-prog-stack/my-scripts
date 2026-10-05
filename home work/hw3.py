from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name: str, level: int, health: int, strength: int):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    @property
    def health(self):
        return self.__health

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию!")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")

warrior = Warrior(name="Конан", level=5, health=100, strength=15)
mage = Mage(name="Гэндальф", level=8, health=60, strength=5)
assassin = Assassin(name="Эцио", level=6, health=75, strength=10)

heroes = [warrior, mage, assassin]

for hero in heroes:
    hero.greet()
    hero.attack()
    hero.rest()
    print("-" * 30)