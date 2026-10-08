import random

class Hero:
    def __init__(self, name, level=1, health=100, strength=20):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}! Уровень: {self.level}, Здоровье: {self.health}, Сила: {self.strength}"

    def attack(self):
        return "Герой наносит удар!"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье! Текущее здоровье: {self.health}"


class Warrior(Hero):
    def __init__(self, name, level=1, health=100, strength=20, stamina=50):
        super().__init__(name, level, health, strength)
        self.stamina = stamina  # Дополнительный атрибут

    # Переопределение метода attack (Полиморфизм)
    def attack(self):
        return f"{self.name} атакует мечом! (Расход выносливости: {self.stamina})"


class Mage(Hero):
    def __init__(self, name, level=1, health=100, strength=20, mana=80):
        super().__init__(name, level, health, strength)
        self.mana = mana  # Дополнительный атрибут

    # Переопределение метода attack (Полиморфизм)
    def attack(self):
        return f"{self.name} кастует заклинание! (Мана: {self.mana})"


class Assassin(Hero):
    def __init__(self, name, level=1, health=100, strength=20, stealth=100):
        super().__init__(name, level, health, strength)
        self.stealth = stealth  # Дополнительный атрибут

    # Переопределение метода attack (Полиморфизм)
    def attack(self):
        return f"{self.name} атакует из-под тишка! (Скрытность: {self.stealth})"

warrior_obj = Warrior(name="Конан", level=5, health=120, strength=30, stamina=60)
mage_obj = Mage(name="Гэндальф", level=6, health=80, strength=15, mana=100)
assassin_obj = Assassin(name="Эцио", level=4, health=95, strength=25, stealth=90)

heroes_pool = {
    'Warrior': warrior_obj,
    'Mage': mage_obj,
    'Assassin': assassin_obj
}


rules = {
    'Warrior': 'Assassin',
    'Assassin': 'Mage',
    'Mage': 'Warrior'
}

print("Добро пожаловать в игру!")
choice = input('Выберите героя (Warrior / Mage / Assassin): ').capitalize()

if choice not in heroes_pool:
    print('Ошибка! Неверный выбор героя.')
else:
    player_hero = heroes_pool[choice]
    comp_choice = random.choice(list(heroes_pool.keys()))
    comp_hero = heroes_pool[comp_choice]

    print(f"\nВы выбрали: {choice}")
    print(f"Противник: {comp_choice}\n")

    print("--- Знакомство и подготовка ---")
    print(player_hero.greet())
    print(comp_hero.greet())
    print("-" * 30 + "\n")

    if choice == comp_choice:
        print("Ничья! Оба героя использовали одинаковую тактику.")
    elif rules[choice] == comp_choice:
        print(player_hero.attack())
        print(f"Вы победили! {choice} оказался сильнее, чем {comp_choice}.")
        print(player_hero.rest())
    else:
        print(comp_hero.attack())
        print(f"{comp_choice} победил!")
        print(comp_hero.rest())





