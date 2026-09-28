class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        return f'Привет, я {self.name}, мой уровень {self.level}, здорьвье {self.health}, и сила {self.strength}'
    def attack(self):
        print(f'{self.name} наносит удар!')
        self.strength -= 1
        return f'Сила: {self.strength}'
    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health += 1
        return f'Здоровье: {self.health}'
try:
    артас = Hero('артас', 100, 1000, 87)
    терон = Hero('терон', 50, 119, 10)
    гулдан = Hero('гулдан',100, 120, 40)
    characters = {'артас':артас, 'терон':терон, 'гулдан':гулдан}
    name_hero = input('Выберите персонажа: ').lower()
    if name_hero in characters:
        chosen_hero = characters[name_hero]
    print(chosen_hero.greet())
    print(chosen_hero.attack())
    print(chosen_hero.rest())
except Exception as e:
    print('Такого персонажа не существует!')


