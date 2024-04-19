import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона. Здоровье {other.name}: {other.health}")

    def is_alive(self):
        return self.health > 0

    def reset_health(self):
        self.health = 100


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)
        self.player_wins = 0
        self.computer_wins = 0

    def play_round(self, first_attacker):
        current_turn = first_attacker
        while self.player.is_alive() and self.computer.is_alive():
            current_turn.attack(current_turn.opponent)
            current_turn = current_turn.opponent

            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает в этом раунде!")
                return self.player
            elif not self.player.is_alive():
                print(f"{self.computer.name} побеждает в этом раунде!")
                return self.computer
        return None

    def start(self):
        self.player.opponent = self.computer
        self.computer.opponent = self.player

        for round_number in range(1, 3):
            first_attacker = random.choice([self.player, self.computer])
            print(f"\nРаунд {round_number}: начинает {first_attacker.name}.")
            winner = self.play_round(first_attacker)
            if winner == self.player:
                self.player_wins += 1
            elif winner == self.computer:
                self.computer_wins += 1
            self.player.reset_health()
            self.computer.reset_health()

        if self.player_wins > self.computer_wins:
            print(f"\n{self.player.name} победил в игре!")
        elif self.computer_wins > self.player_wins:
            print(f"\n{self.computer.name} победил в игре!")
        else:
            print("\nИгра закончилась вничью!")

# Создание и запуск игры
player_name = input("Введите ваше имя героя: ")
computer_name = "Компьютерный Герой"
game = Game(player_name, computer_name)
game.start()
