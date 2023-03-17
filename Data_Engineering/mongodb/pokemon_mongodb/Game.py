import requests
import json
import random
from pokemon import Pokemon
from connection import Client
import os
from dotenv import load_dotenv


class Game:
    def __init__(self, client, pokemon_database):
        self.client = client
        self.database = pokemon_database

    def get_random_pokemon(self):
        # Getting a random pokemon doc
        doc = self.database.aggregate([
            { "$sample": # Randomly samples 1 document from all the documents
             {"size": 1}
            },{ "$project":
             {'name':1,'stats':1}
            }
        ]

        )
        doc = list(doc)
        pokemon = Pokemon(doc)
        return pokemon

    def get_pokemon_by_name(self, pokemon_name):
        doc = self.database.find_one({'name':pokemon_name},{'name':1,'stats':1})
        pokemon = Pokemon([doc])
        return pokemon

    def fight(self, pokemon1, pokemon2):
        # HP, ATTACK, DEFENCE, SPEC.ATK, SPEC.DEF, SPEED

        # Sets the starting health for both pokemon
        health_p1 = pokemon1.health
        health_p2 = pokemon2.health

        # Formatting the names to be capitalised
        pokemon1_name = pokemon1.name.title()
        pokemon2_name = pokemon2.name.title()
        print('---------------------------------------')
        print(f'{pokemon1_name} has {health_p1} base health')
        print(f'{pokemon2_name} has {health_p2} base health')
        print('---------------------------------------')
        print(f'{pokemon1_name} has {pokemon1.defence} base defence')
        print(f'{pokemon2_name} has {pokemon2.defence} base defence')
        print('---------------------------------------')

        # Checking the speed stats of both pokemon, the faster pokemon goes first
        if pokemon1.speed > pokemon2.speed:
            print(f'{pokemon1_name}, is faster, they attack first')
            order = 0
        elif pokemon1.speed < pokemon2.speed:
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
                    damage = pokemon1.attack
                else:
                    # Damage is calculated using attack stat - opponents defence stat
                    damage = max(0, pokemon1.attack-pokemon2.defence)
                # Updates health of opponent
                health_p2 = max(0, health_p2-damage)
                order += 1
                print(f'{pokemon1_name} has done {damage} damage, {pokemon2_name} now has {health_p2} health.')
            else:
                if crit == 0:
                    print('Critical Hit!')
                    # If attack is a crit then attack can ignore defence
                    damage = pokemon2.attack
                else:
                    # Damage is calculated using attack stat - opponents defence stat
                    damage = max(0, pokemon2.attack-pokemon1.defence)
                # Updates health of opponent
                health_p1 = max(0, health_p1-damage)
                order -= 1
                print(f'{pokemon2_name} has done {damage} damage, {pokemon1_name} now has {health_p1} health.')

            ignore = input('')

        # Checking who won the fight
        if health_p2 <= 0:
            return False
        elif health_p1 <= 0:
            return True

    def one_player(self):
        ai_pokemon = self.get_random_pokemon()
        # Asking if the player would like a random pokemon or not
        ask = input('Do you want random pokemon (y/n): ')
        player_pokemon = self.ask(ask)
        print(f'Your Pokemon is {player_pokemon.name.title()} and you are fighting {ai_pokemon.name.title()}')
        who_won = self.fight(player_pokemon, ai_pokemon)
        if who_won:
            print(f'The Computer won with {ai_pokemon.name.title()}!')
            self.client.update_document_by_name(ai_pokemon.name, 'wins', 1)
        else:
            print(f'You won with {player_pokemon.name.title()}!')
            self.client.update_document_by_name(player_pokemon.name, 'wins', 1)

    def two_player(self):
        # Asking both player if they would like random pokemon or not
        ask_p1 = input('Player1, Do you want random pokemon (y/n): ')
        player1_pokemon = self.ask(ask_p1)
        ask_p2 = input('Player2, Do you want random pokemon (y/n): ')
        player2_pokemon = self.ask(ask_p2)

        print(f'Player 1, your Pokemon is {player1_pokemon.name.title()} and Player 2 your Pokemon is {player2_pokemon.name.title()}')
        who_won = self.fight(player1_pokemon, player2_pokemon)
        if who_won:
            print(f'Player 1 won with {player1_pokemon.name.title()}!')
            self.client.update_document_by_name(player1_pokemon.name, 'wins', 1)
        else:
            print(f'Player 2 won with{player2_pokemon.name.title()}!')
            self.client.update_document_by_name(player2_pokemon.name, 'wins', 1)

    def ask(self, player_response):
        if player_response == 'n':
            name = input('What is the name of your pokemon: ')
            player_pokemon = self.get_pokemon_by_name(name)
        else:
            player_pokemon = self.get_random_pokemon()
        return player_pokemon
    
    def print_leaderboard(self, field_name, limit):
        top = list(self.client.get_top_n(field_name, limit))
        print('-------------------------')
        print('The Pokemon Leader Board:')
        print('-------------------------')
        for item in top:
            print(f"{item['name']}, wins: {item[field_name]}")

    def start_game(self):
        ask = int(input('Do you want to play 1 or 2 player (1 or 2): '))
        if ask == 1:
            self.one_player()
        elif ask == 2:
            self.two_player()
        else:
            self.print_leaderboard('wins', 10)


def main():
    load_dotenv()
    MONGODB_URI = os.environ["MONGODB_URI"]
    client = Client(MONGODB_URI, 'pokemon_data','pokemon')
    coll = client.get_collection()
    g = Game(client, coll)
    g.start_game()


if __name__ == '__main__':
    main()