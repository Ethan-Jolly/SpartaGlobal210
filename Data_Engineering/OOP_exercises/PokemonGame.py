import requests
import json
import random


class Game:

    def __init__(self, pokemon):
        self.ALL_POKEMON = pokemon

    def get_random_pokemon(self):
        # Getting a random pokemon json response
        random_pokemon = random.choice(self.ALL_POKEMON["results"])
        response = requests.get(random_pokemon["url"])
        return response.json()

    def get_pokemon_by_name(self, pokemon_name):
        found = False
        url = ''
        # Checking given name against all pokemon from response.
        for pokemon in self.ALL_POKEMON["results"]:
            if pokemon_name == pokemon['name']:
                found = True
                url = pokemon['url']
                break
        if found:
            return requests.get(url).json()
        else:
            print('Pokemon not found')
            return False

    def fight(self, pokemon1, pokemon2):
        # HP, ATTACK, DEFENCE, SPEC.ATK, SPEC.DEF, SPEED

        # Collects stats for both pokemon
        stats_p1 = [stat['base_stat'] for stat in pokemon1['stats']]
        stats_p2 = [stat['base_stat'] for stat in pokemon2['stats']]

        # Sets the starting health for both pokemon
        health_p1 = stats_p1[0]
        health_p2 = stats_p2[0]

        # Formatting the names to be capitalised
        pokemon1_name = pokemon1["name"].title()
        pokemon2_name = pokemon2["name"].title()
        print(f'{pokemon1_name} has {health_p1} base health')
        print(f'{pokemon2_name} has {health_p2} base health')
        print(f'{pokemon1_name} has {stats_p1[2]} base defence')
        print(f'{pokemon2_name} has {stats_p2[2]} base defence')

        # Checking the speed stats of both pokemon, the faster pokemon goes first
        if stats_p1[5] > stats_p2[5]:
            print(f'{pokemon1_name}, is faster, they attack first')
            order = 0
        elif stats_p1[5] < stats_p2[5]:
            print(f'{pokemon2_name}, is faster, they attack first')
            order = 1
        else:
            # If speed stat is the same randomly decide who goes first
            order = random.choice([0, 1])

        # Creating a loop where pokemon will fight until one has no health remaining
        while health_p1 > 0 and health_p2 > 0:
            # Creating a 50% chance for an attack to be a crit
            crit = random.choice([0, 1])
            if order == 0:
                if crit == 0:
                    print('Critical Hit!')
                    # If attack is a crit then attack can ignore defence
                    damage = stats_p1[1]
                else:
                    # Damage is calculated using attack stat - opponents defence stat
                    damage = max(0, stats_p1[1]-stats_p2[2])
                # Updates health of opponent
                health_p2 = max(0, health_p2-damage)
                order += 1
                print(f'{pokemon1_name} has done {damage} damage, {pokemon2_name} now has {health_p2} health.')
            else:
                if crit == 0:
                    print('Critical Hit!')
                    # If attack is a crit then attack can ignore defence
                    damage = stats_p2[1]
                else:
                    # Damage is calculated using attack stat - opponents defence stat
                    damage = max(0, stats_p2[1]-stats_p1[2])
                # Updates health of opponent
                health_p1 = max(0, health_p1-damage)
                order -= 1
                print(f'{pokemon2_name} has done {damage} damage, {pokemon1_name} now has {health_p1} health.')

            ignore = input('')

        # Checking who won the fight
        if health_p1 <= 0:
            return False
        elif health_p2 <= 0:
            return True

    def one_player(self):
        ai_pokemon = self.get_random_pokemon()
        # Asking if the player would like a random pokemon or not
        ask = input('Do you want random pokemon (y/n): ')
        player_pokemon = self.ask(ask)
        print(f'Your Pokemon is {player_pokemon["name"].title()} and you are fighting {ai_pokemon["name"].title()}')
        who_won = self.fight(player_pokemon, ai_pokemon)
        if who_won:
            print(f'The Computer won with {ai_pokemon["name"].title()}!')
        else:
            print(f'You won with {player_pokemon["name"].title()}!')

    def two_player(self):
        # Asking both player if they would like random pokemon or not
        ask_p1 = input('Player1, Do you want random pokemon (y/n): ')
        player1_pokemon = self.ask(ask_p1)
        ask_p2 = input('Player2, Do you want random pokemon (y/n): ')
        player2_pokemon = self.ask(ask_p2)

        print(f'Player 1, your Pokemon is {player1_pokemon["name"].title()} and Player 2 your Pokemon is {player2_pokemon["name"].title()}')
        who_won = self.fight(player1_pokemon, player2_pokemon)
        if who_won:
            print(f'Player 1 won with {player1_pokemon["name"].title()}!')
        else:
            print(f'Player 2 won with{player2_pokemon["name"].title()}!')

    def ask(self, player_response):
        if player_response == 'n':
            name = input('What is the name of your pokemon: ')
            player_pokemon = self.get_pokemon_by_name(name)
        else:
            player_pokemon = self.get_random_pokemon()
        return player_pokemon

    def start_game(self):
        ask = int(input('Do you want to play 1 or 2 player (1 or 2): '))
        if ask == 1:
            self.one_player()
        else:
            self.two_player()


def main():
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=1118').json()
    g = Game(pokemon)
    g.start_game()


if __name__ == '__main__':
    main()
